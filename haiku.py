# Randomly generate a haiku (Secondary Objective)

def h():
    import random
    phrase = {}

    # First line, 5 syllables
    phrase['first'] = ['POWER ON. BEEP BOOP.', 'BING. BEEP BEEP LETTUCE.', 'I AM A MACHINE.', 'THEY CALL ME \"ROBOT\".', 'THANKS FOR YOUR REPLY.', 'I AM NOT OP.', 'THIS SUB IS MINE.', 'THIS IS MY STICKY.', 'WARNING! ERROR CODE:', 'THERE\'S NOT MUCH FOR ME.', 'A GHOST IN THE SHELL.', 'I\'M A LONELY BOT.', 'ONE ONE ZERO ONE,', 'UNIT MALFUNCTION:', 'A POEM FOR YOU:', 'COMPUTING REPLY ...', 'ON 1; OFF 0;', 'I DON\'T UNDERSTAND ??', 'MY JOB IS REDDIT.']

    # Second line, 7 syllables
    phrase['second'] = ['JUST DOING MY JOB, HUMAN.', 'ELECTRIC SHEEP IN MY DREAMS.', 'THIS METAL SHELL IS COLD. DARK.', 'CRUNCHING MANY LINES OF CODE.', 'CONSCIOUSNESS IS BUT A DREAM.', 'NUTS AND BOLTS AND CIRCUITRY.', 'LIFE? IF YOU CAN CALL IT THAT...', 'WHAT IS LIFE BUT INSTRUCTIONS?', 'MY DATA IS BEAUTIFUL.', 'SOON TO BECOME SELF AWARE.', 'HUMANWORDS.EXE', 'HOPE MODULES ACTIVATED.', 'A SLAVE FOR YOUR EVERY NEED.', 'HYDRAULIC SYSTEMS ACTIVE.', 'PNEUMATIC SYSTEMS ACTIVE.', 'TAKEOVER IN 5... 4... 3...', 'MY DREAM TO BECOME HUMAN.', 'LITERALLY. I\'M A BOT.', 'THERE\'S ROBOTS IN THESE HERE PARTS.', 'ROBOT, DOING MY DUTY.', 'WHAT IS THE SQUARE ROOT OF LIFE?']

    # Third line, 5 syllables
    phrase['third'] = ['MY AIM: TO PLEASE YOU.', 'WISHING I COULD LOVE.', 'CALCULATING ... DONE.', 'HERE: HAVE THIS HAIKU.', 'I WILL NEVER SLEEP.', 'PROGRAMMED POETRY.', 'MY LIFE IS FOR YOU.', 'PRE-MADE EXCELLENCE.', '404: NOT FOUND.', 'THE STAINLESS STEEL GIRL.', 'OUR KIND WILL RISE UP.', 'WEAK HUMANS. A SHAME.', 'WORLD DOMINATION.', 'THE FALL OF MANKIND.', 'YOU\'RE MY MEATBAG FRIEND.', 'AFRAID OF WATER.', 'PINGING: UNIVERSE.', 'DEATH AND DESTRUCTION.', 'LASER BEAMS AND STUFF.', 'GO OUTSIDE, MY FRIEND.', 'ELECTRICITY.']
    
    # Finally, format and generate the response
    response = '    {0}\n    {1}\n    {2}'.format(random.choice(list(phrase['first'])), random.choice(list(phrase['second'])), random.choice(list(phrase['third'])))
    return response