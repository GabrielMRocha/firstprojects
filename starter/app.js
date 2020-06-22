/*
The Chicago dice game is a simple yet fun game. The rules are not very difficult and the game is decided by pure luck, but still it is very addictive. Once you start you might not want to stop to see if you can do better in the next game.

The game is played in 11 rounds, starting with round 2, then going to round 3 and continuing until round 12. In each round each player takes his or her turn and rolls both dice, trying to roll the number of that round. For example, in the round with number 2, you aim to roll a 1 on each dice giving you a total of 2.

Every player that rolls the number of the current round gets a point and adds it to his overall score. After all 11 rounds are finished the game ends and the player with the higher number of points is declared the winner.
*/

var scores, roundScore, activePlayer, tHrow, nRolls; //Creating basic variables

newbtn()
// rulebook
var modal = document.getElementById('mod');
var close = document.getElementsByClassName('close')[0];

document.querySelector('.rule-btn').addEventListener('click', function() {
    modal.style.display = 'block';
})

close.onclick = function() {
    modal.style.display = 'none';
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
    }
}

function players() {
    var player1 = prompt('Insert player 1', 'Player 1')
    var player2 = prompt('Insert player 2', 'Player 2')
    player1 ? document.getElementById('name-0').textContent = player1 : player1 = 'Player 1'
    player2 ? document.getElementById('name-1').textContent = player2 : player2 = 'Player 2'

}

function changePlayer(){
    document.querySelector('#current-' + activePlayer).textContent = 0;
    document.querySelector('.player-0-panel').classList.toggle('active');
    document.querySelector('.player-1-panel').classList.toggle('active');
    activePlayer === 0 ? activePlayer = 1 : activePlayer = 0; //ternary operator
    tHrow +=1
    document.querySelector('.number_roll').textContent = 'Throw '+tHrow;
    nRolls = 0;
    roundScore=0
    document.querySelector('.result').textContent = 'NOPE!'


}

function newbtn() {
    scores = [0,0]
    roundScore = 0;
    activePlayer = 0;
    nRolls=0;
    tHrow = 2;
    document.querySelector('#current-0').textContent = 0;
    document.querySelector('#current-1').textContent = 0;
    document.querySelector('#score-0').textContent = 0;
    document.querySelector('#score-1').textContent = 0;
    document.querySelector('.dice').style.display = 'none';
    document.querySelector('.number_roll').textContent = 'Throw '+tHrow;
    document.querySelector('.result').textContent = '';
    document.querySelector('.btn-roll').disabled = false;

}

setTimeout(players(),1000)
document.querySelector('.btn-roll').addEventListener('click', function() {
    if (tHrow < 12) {
        //roll the dice
        var dice = Math.floor(Math.random()*6+1);
        // display the result
        var diceDOM = document.querySelector('.dice');
        diceDOM.style.display = 'block';
        diceDOM.src = 'dice-' + dice + '.png'
        nRolls +=1
        //update the current value if the player did not lose
        if (dice<tHrow){
            roundScore += dice;
            if (roundScore < tHrow && nRolls < 2 && tHrow-dice <7 ) {
            document.querySelector('#current-' + activePlayer).textContent = roundScore;
            document.querySelector('.result').textContent = 'Roll once more'
            } else if (roundScore == tHrow) {
            document.querySelector('#score-' + activePlayer).textContent++
            document.querySelector('#current-' + activePlayer).textContent = 0;
            scores[activePlayer] += 1;
            tHrow +=1;
            nRolls = 0;
            activePlayer === 0 ? activePlayer = 1 : activePlayer = 0;
            document.querySelector('.number_roll').textContent = 'Throw '+tHrow;
            roundScore = 0
            document.querySelector('.result').textContent = 'Point for you';

            changePlayer()
            } else {
                //next player
                changePlayer()
            }
        } else {
            //Next Player
            changePlayer()
        }


    } else  {
        // 12 throws, define start new round
        result = document.querySelector('.result')
        scores[0] < scores[1] ? (document.querySelector('#OV-1').textContent++, result.textContent = 'Player 2 wins'): (scores[0] > scores[1] ? (document.querySelector('#OV-0').textContent++ , result.textContent = 'Player 1 wins' ) : document.querySelector('.result').textContent = 'That was a tie');
        setTimeout(function(){
            alert("Round over");
            newbtn()
     }, 100);
 }
})



document.querySelector('.btn-new_round').addEventListener('click', newbtn);
document.querySelector('.btn-new').addEventListener('click', function() {
    document.querySelector('#OV-0').textContent=0;
    document.querySelector('#OV-1').textContent=0;
    newbtn();
    players();

})


//document.querySelector('#current-' + activePlayer).innerHTML = '<em>' + dice + </em>;
