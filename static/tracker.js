fetch("https://ipapi.co/json/")
  .then(response => response.json())
  .then(data => {
    const trackerData = {
      ip: data.ip,
      city: data.city,
      country: data.country_name,
      browser: navigator.userAgent,
      language: navigator.language,
      platform: navigator.platform,
      screen: {
        width: window.screen.width,
        height: window.screen.height
      },
      referrer: document.referrer || "Direct",
      time: new Date().toISOString()
    };

    fetch("/tracker", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(trackerData)
    });
  });
