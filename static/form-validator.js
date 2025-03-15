document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
  
    form.addEventListener("submit", function (e) {
      const phone = form.phone.value.trim();
      const postal = form.postal_code.value.trim();
  
      const phoneRegex = /^9[1236]\d{7}$/;
      const postalRegex = /^\d{4}-\d{3}$/;
  
      let errors = [];
  
      if (!phoneRegex.test(phone)) {
        errors.push("Número de telemóvel inválido (ex: 912345678)");
      }
  
      if (!postalRegex.test(postal)) {
        errors.push("Código Postal inválido (ex: 3800-211)");
      }
  
      if (errors.length > 0) {
        e.preventDefault();
        alert(errors.join("\n"));
      }
    });
  });
  