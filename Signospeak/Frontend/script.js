const body = document.querySelector("body"),
  nav = document.querySelector("nav"),
  modeToggle = document.querySelector(".dark-light"),
  sidebarOpen = document.querySelector(".sidebarOpen"),
  siderbarClose = document.querySelector(".siderbarClose");

let getMode = localStorage.getItem("mode");
if (getMode && getMode === "dark-mode") {
  body.classList.add("dark");
}

// js code to toggle dark and light mode
modeToggle.addEventListener("click", () => {
  modeToggle.classList.toggle("active");
  body.classList.toggle("dark");

  // js code to keep user selected mode even page refresh or file reopen
  if (!body.classList.contains("dark")) {
    localStorage.setItem("mode", "light-mode");
  } else {
    localStorage.setItem("mode", "dark-mode");
  }
});

//   js code to toggle sidebar
sidebarOpen.addEventListener("click", () => {
  nav.classList.add("active");
});

body.addEventListener("click", (e) => {
  let clickedElm = e.target;

  if (
    !clickedElm.classList.contains("sidebarOpen") &&
    !clickedElm.classList.contains("menu")
  ) {
    nav.classList.remove("active");
  }
});

document.addEventListener("DOMContentLoaded", function () {
  var questions = document.querySelectorAll(".question");

  questions.forEach(function (question) {
    var questionTitle = question.querySelector("h2");
    var answer = question.querySelector(".answer");

    questionTitle.addEventListener("click", function () {
      answer.style.display =
        answer.style.display === "block" ? "none" : "block";
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  var scrollToTopBtn = document.getElementById("scrollToTopBtn");

  // Show or hide the button based on scroll position
  window.addEventListener("scroll", function () {
    if (
      document.body.scrollTop > 20 ||
      document.documentElement.scrollTop > 20
    ) {
      scrollToTopBtn.style.display = "block";
    } else {
      scrollToTopBtn.style.display = "none";
    }
  });

  // Scroll to the top when the button is clicked
  scrollToTopBtn.addEventListener("click", function () {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const toggleNavButton = document.getElementById("toggleNav");
  const nav = document.querySelector("nav");

  toggleNavButton.addEventListener("click", function () {
    nav.style.display = nav.style.display === "block" ? "none" : "block";
  });
});

const notifications = [
  "Believe you can and you're halfway there.",
  "The only way to do great work is to love what you do.",
  "Keep your face always toward the sunshine—and shadows will fall behind you.",
  "Success is not final, failure is not fatal: It is the courage to continue that counts.",
  "The only limit to our realization of tomorrow will be our doubts of today.",
  "With the new day comes new strength and new thoughts.",
  "The best preparation for tomorrow is doing your best today.",
  "You are never too old to set another goal or to dream a new dream.",
  "What you get by achieving your goals is not as important as what you become by achieving your goals.",
  "The future belongs to those who believe in the beauty of their dreams.",
];

function showRandomNotification() {
  const randomIndex = Math.floor(Math.random() * notifications.length);
  const notificationText = notifications[randomIndex];

  const notificationContainer = document.getElementById(
    "notificationContainer"
  );

  const notification = document.createElement("div");
  notification.classList.add("notification");
  notification.innerText = notificationText;

  const closeButton = document.createElement("span");
  closeButton.classList.add("close-button");
  closeButton.innerHTML = "&times;";
  closeButton.onclick = function () {
    notificationContainer.removeChild(notification);
  };

  notification.appendChild(closeButton);
  notificationContainer.appendChild(notification);

  setTimeout(() => {
    notificationContainer.removeChild(notification);
  }, 10000); // Close notification after 10 seconds
}

function showRandomNotificationAfterDelay() {
  setTimeout(() => {
    showRandomNotification();
    showRandomNotificationAfterDelay(); // Recursively call to continue showing notifications
  }, 10000); // Show notification after 10 seconds
}

// Initial call to start showing notifications after 10 seconds
showRandomNotificationAfterDelay();

// chatbot

var chatbotContainer = document.getElementById("chatbotContainer");
var sendButton = document.querySelector(".send-button");
var userInput = document.getElementById("userInput");

function sendMessage() {
  var chat = document.getElementById("chat");

  if (userInput.value.trim() === "") {
    return;
  }

  var userMessage = document.createElement("div");
  userMessage.classList.add("user-message");
  userMessage.innerText = "You: " + userInput.value;
  chat.appendChild(userMessage);

  // Reset input field
  userInput.value = "";

  // Scroll to bottom
  chat.scrollTop = chat.scrollHeight;

  // Simulate bot response after 1 second
  setTimeout(sendBotResponse, 1000);
}

function sendBotResponse() {
  var botResponses = [
    "I understand.",
    "That's a good question.",
    "Interesting!",
    "I'm here to help.",
    "I'm still learning.",
    "Please ask me another question.",
    "Let me think about that...",
  ];

  var randomIndex = Math.floor(Math.random() * botResponses.length);
  var response = botResponses[randomIndex];

  var chat = document.getElementById("chat");
  var botMessage = document.createElement("div");
  botMessage.classList.add("bot-message");
  botMessage.innerText = "Chatbot: " + response;
  chat.appendChild(botMessage);

  // Scroll to bottom
  chat.scrollTop = chat.scrollHeight;
}

function closeChatbot() {
  chatbotContainer.style.display = "none";

  // Reappear chatbot after two minutes
  setTimeout(function () {
    chatbotContainer.style.display = "block";
  }, 120000); // 2 minutes in milliseconds
}

// Event listener for send button click
sendButton.addEventListener("click", sendMessage);

// Event listener for enter key press
userInput.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    sendMessage();
  }
});
