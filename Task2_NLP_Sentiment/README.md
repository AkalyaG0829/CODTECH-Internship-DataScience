# 🎬 Task 2 – IMDb Sentiment Analysis

## 📌 Overview
This project builds a sentiment classifier using the **IMDb movie review dataset**.  
It applies an **LSTM neural network** to classify reviews as **positive** or **negative**.

---

## ⚙️ Workflow
1. **Load Dataset** – 25k training reviews, 25k test reviews  
2. **Preprocess** – Padding sequences, decoding helper for text  
3. **Model** – Embedding → Dropout → LSTM → Dense layers  
4. **Training** – 6 epochs, batch size 128  
5. **Evaluation** – Accuracy, Loss, Confusion Matrix, Classification Report  
6. **Outputs** – Saved plots and trained model

---

## 📊 Results
- **Test Accuracy:** ~77%  
- **Test Loss:** ~0.56  
- **Classification Report:**
  - Negative reviews → Precision 0.73, Recall 0.85, F1 0.79  
  - Positive reviews → Precision 0.82, Recall 0.69, F1 0.75  
