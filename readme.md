# Flask Number Guessing Game

Welcome to the Flask Number Guessing Game! This web application lets users guess a randomly generated number between 0 and 9. Users receive feedback on whether their guess is correct, too high, or too low.
<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="500" height="500" />

## Getting Started

To run the Flask Number Guessing Game locally, follow these steps:

1. Make sure you have Python installed on your machine.

2. Install the required packages using the following command:

   ```bash
   pip install Flask
3. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/flask-number-guessing-game.git
   ```
   
4. Navigate to the directory containing the repository.
5. ```bash
   cd flask-number-guessing-game
   ```
5. Run the following command to start the Flask server:

   ```bash
   python app.py
   ```
<br>
The application will be accessible at http://127.0.0.1:5000/ in your web browser.

## How to Play
* Open the application in your web browser. 
* You will see a home page with the title "Guess the number" and an animated GIF. 
* Enter a number in the URL to make a guess (e.g., http://127.0.0.1:5000/5). 
* Receive feedback on your guess along with an animated GIF:
  - If you guess correctly, you'll see a success message and a celebratory GIF.
  - If your guess is too high, you'll be notified with a message and an animated GIF indicating that it's too high.
  - If your guess is too low, you'll receive a message and an animated GIF indicating that it's too low.
  - Keep guessing until you get the correct number!

## Dependencies
* Flask
* random

## Acknowledgments
GIFs sourced from Giphy