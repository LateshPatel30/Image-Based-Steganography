document.getElementById('encryptForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
  
    const res = await fetch('/encrypt', {
      method: 'POST',
      body: formData
    });
  
    if (res.ok) {
      const blob = await res.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = "encryptedImage.png";
      a.click();
    } else {
      alert("Encryption failed.");
    }
  });
  
  document.getElementById('decryptForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
  
    const res = await fetch('/decrypt', {
      method: 'POST',
      body: formData
    });
  
    const data = await res.json();
    document.getElementById('output').textContent = data.message;
  });
  