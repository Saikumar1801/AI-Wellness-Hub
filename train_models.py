import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import shap

CLEAN_DATA_PATH = 'cleaned_data.csv'
TARGET_COL = 'treatment'
X = pd.read_csv(CLEAN_DATA_PATH).drop(TARGET_COL, axis=1)
y = pd.read_csv(CLEAN_DATA_PATH)[TARGET_COL]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    'XGBoost': XGBClassifier(random_state=42, eval_metric='logloss'),
    'SVM': SVC(probability=True, random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42)
}

accuracies = {}
for name, model in models.items():
    print(f"Training {name}...")
    model.fit(X_train_scaled, y_train)
    accuracies[name] = accuracy_score(y_test, model.predict(X_test_scaled))
    print(f"✅ {name} Accuracy: {accuracies[name] * 100:.2f}%")

best_model_name = max(accuracies, key=accuracies.get)
best_model_object = models[best_model_name]
print(f"\n🏆 Best Model: {best_model_name} with {accuracies[best_model_name] * 100:.2f}% accuracy.")

print("\n--- Saving All Assets ---")
with open('best_model.pkl', 'wb') as f: pickle.dump(best_model_object, f)
print("✅ Model saved to 'best_model.pkl'")
with open('scaler.pkl', 'wb') as f: pickle.dump(scaler, f)
print("✅ Scaler saved to 'scaler.pkl'")
explainer = shap.Explainer(best_model_object)
with open('shap_explainer.pkl', 'wb') as f: pickle.dump(explainer, f)
print("✅ SHAP explainer saved to 'shap_explainer.pkl'")