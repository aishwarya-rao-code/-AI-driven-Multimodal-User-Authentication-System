# Multimodal Biometric Authentication System

## Project Overview
This project is part of the midterm AI application requirement, where we have developed an **AI-driven Multimodal User Authentication System** that integrates **Face and Voice Biometrics**. By combining both modalities through **feature-level fusion**, the system significantly enhances authentication accuracy and security. We have applied advanced **machine learning and deep learning** techniques to achieve this.

For the **final project**, we will be evaluating trustworthiness aspects such as **fairness, privacy, robustness, and explainability** within this biometric system.

---
## Dataset Download Instructions
This project uses the following datasets:
- **[Caltech Face Dataset](https://doi.org/10.22002/D1.20237)**
- **[AudioMNIST](https://github.com/soerenab/AudioMNIST)**

To download the datasets:
- **Linux/Mac**: Run `./download_datasets.sh`
- **Windows**: Run `download_datasets.bat`

## Key Features

### 🔹 AI-Powered Biometric Authentication
- Uses **facial and voice recognition** to enhance security.

### 🔹 Feature-Level Fusion
- Merges **facial and voice features** to create a more robust representation.

### 🔹 Machine Learning and Deep Learning Models
- **Baseline Models**: Random Forest, SVM, k-NN.
- **Advanced Models**: CNNs and LSTMs for feature extraction.

### 🔹 Performance Metrics Visualization
- **Confusion Matrix**
- **Multiclass ROC Curve**
- **Score Distribution** for Genuine and Impostor Users
- **Equal Error Rate (EER)** and **d-prime calculations**

### 🔹 Trustworthiness Considerations
- **Bias detection and fairness analysis**
- **Privacy-preserving techniques** (encryption, differential privacy)
- **Explainable AI (XAI)** methods for transparency

### 🔹 User Interface
- **Tkinter-based UI** for easy interaction.
- **API integration** planned for real-world deployment.

---

## 📂 Project Files
| File | Description |
|------|-------------|
| `biometric_ui_with_final_project.py` | UI implementation using Tkinter to execute and display authentication results. |
| `Final_Project.py` | Main AI script handling biometric data processing, training models, and visualization. |
| `Multimodal_Authentication_System_Using_Face_and_Voice_Data.pdf` | Detailed project report covering methodology and findings. |
| `Screenshots/` | Sample outputs from the system, including Confusion Matrix, ROC Curve, and Score Distribution. |

---

## 🚀 How to Run the Application

### 1️⃣ Install Dependencies
```sh
pip install numpy opencv-python librosa scikit-learn imbalanced-learn matplotlib seaborn tkinter
```

### 2️⃣ Run the Biometric Authentication System
```sh
python biometric_ui_with_final_project.py
```

### 3️⃣ Interact with the UI
- Click on **"Run Biometric System"** to initiate authentication.
- View real-time results, including performance visualizations.

---

## 🔄 System Workflow

### 1️⃣ Data Collection and Preprocessing
- **Face images**: Resized, normalized, and edge features extracted.
- **Audio samples**: Resampled, MFCC & spectral contrast features extracted.

### 2️⃣ Feature-Level Fusion
- Facial and voice features are combined into a **single vector per user**.

### 3️⃣ Model Training
- **Stratified k-Fold Cross Validation (k=5)**.
- **SMOTE applied** for dataset balancing.

### 4️⃣ Performance Evaluation
- **Confusion Matrix** for classification accuracy.
- **Multiclass ROC Curve** to measure model performance.
- **Score Distribution** to compare genuine vs. impostor users.
- **Equal Error Rate (EER) and d-prime calculations**.

### 5️⃣ User Interface & API Development
- **Tkinter-based UI** allows users to run the system interactively.
- **API development** is ongoing for external system integration.

---

## 📊 Results Summary
| Metric | Face-Only | Voice-Only | Multimodal |
|--------|----------|-----------|------------|
| **Accuracy** | 99% | 95% | 99% |
| **ROC AUC** | 1.00 | 0.99 | 1.00 |
| **EER** | 0.0001 | 0.0149 | 0.0001 |
| **d-prime** | 11.98 | 4.93 | 12.22 |

**Key Insights:**
- **Multimodal authentication** performed **better** than unimodal systems.
- **SVM** delivered the best results, closely followed by **Random Forest**.
- **EER was significantly reduced**, enhancing security.

---

## 🔍 Trustworthiness Aspects (Final Project Focus)
For the final phase, we will focus on evaluating the following:

### ✅ **Fairness & Bias Detection**
- Analyse potential biases in model predictions across different demographics.

### ✅ **Privacy & Security**
- Implement **encryption and differential privacy** techniques to protect biometric data.

### ✅ **Explainability (XAI)**
- Use **SHAP and LIME** to interpret model decisions.

### ✅ **Robustness**
- Assess system resilience against **adversarial attacks** and **noisy inputs**.

---

## 🔮 Future Enhancements

### 🔹 Expand Deep Learning Models
- Implement **CNNs and LSTMs** for improved feature extraction.

### 🔹 Experiment with Fusion Techniques
- Extend beyond **feature-level fusion** to include **score-level and decision-level fusion**.

### 🔹 Enhance Dataset Diversity
- Incorporate **real-world samples** for better model generalization.

### 🔹 Improve User Interface
- Upgrade UI with **interactive visualizations** and **real-time authentication testing**.

### 🔹 Develop a Trustworthy AI Framework
- Focus on **fairness, robustness, and transparency** in biometric authentication.

---

## 👨‍💻 Developed by
- **Aishwarya Rao Kallepu**
- **Anil Reddy Vangala**
- **Shashidhar Reddy Kamatham**
