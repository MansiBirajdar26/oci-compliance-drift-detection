import oci
import json
import datetime
import os

# Load OCI config
config = oci.config.from_file()
tenancy_id = config["tenancy"]

# Initialize clients
identity_client = oci.identity.IdentityClient(config)
network_client = oci.core.VirtualNetworkClient(config)
object_storage_client = oci.object_storage.ObjectStorageClient(config)

print("🔍 Collecting config snapshot...")

snapshot = {
    "timestamp": str(datetime.datetime.now()),
    "parameters": {}
}

# ── Parameter 1: Bucket visibility ──────────────────────────
print("  Checking bucket visibility...")
try:
    namespace = object_storage_client.get_namespace().data
    buckets = object_storage_client.list_buckets(
        namespace_name=namespace,
        compartment_id=tenancy_id
    ).data
    snapshot["parameters"]["buckets"] = [
        {
            "name": b.name,
            "is_public": getattr(b, 'public_access_type', 
                        getattr(b, 'access_type', 'NoPublicAccess')) != "NoPublicAccess"
        }
        for b in buckets
    ]
except Exception as e:
    snapshot["parameters"]["buckets"] = {"error": str(e)}

# ── Parameter 2: MFA status per user ────────────────────────
print("  Checking MFA status...")
try:
    users = identity_client.list_users(compartment_id=tenancy_id).data
    snapshot["parameters"]["mfa"] = [
        {
            "user": u.name,
            "mfa_active": u.is_mfa_activated
        }
        for u in users
    ]
except Exception as e:
    snapshot["parameters"]["mfa"] = {"error": str(e)}

# ── Parameter 3: Open ports in security lists ────────────────
print("  Checking open ports...")
try:
    compartments = identity_client.list_compartments(
        compartment_id=tenancy_id
    ).data
    open_ports = []
    for c in compartments:
        try:
            sls = network_client.list_security_lists(
                compartment_id=c.id
            ).data
            for sl in sls:
                for rule in sl.ingress_security_rules:
                    port = "all"
                    if hasattr(rule, 'tcp_options') and rule.tcp_options:
                        if rule.tcp_options.destination_port_range:
                            port = str(rule.tcp_options.destination_port_range.min)
                    open_ports.append({
                        "compartment": c.name,
                        "source": rule.source,
                        "port": port,
                        "risky": port in ["22", "3389", "all"]
                    })
        except Exception:
            continue
    snapshot["parameters"]["open_ports"] = open_ports
except Exception as e:
    snapshot["parameters"]["open_ports"] = {"error": str(e)}

# ── Parameter 4: Audit log retention period ──────────────────
print("  Checking audit retention...")
try:
    audit_client = oci.audit.AuditClient(config)
    retention = audit_client.get_configuration(tenancy_id).data
    snapshot["parameters"]["audit_retention"] = {
        "retention_period_days": retention.retention_period_days,
        "compliant": retention.retention_period_days >= 90
    }
except Exception as e:
    snapshot["parameters"]["audit_retention"] = {"error": str(e)}

# ── Parameter 5: Users without MFA (summary flag) ───────────
print("  Computing compliance flags...")
try:
    mfa_data = snapshot["parameters"].get("mfa", [])
    if isinstance(mfa_data, list):
        users_without_mfa = [u for u in mfa_data if not u["mfa_active"]]
        snapshot["parameters"]["mfa_compliance"] = {
            "total_users": len(mfa_data),
            "users_without_mfa": len(users_without_mfa),
            "compliant": len(users_without_mfa) == 0
        }
except Exception as e:
    snapshot["parameters"]["mfa_compliance"] = {"error": str(e)}

# ── Save snapshot ─────────────────────────────────────────────
os.makedirs("data/snapshots", exist_ok=True)
timestamp_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"data/snapshots/snapshot_{timestamp_str}.json"

with open(filename, "w") as f:
    json.dump(snapshot, f, indent=2)

print(f"\n✅ Snapshot saved: {filename}")
print(f"   Buckets found:   {len(snapshot['parameters'].get('buckets', []))}")
print(f"   Users found:     {len(snapshot['parameters'].get('mfa', []))}")
print(f"   Open ports:      {len(snapshot['parameters'].get('open_ports', []))}")