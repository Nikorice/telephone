// function to send user prompt and get generated image
function generateImage(prompt) {
    // make a POST request to /generate endpoint with the prompt data
    fetch("/generate", {
      method: "POST",
      body: JSON.stringify({ prompt: prompt }),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        // display generated image on the page
        document.getElementById("generated-image").src = data.image_url;
  
        // show the "pass image" button and hide the "generate image" button
        document.getElementById("pass-image-btn").style.display = "block";
        document.getElementById("generate-image-btn").style.display = "none";
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
  
  // function to send user guess and get next generated image
  function passImage(guess) {
    // make a POST request to /pass endpoint with the guess data
    fetch("/pass", {
      method: "POST",
      body: JSON.stringify({ guess: guess }),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.game_over) {
          // if game is over, redirect to the end page
          window.location.href = "/end";
        } else {
          // if game is not over, display next generated image and prompt for guess
          document.getElementById("generated-image").src = data.image_url;
          document.getElementById("guess-form").reset();
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
  
  // add event listener to "generate image" button
  document.getElementById("generate-image-btn").addEventListener("click", () => {
    // get user prompt from input field
    const prompt = document.getElementById("prompt-input").value.trim();
  
    // make sure user has entered a prompt
    if (!prompt) {
      alert("Please enter a prompt.");
      return;
    }
  
    // call generateImage function with user prompt as argument
    generateImage(prompt);
  });
  
  // add event listener to "pass image" button
  document.getElementById("pass-image-btn").addEventListener("click", () => {
    // get user guess from input field
    const guess = document.getElementById("guess-input").value.trim();
  
    // make sure user has entered a guess
    if (!guess) {
      alert("Please enter a guess.");
      return;
    }
  
    // call passImage function with user guess as argument
    passImage(guess);
  });
  