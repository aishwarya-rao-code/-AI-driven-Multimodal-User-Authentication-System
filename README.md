# Multimodal Biometric Authentication System (Final Project)

## Project Objective
This project is built on the midterm work where we developed an AI-powered Multimodal User Authentication System that combines Face and Voice Biometrics. For the final phase, we evaluated the system's trustworthiness based on key aspects:

- Privacy
- Fairness and Bias
- Robustness and Reliability
- Transparency and Explainability
- Accountability and Responsibility

We made sure the system not only performs well but is also secure and trustworthy for real-world use.

## Dataset Download Instructions
We used the following datasets:
- Caltech Face Dataset: https://doi.org/10.22002/D1.20237
- AudioMNIST Dataset: https://github.com/soerenab/AudioMNIST

Download instructions:
- Linux/Mac: `./download_datasets.sh`
- Windows: `download_datasets.bat`

## Key Features

- AI-powered authentication using face and voice together
- Feature-Level Fusion to combine modalities
- Machine Learning Models: Random Forest, SVM, k-NN
- Deep Learning for feature extraction: CNNs and LSTMs
- Performance metrics: Confusion Matrix, ROC Curve, EER, d-prime
- Tkinter-based GUI for real-time testing
- Privacy enhancement by hashing fused features
- Explainable AI using SHAP and LIME
- Robustness testing with noisy and blurred inputs

## Project Structure

| File | Description |
|------|-------------|
| `biometric_ui_with_final_project.py` | Tkinter GUI to run the system |
| `Final_Project.py` | Main code for data processing, training, and evaluation |
| `Screenshots/` | Folder containing output visualizations |
| `Multimodal_Authentication_System_Using_Face_and_Voice_Data.pdf` | Detailed report |

## How to Run

### Install Requirements
```bash
pip install numpy opencv-python librosa scikit-learn imbalanced-learn matplotlib seaborn tkinter
```

### Run the Application
```bash
python biometric_ui_with_final_project.py
```

### Interact
- Click "Run Biometric System" in the GUI
- View Confusion Matrix, ROC Curve, and authentication results

## System Workflow

1. Data Collection and Preprocessing (Face and Voice)
2. Feature Extraction
3. Feature-Level Fusion
4. Privacy: Save and Hash fused features
5. Train Models using Stratified K-Fold
6. Apply SMOTE for dataset balancing
7. Performance Evaluation
8. Explainability with SHAP and LIME
9. Robustness Testing with distortions

## Results Summary

| Metric | Face Only | Voice Only | Multimodal |
|--------|-----------|------------|------------|
| Accuracy | 99% | 95% | 99% |
| ROC AUC | 1.00 | 0.99 | 1.00 |
| EER | 0.0001 | 0.0149 | 0.0001 |
| d-prime | 11.98 | 4.93 | 12.22 |

**Insight:** Multimodal authentication is stronger than face-only or voice-only systems.

## Trustworthiness Aspects

| Aspect | What we did |
|--------|-------------|
| Privacy | Feature hashing, no raw data storage |
| Fairness | Used SMOTE to balance data |
| Transparency | SHAP and LIME visualizations |
| Robustness | Tested under noisy and blurred conditions |
| Reliability | Used Stratified K-Fold cross-validation |
| Accountability | Focused on data security and ethical design |

## Future Work

- Add Score-Level and Decision-Level Fusion
- Expand with larger and diverse datasets
- Improve GUI with real-time visual analytics
- Explore encryption for further privacy protection
- Complete demographic-based fairness evaluation

## Developed by
- Aishwarya Rao Kallepu
- Anil Reddy Vangala
- Shashidhar Reddy Kamatham

## Submission Notes
- Code and documentation organized
- README file updated clearly
- Trustworthiness evaluations done as per project objective
- Ready for final submission

---

> This project idea also takes reference from the Mobile Biometrics course project from last semester, where we studied the future of multimodal biometric systems.

---

Thank you for reviewing our work!
