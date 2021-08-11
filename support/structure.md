import basic os stuff
import sqlalchemy and migrate db
import models
import logging

setup logging

setup config / disc count / current player index / dice to keep

Print Intro

prompt and create players

create game with players

begin while loop:


  select current player and print the start of turn

  init vars for keeps[] and sets[]
    keeps[] is a list of indivicual dice that make up the x number of sets
    sets[] is the collections that get scored

  for loop for 10 turns

    clear message
    determin remaining dice to role

    role remaining dice and print the dice

    check if dice are scorable, break if not. turn is done

    if scorable, prompt which to keep

    if user keeps none (blank input) or enters x, then break
    if user selects dice, create a list of dice and append it to the sets

    add those dice to keeps

    if all 6 dice are in keeps (used in sets) we are done

  get score from the sets
  add points to players game

  clear screen and print how many points this round
  of there is a message print it as well
  print that round is over
  print current score in game


  Notify next player is up, sleep x seconds and go again

  check to see if game is done

  if it is declare the winner
  if no winner toggle current player (index)

