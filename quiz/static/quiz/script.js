const BASE_URL = "https://django-quiz-app-mf3p.onrender.com/quiz/";
const userId = "test_user";

document.addEventListener("DOMContentLoaded", () => {
    const startButton = document.querySelector("#start-quiz");
    const submitButton = document.querySelector("#submit-answer");
    const restartButton = document.querySelector("#restart-quiz");
    const resultsPage = document.querySelector("#results-page");

    if (startButton) {
        startButton.addEventListener("click", startQuiz);
    } else if (submitButton) {
        loadQuestion();
        submitButton.addEventListener("click", submitAnswer);
    } else if (restartButton) {
        restartButton.addEventListener("click", startQuiz);
    }
});

async function startQuiz() {
    const response = await fetch(`${BASE_URL}api-start/?user_id=${userId}`);
    const data = await response.json();
    alert(data.message);
    window.location.href = "/quiz/question/";
}

async function loadQuestion() {
    const response = await fetch(`${BASE_URL}api-question/`);
    const data = await response.json();
    document.getElementById("question-text").innerText = data.question_text;
    document.getElementById("question-text").dataset.questionId = data.id;

    const optionsList = document.getElementById("options");
    optionsList.innerHTML = "";
    data.options.forEach((option, index) => {
        const li = document.createElement("li");
        li.innerHTML = `<input type="radio" name="option" value="${index + 1}"> ${option}`;
        optionsList.appendChild(li);
    });
}

async function submitAnswer() {
    const selectedOption = document.querySelector('input[name="option"]:checked');
    if (!selectedOption) {
        alert("Please select an option!");
        return;
    }

    const questionId = document.getElementById("question-text").dataset.questionId;
    const response = await fetch(
        `${BASE_URL}api-submit/?user_id=${userId}&question_id=${questionId}&selected_option=${selectedOption.value}`
    );
    const data = await response.json();
    alert(data.result);
    window.location.href = "/quiz/question/";
}

async function loadResults() {

    const response = await fetch(`${BASE_URL}api-results/?user_id=${userId}`);
    const data = await response.json();
    document.getElementById("total-questions").innerText = data.total_questions;
    document.getElementById("correct-answers").innerText = data.correct_answers;
    document.getElementById("incorrect-answers").innerText = data.incorrect_answers;
}