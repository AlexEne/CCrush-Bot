A python bot that plays Candy Crush.

Due to lack of time when I coded this I warn you that it's full of hardcoded stuff :).

This is how it works: 

1. Take a screenshot of the desktop
2. Extract the game board from it
3. From that game board extract each cell
4. Using a classification algorithm determine what candy is in each cell
5. Compute the best move using a greedy-like algorithm
6. Send Inputs to the browser window
7. Wait for the board to stabilize and all the movement to stop
8. Goto 1 :)

The main problem now is the fact that I hardcoded the position of the board in the screenshot. You need to ajust the offsets of it in order to match the ones for your browser and screen size.

It works with python 2.7 and needs the libraries: scikit-learn, PIL, win32api.

You can watch it in action here: https://www.youtube.com/watch?v=18vqQOPlvO4

There is a more in-depth explanation about how it works here: http://www.clickalot.me/2015/05/candy-crush-bot/
