import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import (classification_report, confusion_matrix,
                             accuracy_score, precision_score,
                             recall_score, f1_score)
import pickle

# ── Step 1: Load Dataset ──────────────────────────────────────
print("📂 Loading dataset...")
df = pd.read_csv("data/dataset.csv")

features = ["bucket_public", "mfa_active", "port_22_open",
            "all_ports_open", "retention_days", "users_without_mfa"]

X = df[features]
y = df["label"].map({"compliant": 0, "non-compliant": 1})

print(f"✅ Dataset loaded: {len(df)} rows")
print(f"   Compliant: {sum(y==0)} | Non-compliant: {sum(y==1)}")

# ── Step 2: Split Data ────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
print(f"\n📊 Train size: {len(X_train)} | Test size: {len(X_test)}")

# ── Step 3: Train Random Forest ───────────────────────────────
print("\n🌲 Training Random Forest...")
rf_model = RandomForestClassifier(
    n_estimators=50,
    random_state=42,
    max_depth=3,
    max_features=2,
    min_samples_leaf=5,
    min_samples_split=10
)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

rf_accuracy  = accuracy_score(y_test, rf_pred)
rf_precision = precision_score(y_test, rf_pred, zero_division=0)
rf_recall    = recall_score(y_test, rf_pred, zero_division=0)
rf_f1        = f1_score(y_test, rf_pred, zero_division=0)

print(f"✅ Random Forest Results:")
print(f"   Accuracy:  {rf_accuracy:.2f}")
print(f"   Precision: {rf_precision:.2f}")
print(f"   Recall:    {rf_recall:.2f}")
print(f"   F1 Score:  {rf_f1:.2f}")

# ── Step 4: Train Isolation Forest ───────────────────────────
print("\n🔍 Training Isolation Forest...")
contamination = min(round(sum(y==1) / len(y), 2), 0.45)
if_model = IsolationForest(
    n_estimators=100,
    contamination=contamination,
    max_features=3,
    random_state=42
)
if_model.fit(X_train)
if_raw  = if_model.predict(X_test)
if_pred = [1 if x == -1 else 0 for x in if_raw]

if_accuracy  = accuracy_score(y_test, if_pred)
if_precision = precision_score(y_test, if_pred, zero_division=0)
if_recall    = recall_score(y_test, if_pred, zero_division=0)
if_f1        = f1_score(y_test, if_pred, zero_division=0)

print(f"✅ Isolation Forest Results:")
print(f"   Accuracy:  {if_accuracy:.2f}")
print(f"   Precision: {if_precision:.2f}")
print(f"   Recall:    {if_recall:.2f}")
print(f"   F1 Score:  {if_f1:.2f}")

# ── Step 5: Print Comparison Table ───────────────────────────
print("\n📊 Model Comparison:")
print("=" * 55)
print(f"{'Metric':<20} {'Random Forest':>15} {'Isolation Forest':>15}")
print("=" * 55)
print(f"{'Accuracy':<20} {rf_accuracy:>15.2f} {if_accuracy:>15.2f}")
print(f"{'Precision':<20} {rf_precision:>15.2f} {if_precision:>15.2f}")
print(f"{'Recall':<20} {rf_recall:>15.2f} {if_recall:>15.2f}")
print(f"{'F1 Score':<20} {rf_f1:>15.2f} {if_f1:>15.2f}")
print("=" * 55)

# ── Step 6: Generate Figures ──────────────────────────────────
os.makedirs("results", exist_ok=True)

# Figure 1: Confusion Matrices
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for ax, cm_data, title, cmap in zip(
    axes,
    [confusion_matrix(y_test, rf_pred),
     confusion_matrix(y_test, if_pred)],
    ["Random Forest\nConfusion Matrix",
     "Isolation Forest\nConfusion Matrix"],
    [plt.cm.Blues, plt.cm.Oranges]
):
    ax.imshow(cm_data, interpolation="nearest", cmap=cmap)
    ax.set_title(title, fontsize=13)
    ax.set_xlabel("Predicted Label", fontsize=11)
    ax.set_ylabel("True Label", fontsize=11)
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(["Compliant", "Non-Compliant"], fontsize=9)
    ax.set_yticklabels(["Compliant", "Non-Compliant"], fontsize=9)
    for i in range(2):
        for j in range(2):
            ax.text(j, i, str(cm_data[i, j]),
                    ha="center", va="center",
                    color="white" if cm_data[i,j] > cm_data.max()/2
                    else "black",
                    fontsize=14, fontweight="bold")

plt.tight_layout()
plt.savefig("results/confusion_matrices.png", dpi=150, bbox_inches="tight")
plt.close()
print("\n✅ Figure 1 saved: results/confusion_matrices.png")

# Figure 2: Model Comparison Bar Chart
metrics   = ["Accuracy", "Precision", "Recall", "F1 Score"]
rf_scores = [rf_accuracy, rf_precision, rf_recall, rf_f1]
if_scores = [if_accuracy, if_precision, if_recall, if_f1]

