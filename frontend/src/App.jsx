// File: frontend/src/App.jsx
import React, { useState } from "react";

export default function App() {
  const [pdf, setPdf] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    setPdf(file);

    if (file) {
      const formData = new FormData();
      formData.append("file", file);
      formData.append("source_type", "pdf");

      try {
        const response = await fetch("http://127.0.0.1:5000/upload", {
          method: "POST",
          body: formData,
        });

        const result = await response.json();
        if (!response.ok) throw new Error(result.error || "Upload failed");
        alert("PDF uploaded and processed.");
      } catch (error) {
        alert("Upload error: " + error.message);
      }
    }
  };

  const handleAsk = async () => {
    if (!question) return alert("Please enter a question");

    try {
      const response = await fetch("http://127.0.0.1:5000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });

      const result = await response.json();
      if (!response.ok) throw new Error(result.error || "Question failed");

      setAnswer(result.answer);
    } catch (error) {
      alert("Question error: " + error.message);
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "4rem", fontFamily: "sans-serif" }}>
      <h1>📖 <strong>Research Assistant</strong>
      </h1>
      <p style={{ marginTop: "-0.5rem", marginBottom: "2rem", color: "#555" }}>
        Upload a paper and ask questions about it
      </p>

      <div style={{ marginBottom: "2rem" }}>
        <strong>Upload your PDF:</strong>
        <br />
        <input type="file" onChange={handleFileChange} accept="application/pdf" />
      </div>

      <div style={{ marginBottom: "2rem" }}>
        <strong>Ask a question:</strong>
        <br />
        <input
          type="text"
          placeholder="e.g., What is this paper about?"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          style={{ width: "400px", padding: "0.4rem" }}
        />
        <br />
        <button style={{ marginTop: "0.5rem" }} onClick={handleAsk}>Ask</button>
      </div>

      {answer && (
        <div
          style={{
            maxWidth: "600px",
            margin: "0 auto",
            padding: "1rem",
            backgroundColor: "#f5f5f5",
            borderRadius: "8px",
          }}
        >
          <strong>Answer:</strong>
          <p style={{ whiteSpace: "pre-wrap" }}>{answer}</p>
        </div>
      )}
    </div>
  );
}