# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

# Mycroft libraries
from os.path import dirname,join
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util import play_mp3
from mycroft.util.log import getLogger

#required libraries
import time
import datetime
import requests         # http library, no known relation to re :)
from random import choice, sample

__author__ = 'GregV', '@lachendeKatze'

LOGGER = getLogger(__name__)

class DaysUntilChristmasSkill(MycroftSkill):
    def __init__(self):
        super(DaysUntilChristmasSkill, self).__init__(name="DaysUntilChristmasSkill")
	self.process = None

	self.songs = [ join(dirname(__file__), "polar_express.mp3"),
		       join(dirname(__file__), "let_it_snow.mp3"),	
		       join(dirname(__file__), "holly_jolly_christma.mp3"),
		       join(dirname(__file__), "frosty_the_snowman.mp3"),
		       join(dirname(__file__), "mr_grinch.mp3"),
		       join(dirname(__file__), "sugar_plum.mp3"),
		       join(dirname(__file__), "carol_of_bells.mp3")]	

    def initialize(self):
        self.load_data_files(dirname(__file__))
	self.register_intent_file('days.until.christmas.intent',self.handle_christmas)

    def handle_christmas(self,message):
	
	today = datetime.date.today()
	christmasDay = datetime.date(today.year, 12, 25)
	
	# in datetime atimetic, if a day is in the past, it is 'negative' or less 
        # than today, or less than a day in the future
        # check to see if christmas is past :( if so, correct to next year :(
	if christmasDay < today:
		christmasDay = christmasDay.replace(year=today.year+1)
	
	daysUntilChristmas = abs(christmasDay - today)
	# r = requests.get('http://10.0.0.101/christmas?days=' + str(daysUntilChristmas.days))
	self.speak("there are " + str(daysUntilChristmas.days) + " days until christmas")
	time.sleep(3)
	self.process = play_mp3(choice(self.songs))
	
    def stop(self):
	pass

def create_skill():
	return DaysUntilChristmasSkill()
		
