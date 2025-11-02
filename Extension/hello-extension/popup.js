document.getElementById("sayHello").addEventListener("click", async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    func: () => {
      alert("Hello from your Chrome Extension! 🎉");
    },
  });
});
