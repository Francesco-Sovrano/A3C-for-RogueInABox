#Copyright (C) 2017 Francesco Sovrano
#
#This file is part of Rogueinabox.
#
#Rogueinabox is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Rogueinabox is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

class RogueFrameInfo:
	def __init__(self, pixel, map, statusbar, screen):
		self.pixel = pixel
		self.map = map
		self.statusbar = statusbar
		self.screen = screen
		
	def get_tile_below_player(self):
		pos = self.get_player_pos( )
		return self.get_environment_tile_at(pos)
		
	def get_environment_tile_at(self, pos):
		x, y = pos
		if x >= 0 and y >= 0 and x < len(self.map) and y < len(self.map[x]):
			return self.map[x][y]
		return ' '

	def get_player_pos(self):
		if len(self.pixel["agents"]["@"])>0:
			return self.pixel["agents"]["@"][0]
		print("Error: no agent @ visible on screen")
		return (-1,-1)
		
	def has_statusbar(self):
		return not self.statusbar["is_empty"]
		
	def get_list_of_positions_by_tile( self, tile ):
		for key in self.pixel:
			if self.pixel[key].get(tile):
				return self.pixel[key][tile]
		return []
		
	def get_list_of_positions_by_type( self, type ):
		result = []
		type_list = self.pixel[type] 
		for key in type_list:
			result = list( set().union ( result, type_list[key] ) )
		return result
		
	def get_list_of_walkable_positions(self):
		passages = self.get_list_of_positions_by_tile("#")
		doors = self.get_list_of_positions_by_tile("+")
		floors = self.get_list_of_positions_by_tile(".")
		items = self.get_list_of_positions_by_type("items")
		return list(set().union(passages, doors, floors, items))

	def get_tile_count( self, tile ):
		return len( self.get_list_of_positions_by_tile(tile) )
				
	def get_type_count( self, type ):
		count = 0
		dict = self.pixel[type]
		for tile in dict:
			count += len(dict[tile])
		return count
				
	def get_known_tiles_count( self ):
		count = 0
		for key in self.pixel:
			count += self.get_type_count(key)
		return count