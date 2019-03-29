#!/bin/bash
# ------------------------------------------------------------------
# [Author] Title
#          Description
# ------------------------------------------------------------------
#Variables
today=`date '+%Y-%m-%d %H:%M:%S'`;

#Add all new files
git add --all;

#Commit files locally
git commit -a -m "$today"; 

#Push to remote repo
git push https://github.com/ryanleonbutler/rpg_game.git;