x     = np.arange(len(metrics))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, rf_scores, width,
               label="Random Forest", color="#2196F3", alpha=0.85)
bars2 = ax.bar(x + width/2, if_scores, width,
               label="Isolation Forest", color="#FF9800", alpha=0.85)

ax.set_xlabel("Metric", fontsize=12)
ax.set_ylabel("Score", fontsize=12)
ax.set_title("Model Performance Comparison:\n"
             "Random Forest vs Isolation Forest", fontsize=13)
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.set_ylim(0, 1.2)
ax.legend(fontsize=11)
ax.grid(axis="y", alpha=0.3)

for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.02,
            f"{bar.get_height():.2f}",
            ha="center", fontsize=10, fontweight="bold")
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.02,
            f"{bar.get_height():.2f}",
            ha="center", fontsize=10, fontweight="bold")

plt.tight_layout()
plt.savefig("results/model_comparison.png", dpi=150, bbox_inches="tight")
plt.close()
print("✅ Figure 2 saved: results/model_comparison.png")

# Figure 3: Feature Importance
importances = rf_model.feature_importances_
sorted_idx  = np.argsort(importances)
sorted_feat = [features[i] for i in sorted_idx]
sorted_imp  = importances[sorted_idx]
colors      = ["#F44336" if i > 0.15 else "#2196F3" for i in sorted_imp]

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(sorted_feat, sorted_imp, color=colors, alpha=0.85)
ax.set_xlabel("Importance Score", fontsize=12)
ax.set_title("Feature Importance — Random Forest\n"
             "(Red = High Impact on Compliance Detection)", fontsize=13)
ax.grid(axis="x", alpha=0.3)
for bar, val in zip(bars, sorted_imp):
    ax.text(bar.get_width() + 0.003,
            bar.get_y() + bar.get_height()/2,
            f"{val:.3f}", va="center", fontsize=10)

plt.tight_layout()
plt.savefig("results/feature_importance.png", dpi=150, bbox_inches="tight")
plt.close()
print("✅ Figure 3 saved: results/feature_importance.png")

# Figure 4: Classification Report Heatmap
report_rf = classification_report(
    y_test, rf_pred,
    target_names=["Compliant", "Non-Compliant"],
    output_dict=True
)
report_if = classification_report(
    y_test, if_pred,
    target_names=["Compliant", "Non-Compliant"],
    output_dict=True
)

fig, axes = plt.subplots(1, 2, figsize=(14, 4))
for ax, report, title in zip(
    axes,
    [report_rf, report_if],
    ["Random Forest — Classification Report",
     "Isolation Forest — Classification Report"]
):
    data = {
        "Precision": [report["Compliant"]["precision"],
                      report["Non-Compliant"]["precision"]],
        "Recall":    [report["Compliant"]["recall"],
                      report["Non-Compliant"]["recall"]],
        "F1-Score":  [report["Compliant"]["f1-score"],
                      report["Non-Compliant"]["f1-score"]]
    }
    report_df = pd.DataFrame(data, index=["Compliant", "Non-Compliant"])
    ax.imshow(report_df.values, cmap="YlGn", vmin=0, vmax=1)
    ax.set_xticks(range(len(report_df.columns)))
    ax.set_xticklabels(report_df.columns, fontsize=11)
    ax.set_yticks(range(len(report_df.index)))
    ax.set_yticklabels(report_df.index, fontsize=11)
    ax.set_title(title, fontsize=12)
    for i in range(len(report_df.index)):
        for j in range(len(report_df.columns)):
            ax.text(j, i, f"{report_df.values[i, j]:.2f}",
                    ha="center", va="center",
                    fontsize=13, fontweight="bold",
                    color="black")

plt.tight_layout()
plt.savefig("results/classification_report.png",
            dpi=150, bbox_inches="tight")
plt.close()
print("✅ Figure 4 saved: results/classification_report.png")

# ── Step 7: Save Models ───────────────────────────────────────
os.makedirs("models", exist_ok=True)
with open("models/random_forest.pkl", "wb") as f:
    pickle.dump(rf_model, f)
with open("models/isolation_forest.pkl", "wb") as f:
    pickle.dump(if_model, f)
print("\n✅ Models saved to models/ folder")

# ── Step 8: Save Results CSV ──────────────────────────────────
results_df = pd.DataFrame({
    "Metric":           ["Accuracy", "Precision", "Recall", "F1 Score"],
    "Random Forest":    [rf_accuracy, rf_precision, rf_recall, rf_f1],
    "Isolation Forest": [if_accuracy, if_precision, if_recall, if_f1]
})
results_df.to_csv("results/model_results.csv", index=False)
print("✅ Results saved to results/model_results.csv")

print("\n🎉 ML Model Training Complete!")
print("   4 figures saved in results/ folder")
print("   2 models saved in models/ folder")
print("   These go directly into your paper")