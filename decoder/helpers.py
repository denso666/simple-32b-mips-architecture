import json

def loadInsDict():
	try:
		file = open( "./instructions.json" )
		data = json.load( file )
		file.close()

		return data

	except Exception as e:
		print( e )
		return 0

def loadInsTypes():
	try:
		file = open( "./types.json" )
		data = json.load( file )
		file.close()

		return data
	except Exception as e:
		print( e )
		return 0

def loadInsFile( file_name ):
	try:
		file = open( file_name )
		data = file.read()
		file.close()
		return data.strip().split( "\n" )
		
	except Exception as e:
		print( e )
		return 0

def saveFile( file_name, instructions ):
	try:

		file = open( file_name, "w" )
		
		for l in instructions:
			file.writelines( [l, '\n'] )

		file.close()

		print( f"file saved as {file_name}" )

	except Exception as e:
		print( "Error to save instructions file" )
		print( e )
		return 0

def intToBinary( number, quantity ):
	return bin( int( number ) )[2:].zfill( quantity )