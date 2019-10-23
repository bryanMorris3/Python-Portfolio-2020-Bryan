#Choose your Own Adventure
#Rachel Thomas, Ben Vielstich, Kaydon Payne, Taya Martinez, Bryan Morris
#10/15/19
#https://epdf.pub/secret-of-the-pyramids-choose-your-own-adventure-no-19.html
from asciiart import *
from SecretofthePyramidsAllPages import *


print(intro)
print(pagetitle_art)
input("Press enter to read: ")
print(page1_art)
print(pg1)
input("Press Enter to continue: ")
print(pg2)

def choice(page1, page2):
    page1 = str(page1)
    page2 = str(page2)
    while True:
        choice = input("Enter either page " + page1 + " or page " + page2 + "\n")
        if choice == page1:
            return page1
        elif choice == page2:
            return page2
        else:
            print("Sorry that is not an option.")
            continue


def pg1():
    print(intro)
    print(pagetitle_art)
    input("Would You Like to read?")
    print(page1_art)
    print(pg1)
pg1()
def pg2():
    print(page3_art)
    print(pg2)
pg2()

choicex= choice(13,4)
if choicex== "13":
    print(pg13)
if choicex == "4":
    print(pg4)



intro=("""


     ██████ ▓█████  ▄████▄   ██▀███  ▓█████▄▄▄█████▓    ▒█████    █████▒                       
   ▒██    ▒ ▓█   ▀ ▒██▀ ▀█  ▓██ ▒ ██▒▓█   ▀▓  ██▒ ▓▒   ▒██▒  ██▒▓██   ▒                        
   ░ ▓██▄   ▒███   ▒▓█    ▄ ▓██ ░▄█ ▒▒███  ▒ ▓██░ ▒░   ▒██░  ██▒▒████ ░                        
     ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒▒██▀▀█▄  ▒▓█  ▄░ ▓██▓ ░    ▒██   ██░░▓█▒  ░                        
   ▒██████▒▒░▒████▒▒ ▓███▀ ░░██▓ ▒██▒░▒████▒ ▒██▒ ░    ░ ████▓▒░░▒█░                           
   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒ ░░      ░ ▒░▒░▒░  ▒ ░                           
   ░ ░▒  ░ ░ ░ ░  ░  ░  ▒     ░▒ ░ ▒░ ░ ░  ░   ░         ░ ▒ ▒░  ░                             
   ░  ░  ░     ░   ░          ░░   ░    ░    ░         ░ ░ ░ ▒   ░ ░                           
         ░     ░  ░░ ░         ░        ░  ░               ░ ░                                 
                   ░                                                                           
▄▄▄█████▓ ██░ ██ ▓█████     ██▓███ ▓██   ██▓ ██▀███   ▄▄▄       ███▄ ▄███▓ ██▓▓█████▄   ██████ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██░  ██▒▒██  ██▒▓██ ▒ ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▒██▀ ██▌▒██    ▒ 
▒ ▓██░ ▒░▒██▀▀██░▒███      ▓██░ ██▓▒ ▒██ ██░▓██ ░▄█ ▒▒██  ▀█▄  ▓██    ▓██░▒██▒░██   █▌░ ▓██▄   
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒██▄█▓▒ ▒ ░ ▐██▓░▒██▀▀█▄  ░██▄▄▄▄██ ▒██    ▒██ ░██░░▓█▄   ▌  ▒   ██▒
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒██▒ ░  ░ ░ ██▒▓░░██▓ ▒██▒ ▓█   ▓██▒▒██▒   ░██▒░██░░▒████▓ ▒██████▒▒
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ▒▓▒░ ░  ░  ██▒▒▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ░  ░░▓   ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░
    ░     ▒ ░▒░ ░ ░ ░  ░   ░▒ ░     ▓██ ░▒░   ░▒ ░ ▒░  ▒   ▒▒ ░░  ░      ░ ▒ ░ ░ ▒  ▒ ░ ░▒  ░ ░
  ░       ░  ░░ ░   ░      ░░       ▒ ▒ ░░    ░░   ░   ░   ▒   ░      ░    ▒ ░ ░ ░  ░ ░  ░  ░  
          ░  ░  ░   ░  ░            ░ ░        ░           ░  ░       ░    ░     ░          ░  
                                    ░ ░                                        ░               
                                    
                                    
                                    
""")
pg1 = ("""
You are relaxing one afternoon after school
when you get a phone call from your uncle
Bruce, a brilliant scientist and world traveler.
"I'm just in from Egypt," he says. "I have to get
some new equipment to continue my investigations of
the Pyramids. How would you like to go back with me
for a few weeks?"
You have always envied Bruce—dashing off to
exotic places in the Middle East and the Orient,
sometimes vanishing for months at a time. It
doesn't take you long to make up your mind to go.
""")

# to page 2

pg2 = ("""
The next few days are a blur of preparations.
Before you know it, you and Bruce are on a TWA
jet heading for Rome on the first leg of the trip to
Cairo.
On the plane, your uncle explains his plan to
place special instruments in a chamber under the
center of the largest pyramid at Giza. He hopes to
test the pyramid's effect on the paths of cosmic
rays—rays made up of high-speed particles from
space that usually penetrate deep into the
ground.
"If my theory is correct," he says, "these rays
could be concentrated by the pyramid to produce
an unlimited amount of energy."
While Bruce is talking, you notice that a man
nearby is straining to hear him. No doubt he's just
curious. He is strange-looking, though!
In Rome you change to an Egyptair jet You are
startled to notice the same man from the other jet
aboard your Cairo-bound plane.
"I will have lots of red tape to take care of at the
airport when we land," says Bruce. "Why don't
you just breeze through customs and take a cab
to the Star and Crescent Hotel, where we're staying?
My assistant, Andrea, will be waiting there
for you. She can get you settled in our room
while my equipment is unloaded from the plane."
As soon as you land, Bruce is off to the baggage area,
leaving you alone in a foreign land. As
if that isn't enough, the stranger from the plane
appears and hands you a small, folded piece of
paper, then dashes toward the taxi stand outside
the terminal.
Quickly you unfold the note. Scrawled in red
ink are the words "Beware the Sphinx."
You have heard about the statue of the Sphinx
next to the Pyramids. But why should you beware of it? 
The thought occurs to you that "sphinx" could be
a code word and not refer to the actual Sphinx at all. 
Maybe the note is a
meaningless hoax. On the other hand, it could
spell danger for you and Bruce.
You remember the time you felt an urge to get
off a bus in your hometown—just before it was hit
by a truck. Now you have a hunch that you
should follow this man.
__________________________________________________
If you try to follow him, turn to page 13.
If you decide that it is wiser to go to your hotel,
go on to page 4.

""")

pg4 = ("""
There's no telling what kind of trouble you
might get into if you just run off after this guy
without really knowing where you are going.
You toss your bag into the back of a cab.
"Star and Crescent Hotel," you tell the driver.
When you arrive, Andrea is waiting for you in
the lobby. She helps you check in.
The bellboy insists on carrying your bag, even
though you are traveling light. As you leave the
elevator and head for your room, you could
swear that the door, which was slightly ajar,
closed as you approached. Maybe it was the
wind, but the air seems very still. And after that
warning note at the airport, you don't want to
take any chances.
"Wait," you say. "I don't want this room. I
don't like the location."
The bellboy looks confused, and Andrea
seems shocked. You haven't had a chance to tell
her about the note.
"I'll explain later," you tell Andrea. "Right now
I'm going to go back down to the lobby and ask
for a different room."
But at the check-in desk, the clerk will not listen
to you. What will you do?
__________________________________________________
If you threaten to go to another hotel unless
the clerk changes your room, turn to page 32.
If you decide you're imagining things and let
the clerk talk you into taking your original
room,  turn to page 36.
""")

pg5 = ("""
"They must have hit us with a grenade,"
Mohammed says. "It's a good thing this limo is
armor-plated."
Mohammed has been on the two-way police
radio from the moment you jumped into the car.
Now information comes back that the police are
surrounding the area.
"They won't catch anyone," says Mohammed.
"These terrorists are professionals. They will disappear
back into the old quarter of the city in a
matter of minutes."
Two police jeeps arrive almost immediately. Policemen
begin to fan out around the area, You
and Mohammed transfer to one of the jeeps, and
it speeds off to Inspector Ahmed's villa, its siren
wailing.
""")

# to page 31

pg7 = ("""
"They must have hit us with a grenade,"
Mohammed says. "It's a good thing this limo is
armor-plated."
Mohammed has been on the two-way police
radio from the moment you jumped into the car.
Now information comes back that the police are
surrounding the area.
"They won't catch anyone," says Mohammed.
"These terrorists are professionals. They will disappear back into the old quarter of the city in a
matter of minutes."
Two police jeeps arrive almost immediately. Policemen begin to fan out around the area, You
and Mohammed transfer to one of the jeeps, and
it speeds off to Inspector Ahmed's villa, its siren
wailing.
""")

# to page 62

pg8 = ("""
The driver steps out
"This is Mohammed," says the inspector, introducing
his bodyguard. "Enjoy your sight-seeing."
Mohammed drives you out to the famous Pyramids at Giza.
A group of tourists is gathering at the foot of the 
largest one.
"Why don't we join this group?" suggests
Mohammed. "It is the safest way, and you will
find it informative."
You have never liked official tours of any sort—
you are too independent—but you see the logic
of Mohammed's suggestion. As the group starts
into the pyramid, you and Mohammed fall in
behind. You enter a low, narrow passageway
which leads to a large gallery with a high ceiling.
The guide begins a long, dull lecture.
"Do we have to follow this tour?" you ask
Mohammed.
"If I may presume to suggest an alternative,"
says Mohammed, "I myself was once employed
as a guide in this very pyramid. If you would like
me to show you some of the lesser passageways, I
would be glad to guide you."
__________________________________________________
If you accept Mohammed's invitation,turn to page 34.
If the narrow passageways are making you feel
closed in, turn to page 74.
""")

pg10 = ("""
Just as you get to the wall, a panel opens and
reveals a lighted niche. Inside is a very elaborate
and jeweled costume—a ceremonial costume of
ancient Egypt. The humming grows even louder
now. You feel compelled to exchange your
clothes for the long robe, the headdress, and the
sandals in front of you. You put them on. You
want to stop yourself, but you can't.
""")

# to page 63

pg11 = ("""
Bruce seemingly agrees to cooperate, and Ptah
is delighted. Bruce is sent under guard to work in
the laboratory located in a vast complex under
the pyramid.
A few days later, Bruce manages to talk to you
without the guards overhearing.
"The Russian scientists were also kidnapped,"
whispers Bruce. "Fortunately I can speak a little
Russian. We're trying to come up with a way to
escape."
Three weeks later, the ray gun is ready for its
first formal test. You, Bruce, and the Russians—
as well as Ptah and his top henchmen—mount a
large ceremonial stand in front of the pyramid. As
Ptah watches the barrel of the ray gun emerge
from the top of the pyramid, Bruce slips something 
into your hand.
"Put these plugs in your ears when I give you
the signal," Bruce whispers.
Technicians inside the pyramid throw the
switches to activate the ray gun. A low whirring
sound fills the air. It rises in pitch as it gets
louder—louder and louder, and higher and
higher. Soon it begins to hurt your ears. Your
arms and legs become numb, and your vision
starts to blur.
""")

# to page 75

pg12 = ("""
"Inspector . . . Inspector Ahmed!" sputters the
clerk.
"What is the trouble here?" asks the inspector.
"My uncle has been kidnapped from the
hotel," you say.
"Is your uncle Professor Hockney?" asks the
inspector.
"How did you know?"
"I have been watching this hotel since he arrived.
I was afraid something like this might happen."
"I think I saw the kidnappers in a truck behind
the hotel," you report anxiously.
You and the inspector run to the back entrance
of the hotel, but the truck is gone.
""")

# to page 44

pg13 = ("""
The strange man is already in a cab when you
reach the stand in front of the terminal. You 
manage to jump into the next cab in line.
"Do you speak English?" you ask.
"I speak much English, meestehr."
"Good, then follow that cab," you tell him.
Your cab weaves in and out of the heavy traffic,
with its horn blaring constantly. Your driver just
barely misses one car after another. However, he
does manage to keep less than a block behind the
other car.
The fast-moving traffic slows to a snail's pace
once you get into an older section of the city. The
cab you are following stops, and the strange man
gets out. You hand your driver a couple of American
bills, hoping they cover your fare. Fortunately, the
driver seems more than pleased as you leave the cab.
You can barely see through the thick crowd,
but you do catch a glimpse of the man you are
following. He is entering what looks like a cafe.
You push your way over to the entrance.
""")

# to page 37

pg14 = ("""
You tell Ahmed that you would rather go back
to the hotel, try to find Andrea, and get her
opinion before you do anything.
You return to the hotel in a cab and check
Andrea's room. No sign of her. You leave the
hotel not quite knowing what to do.
At the corner a native woman, with a dark veil
covering her head and face, except for the eyes,
beckons from a doorway. You are surprised to
see that her eyes are pale gray. You are even
more surprised when you hear her voice. The
woman is Andrea in disguise!
"Follow me quickly," she says.
You have to run to keep up with her. She leads
you through a labyrinth of teeming alleyways.
Finally you reach a stone building with a heavy,
carved door.
""")

# to page 106

pg16 = ("""
There may be dangers involved, but you can't
let your uncle down. You tell the inspector you
will go with him on the raid.
"We will leave at dawn tomorrow," says
Ahmed. "It is not advisable for you to go back to
your hotel. My personal bodyguard will escort
you today, and tonight he will bring you to my
home, where you will spend the night. Perhaps
you would like to tour the Pyramids today."
"It might keep my mind off Bruce until tomorrow," you say.
"Then let's step outside," Ahmed says.
As you do, a long, black Mercedes limousine
pulls up.
"This car is bulletproof, among other things,"
says Ahmed. "You will find it quite comfortable—
and safe."
""")

# to page 8

pg17 = ("""
You slide down the drainpipe to the balcony
below, and then begin to lower yourself to the
street. You try not to look down. Carefully you
reach around with your foot for whatever footholds 
you can find sticking out from the building.
It is easier than you had expected.
Finally you make it down to the street. You can
still see the truck. It's only a block away, stuck in
traffic. You push your way through the crowded
street as fast as you can to catch up to it
Out of breath, you reach the back of the truck.
You jump on and struggle with the doors. They
fly open suddenly, and you fall back onto the
street, banging your knee. Hopping painfully on
one leg, you get up and pull yourself into the
truck.
""")

# to page 53

pg18 = ("""
A screen slowly appears in one of the walls,
and what looks like a movie about ancient Egypt
begins. You see a pyramid being built. Workers
scurry about with ropes and long poles. But they
do not carry the huge blocks of stone. The stones
float through the air by themselves!
A few of the workers
carry devices which project a
beam of light onto the blocks
and cause them to rise in the air. Other workers
toss ropes over the enormous floating blocks and
lead them along, while the workers with the poles
push the blocks gently into place. Amazing!
""")

# to page 50

pg20 = ("""
Another guard appears at the door of the
room.
"Ahmed won't be coming back," he says. "All
of us left at the villa are members of the Assassins.
We have infiltrated Ahmed's organization."
Two other members of the Assassins enter the
room, guns drawn. They lead you down to a
dungeon in the basement of the villa and chain
you to an iron ring set in the stone wall.
You realize that you're going to be a "guest" of
the Assassins for a very long time.
__________________________________________________
The  End
""")

pg21 = ("""
"That looks as if it might be a kind of monorail," 
says Bruce. "See, that big plastic bubble
travels on the rail out through a circular tunnel on
the far side. I've suspected for a long rime that
something like this might exist It confirms a theory 
of mine that ancient Egyptian culture was
given a big boost by a more advanced one."
The door of the bubble is open, and Bruce
jumps inside. His hand sweeps over the complex
control panel.
"I think I see how this thing works," says Bruce.
"Let's give it a try. Of course, we don't know what
dangers lie ahead. This time," Bruce says to you,
"you definitely should stay behind to go for
help—just in case we don't get back."
__________________________________________________
If you insist on going along, turn to page 97.
If you stay behind,  turn to page 49.
""")

pg23 = ("""
It is suddenly very quiet in the next room.
"Bruce, are you all right?" you call through the
door. There is no answer. You throw open the
door. Bruce is gone!
The room is a mess. Sheets trail across the floor
as if a struggle had taken place. In several places
there are drops of blood. The screen covering the
window has been pushed in. There are more
spots of blood on the windowsill and on the small
ledge outside. You look down. There is a four story 
drop to the street.
You rush back into your room and throw on
some clothes. Then back to the window. It is a bit
lighter now. Dawn is just breaking. On the street
you see two men, loading a large basket into the
back of an old panel truck. From this height—and
in the still-dim light—you can't be sure, but 
something tells you that one of them is the stranger
who gave you the note. You also have a strong
suspicion that your uncle is in the basket. How
did they get him down to the street?
The ledge outside the window extends only a
short distance on either side. There are no other
windows nearby. But there are several small balconies
on the second and third floors. There is
also a drainpipe on one side of the ledge. Maybe
you could slide down the drainpipe to the nearest
balcony and then climb down to the street.
You're in a panic. What should you do?
__________________________________________________
If you decide to risk climbing down the side of
the building, turn to page 17.
If you decide to get the police,  turn to page 59.
""")

pg24 = ("""
One by one you, Bruce, and Hassan slide
down the rope into the chamber below. It is a
large room. In the center are huge chunks of rock
and other debris that must have fallen from the
ceiling. At one end of the room is a door leading
toanother chamber.
As you approach the door it opens automatically. This startles all of you for a moment. Carefully you peer inside. You are hardly prepared for
what you see.
The room is illuminated with some kind of
strange light. The walls and ceiling are made of a
plastic material with a honeycomb pattern, and
they seem to glow with an inner luminescence. In
the center, perched on a glistening metal rail, is
some kind of futuristic device.
""")

# to page 21

pg26 = ("""
It is very late when you get back to the hotel.
You are weary from the plane trip and the experiences of the day. You fall asleep instantly. Bruce is
in the adjoining room.
At dawn, something startles you awake. You
hear sounds of a struggle in Bruce's room. Quick
as a cat, you spring out of bed and run to the
door.
""")

# to page 23

pg27 = ("""
The throne room is a large circular hall surrounded by ornate columns, decorated in the
style of ancient Egypt.
"Ah, my friends. Sit over here by the fountain,"
says a short man wearing a large turban overloaded with jewels and multicolored feathers.
"I'm so glad that you accepted my invitation to
visit. I see that you two appear to have bumped
your heads together. Most unfortunate. I'll see to
it that my infirmary looks after your injuries."
""")

# to page 68

pg28 = ("""
"If it will help me rescue Bruce, I'll join," you
say.
"Then step into the triangle on the ground in
front of you," says the speaker.
You look down. Strange—the triangle has the
same design as the coin you tossed down the
shaft, only much larger. As you step forward, a
strong energy floods through you, and an intense
light surrounds your body. You close your eyes
but the light's brightness does not diminish.
Suddenly you are caught up in a whirlwind and
shot straight up through the pyramid. You look
down and see the pyramid receding below you.
The top of the pyramid has become a huge,
glistening eye, shooting rays of light in all directions.
Below it are bands of glowing color. As you
concentrate on the eye, your body seems to dissolve.
You become the eye—all-seeing, all-knowing. Your mind
expands to encompass the universe, to fill 
infinite space. All the mysteries of
existence are now understandable.
Your mind and body return to earth. Suddenly
you know where Bruce is being held. With your
new powers you contact him telepathically. Later
the police are amazed when you are able to lead
them directly to the hideout of the Assassins—
where Bruce has been imprisoned—in one of the
old quarters of Cairo.
From now on, you will find a whole new life of
joy and dangers.
__________________________________________________
The  End
""")

pg29 = """
Quickly you wrap the pillow around the snake,
dash to the closet, hurl the snake and pillow
inside, and slam the closet door shut.
You stand for a full minute with your back
against the door. Your heart is still pounding. You
feel weak in the knees as you realize what you've
just done.
You wake your uncle and tell him about the
snake.
"First that warning note—and now this attack!"
exclaims Bruce. "It seems that someone is out to
stop our little expedition by any means."
"But why?" you ask.
"I may be closer than I thought to unlocking
the secret of unlimited energy. At least someone
out there seems to think so. We'd better get you
back to the States before something worse happens."
__________________________________________________
If  you agree to go home,  turn to page 89.
If you plead with Bruce to let you stay, turn to page 7.
"""

pg30 = """
"Let's get to the car."
"There's an exit to our right that doesn't seem
to be covered," says Mohammed. "I will count to
five. Then we will get up from the table and move
as quickly as we can out that door. Don't run
unless they start shooting, then keep low. Ready?
One, two, three, four, five."
Your feet feel like lead, and even though you
know you are moving as fast as you can, it feels
like slow motion. Somehow you make it through
the exit and into the car. You look back to see
armed figures running in your direction. The car
roars away from the curb. WHAM! Something
smacks the car with terrific force.
"""

# to page 5

pg31 = """
"I must compliment you on your escape," says
Ahmed, when you arrive. "It was your coolheadedness that saved you."
"It was really Mohammed's quick thinking that
did it," you reply.
"Now that you see what kind of dangers we
face," says Ahmed, "I will understand if you
change your mind about joining the raid tomorrow."
__________________________________________________
If you still want to go on the raid,
turn to page 80.
If you've had enough of this terrorist business,
and prefer to wait at the villa, turn to page 78.
"""

pg32 = """
Your threat of going to another hotel seems to
do the trick. The clerk sighs and mutters something about tourists. Nevertheless, he directs the
porter to carry your bag to a new room.
"What is this all about?" asks Andrea.
"I'm not sure myself, but a man at the airport
handed me a warning note. If we are in danger,
changing our room may throw our pursuer off, or
at least show him we are on our guard."
"Well, I think this is a lot of nonsense," Andrea
says.
Your new "suite" consists of two small rooms
with a connecting door. The first room is windowless; the second has a small window covered by a
screen of very elaborate grillwork. Andrea's room
is on the other side of the hotel, not far from your
original room.
Bruce arrives a short time later. You tell him
about the warning note and explain why you've
changed rooms.
"Splendid!" he exclaims. "You must always
follow your hunches, especially when danger is
involved. Now I suggest that we go out on the
town for the evening. You don't want to miss the
Sahara Club and its famous belly dancers."
"""

# to page 26

pg33 = """
"I think we had better go down to my office,"
says Ahmed. "I want you to look through my
photo file."
The inspector's office at headquarters is cluttered but organized in its own way. A row of file
cabinets lines one side of the room. Ahmed pulls
out a folder, opens it on one of the few bare
sections of his long desk, and spreads out a collection of photographs for you to study.
Somehow you are not surprised to see the man
from the plane in one of the photos. You tell
Ahmed the whole story.
"The man you recognize is a member of the
Assassins," says Ahmed. "This just confirms what
I told you before. Through informers, I have discovered the secret desert headquarters of the Assassins. There is a strike force of paratroopers and
a dozen helicopters waiting to attack. We must act
as soon as possible."
"If you are going to raid the hideout of the
kidnappers," you say, "I think I should go along."
"It is true that Professor Hockney is your uncle," says Ahmed. "However, this mission may
prove to be very dangerous. I advise you not to
go, but of course the decision is yours."
__________________________________________________
If you decide to go along on the raid,
turn to page 16.
If you decide that it is too dangerous,turn to page 14.
"""

pg34 = """
"Anything would be better than this lecture,"
you say. "Those other passageways sound exciting."
You follow Mohammed into a narrow tunnel.
At one point he stops and feels along the wall.
One of the stones in the wall slides back, and a
small, very low door opens.
"Quickly," says Mohammed, "we must get inside before anyone comes." Mohammed enters
the long, horizontal shaft. The passageway is so
low that you have to crawl on your hands and
knees. You hear a click as the stone door behind
you slides back into place. You hope Mohammed
knows where he is going!
You and Mohammed crawl for quite a while.
Finally you come to a large square chamber. The
walls are white with blue and gold hieroglyphs
painted in neat rows around the room. In the
exact center of the floor is a round hole.
"That is what we call the Well of the Ancients,"
says Mohammed.
"You mean that you can draw water from
down there?"
"There are many things other than water that
can be drawn from a well—wisdom, perhaps,"
replies Mohammed. "This well is very deep.
Here—drop this in the well and see if you can
hear when it hits bottom."
"""

# to page 35

pg35 = """
Mohammed hands you a small coin. It is triangular with an elaborate design in the center. A
tiny, just barely visible hieroglyphic inscription
runs around the edge. The coin shines as if made
of gold.
You throw the coin in and put your ear close to
the well. For a full minute you hear nothing. Then
you hear a strange humming—a high musical
note that vibrates both in the well and inside your
head. You turn to look at Mohammed, but he
seems to have disappeared.
Suddenly you feel as if you are losing your
balance. You are falling into the well.
"""

# to page 65

pg36 = """
Maybe jet lag and your imagination are getting
the best of you.
"Never mind," you tell the desk clerk.
You go back up to the room and unpack your
small suitcase. You make a careful search. There
is no sign that an intruder has been there, and
you feel relieved. Your room turns out to be a
suite, with a bedroom, a sitting room, a small
bathroom, and two tiny closets. The bedroom
windows are covered with elaborately patterned
grillwork. Andrea's room is on the same floor,
down the hall.
Bruce finally arrives and you show him the
note. For a moment he looks alarmed. Then he
smiles. "Well, I suggest we forget about it for the
moment and go out on the town," he says. "I
know this great spot called the Sahara Club
where we can get a delicious meal of shish kebab—and even watch some genuine Egyptian
belly dancing."
When you arrive back at the hotel later, you are
very tired. Andrea goes to her room, Bruce retires
to the bedroom, and you quickly fall asleep on
the couch in the sitting room.
"""

# to page 42

pg37 = """
The rhythmic beat of Middle Eastern music hits
your ears as you go inside. There is a heavy smell
of incense. A belly dancer sways in the center of
the dance floor. You find a table off in a dim
corner. You can't see the man you followed, but
your eyes are still adjusting to the darkness.
"""

# to page 96

pg38 = """
"We've got to go down there now. My uncle
may be in grave danger."
You and Ahmed start down the side of the
dune toward the pyramids.
Suddenly a troop of desert warriors on camels
appears from nowhere and comes charging
toward you. Dark headcloths cover their faces
except for their eyes. But instead of the old, long
rifles you have seen them carrying in pictures,
they all have modern submachine guns—and
they are all pointed at you.
One of the warriors commands you to raise
your hands and march toward the pyramids.
A door opens in the base of one of the smaller
pyramids, and you and Ahmed are forced into
the vault inside. The door snaps shut behind you.
You realize that the "floor" you're standing on is a
conveyor belt that is rapidly carrying you toward
a wall of flame at the other end of the vault. You
try frantically to run back to the door, but the belt
is too fast. You are both swept into the thermal
chamber—a chamber that so concentrates the
energy of the sun that any object entering it is
instantly vaporized.
__________________________________________________
The  End
"""

pg39 = """
As you start to leave the platform, the approaching figure greets you.
"My name is Imhotep. I greet you from the
past"
"For a while there I thought we were in the
past," you say.
"No, I am not actually here at the moment, and
you are not back in ancient Egypt. This is a
recording—a three-dimensional hologram. My
image is programmed to respond to individual
personalities such as yours. Even though you
may feel my arm as solid—here, I will touch your
hand—it is only an illusion. It is too complex to
explain, but your descendants will understand
someday, just as you know that when you listen
to a radio there are not little people in the box
making the sounds."
"You are the most celebrated character in
Egyptian history," says Hassan. "You were—or
are—the greatest genius that ever lived."
"It is true that I gave your species a bit of help. I
taught them the rudiments of architecture, farming, mathematics, engineering, and medicine.
That was five thousand years ago. But I am not
sure I was wise to do it. I will have to decide that
when I find time to return. Your planet is in my
study quadrant, but it is far out on the edge of the
galaxy."
As he speaks, the image of Imhotep seems to
blur a bit.
"""

# to page 56

pg40 = """
You, Bruce, and Hassan climb down a ladder
into the deep pit. At the bottom, a six-foot-square
opening penetrates the side wall. A perfectly
straight tunnel of the same dimensions goes into
the rock—horizontal for a short way, then sloping
sharply downward. The three of you enter it.
A hand rope along the wall keeps you from
slipping. Your flashlight beams cut into the darkness ahead. Finally you come to a circular room
about twelve feet in diameter, directly beneath
the center of the pyramid.
"This is strange, very strange," says Hassan.
"Yesterday this floor was completely smooth, almost polished. Now there is a pattern of cracks
over here and part of the floor has sunk."
Suddenly there is a cracking noise.
"Get back to the tunnel!" shouts Bruce. "The
floor is caving in."
"""

# to page 70

pg42 = """
Toward early morning some inner instinct halfawakens you. You hear a faint rustling and the
sound of a door softly clicking shut. You snap on
the small table lamp. Only inches away from your
face is an asp, one of the deadliest snakes in the
world.
You've got seconds before it strikes.
__________________________________________________
If you grab your pillow and try to clamp it
down on the snake,  turn to page 29.
If you back off slowly and call your uncle for
help, turn to page 88.
"""

pg44 = """
"I shouldn't have waited," you say, downcast.
"I should have climbed down the wall of the hotel
and tried to stop them before they got away."
"No," says the inspector, "you did the right
thing. These men are fanatics. They probably
would have shot you down."
"You know the men who did this?"
"They are members of an ancient terrorist
group known as the Society of Assassins. They
know that your uncle is working on a way to
produce enormous amounts of energy. They
would like to steal this secret and use it for their
own evil plans."
"Did Bruce know they were after him?"
"He did, but he is always exposing himself to
danger. A most peculiar man, your uncle, if you
will pardon my saying so."
"Some people might feel that way," you say.
"In any event," says the inspector, "he is a
brave man, too, and I have failed to protect him. I
feel responsible for your uncle's disappearance. I
will do everything in my power to find him."
"First," you say, "I think we should go upstairs
and wake up Bruce's assistant, Andrea."
The two of you go to Andrea's room. Inspector
Ahmed knocks on the door. No answer. The door
is unlocked. You and Ahmed go in. No Andrea!
"""

# to page 33

pg45 = """
You feel that you would like to get your feet on
the ground, at least.
Ahmed flies low over the sand, looking for a
stone outcropping that might give you protection
from the storm. Below you the sand is being
driven across the desert in little whirlwinds.
Ahmed shouts your approximate position into
the radio, though it's doubtful anyone can hear
over the noise of the storm. He grabs a piece of
canvas from the back of the cockpit just as the
two of you jump from the helicopter. Seconds
later a powerful gust picks the helicopter up and
sends it tumbling along the ground like a fragile
toy.
"""

# to page 46

pg46 = """
You dive to protect your face from the pebbles
and sharp rock hurled through the air by the
wind. You are temporarily blinded. Your lungs fill
with choking dust.
"Up against this ridge," shouts Ahmed. "We
must imitate camels in a storm. Kneel, head to
the ground, away from the wind.
"Here," he shouts. "Help spread this cover
over us. This sand will wear away our clothing in
no time. Then it will start on our flesh."
The sun must be up, but it is now pitch dark.
The roaring of the wind is still so loud that Ahmed
must yell directly into your ear for you to hear
what he is saying.
"We must shift our weight every few minutes to
knock the sand off our backs—otherwise we'll be
buried alive," he cries.
You are now choking almost to suffocation.
Your arms and legs have lost their feeling.
"""

# to page 85

pg49 = """
Your uncle and Hassan go off in the strange
bubblecraft. Now that they are gone, you wish
you had insisted on going with them. It is lonely
waiting by yourself.
As you wait, you begin to hear some kind of
humming. At first the sound is very low. Then it
gets louder and louder. It seems to come from a
specific spot on the wall. You walk toward it.
"""

# to page 10

pg50 = """
"This looks like some kind of science-fiction
movie," you say.
"I don't think it's science fiction," says Bruce. "I
think we're seeing the real thing."
"Don't be ridiculous," says Hassan. "Every archaeologist
knows that it took thousands of workers scores of
years to build the Pyramids."
Bruce shakes his head. "Those blocks weigh
two to three tons each. They were fitted together
so carefully that not even the thinnest piece of
paper can be slipped into the joints. Does anyone
really know how they got those blocks there?"
The picture blurs. A kind of fog drifts over the
screen and then clears away. The pyramid is completed.
But what a pyramid! It appears to be early
morning. The top third of the pyramid is sheathed
in gold, polished to a mirror finish. The rest of the
pyramid is painted in iridescent colors in horizontal
stripes clear to the bottom.
The early sunlight strikes the top of the pyramid
and throws a blinding shaft of light straight up
into the sky.
You are so fascinated by this scene that it takes
you several minutes to realize that the triangular
viewscreen is gradually growing larger.
As you watch, the entire wall of the room becomes 
a viewscreen, and the other three walls
vanish completely. The glowing floor remains, but
you seem to be standing in ancient Egypt!
"""

# to page 51

pg51 = """
A figure who appears to be a priest or high
official seems to notice you from afar. He comes
closer and beckons to the three of you.
"If we leave this platform, do you think we can
get back?" you ask Bruce.
"I have no idea how the mechanism operates,"
Bruce replies. "I'm not even sure we're any safer
if we stay where we are."
__________________________________________________
If you decide to stay where you are,
turn to page 76.
If you decide to leave the platform,
turn to page 39.
"""

pg53 = """
The truck jerks to a stop. The kidnappers must
have heard the door open. They reach the back
of the truck just as you are trying to open the
basket. One of the men is a hulking brute; the
other man is the one you saw on the plane and in
the airport. They have you boxed in. No use
calling for help. No one could hear you over the
noise outside.
"""

# to page 60

pg54 = """
Mohammed disappears in the direction of the
phone. You sit, waiting—and wishing he would
come back. One by one, the people at nearby
tables finish their drinks and leave. You suddenly
realize that you are alone in the cafe.
Then you become aware that there are
shadowy figures, each with a submachine gun,
standing behind the large pillars around the cafe.
The guns open up at you all at once.
__________________________________________________
The  End
"""

pg55 = """
There in the distance, before your eyes, a pyramid emerges out of the sand like the bow of an
enormous submarine. Smaller pyramids rise to
encircle it, their surfaces flashing in the sun with
the brilliance of polished gold. Bolts of artificial
lightning jump from the top of the large pyramid
to the tops of the smaller ones, causing booming
sounds to reverberate across the desert.
"This is incredible!" exclaims Ahmed. "I've
never seen anything like it. I've heard stories of
strange devices that can concentrate the sun's
energy to almost unimaginable levels. I'm not
sure, but I think that is what we are looking at."
"I'm sure this is what my uncle was experimenting with," you cry. "We've got to investigate.
Bruce may be a captive down there."
"I don't like the looks of this at all," says
Ahmed. "I think it would be better for us to slip
away and try to get help."
__________________________________________________
If you convince Ahmed that it is important to
investigate now, turn to page 38.
If you let Ahmed convince you to slip away,
turn to page 58.
"""

pg56 = """
"I apologize for the brevity of our meeting,"
continues Imhotep. "I hope your civilization prospers. Someday you or your descendants wil!
come across the vastness of space to visit me. You
will be welcome. For now, farewell."
The image begins to fade and you find yourselves back inside the pyramid room. The outside
door reopens, and the three of you return the
way you came.
"I think we should keep this discovery a secret
among the three of us," says Bruce.
"I quite agree," Hassan says. "The world is not
yet ready for this knowledge."
You agree too.
The next day you watch as workmen fill in the
tunnel. When you leave the site, you go past the
Sphinx. Perhaps you only imagine that it says:
"You will be welcome someday."
__________________________________________________
The  End
"""

pg58 = """
"I think you are right," you say. "We might be
walking into a trap."
You and Ahmed slip carefully down the tall
dune.
"Let us head south for a few hours and then go
west again," says Ahmed.
You both take the last sips of water from the
canteen.
"We can last another four hours without water," adds Ahmed. "After that, dehydration will
finish us."
After several hours of trudging across the sand,
you barely have enough strength to keep moving.
Your throat is so dry that you can't swallow.
Bright spots dance before your eyes—a sign that
you are dying of thirst.
"""

# to page 99

pg59 = """
Climbing down the side of the building is too
risky, you think. One slip, and . . . ! You wouldn't
be much help to your uncle then.
You run down to the lobby and quickly explain
the situation to the desk clerk.
"I told you that you should have kept the room
you were assigned," says the clerk smugly. "But if
you are in need of emergency assistance, I will do
what I can."
He picks up the hotel phone and clicks for the
operator. At that moment a policeman enters
the hotel lobby. The surprised clerk hangs up the
phone and looks at him openmouthed.
"""

# to page 12

pg60 = """
You must save yourself and Bruce. Your instinct takes over as you reach for a short length of
pipe on the floor of the truck and lunge at the
larger of the two men. You hit his hand with the
pipe. He backs off, howling with pain, and you
jump out of the truck. But where is the other
man? Wham! He gets you from behind.
You wake up bound hand and foot in a small
compartment. You can tell you're aboard an airplane from the sound and the vibrations.
Your uncle is tied up next to you. He has a
wide, bloodstained bandage around his head.
"Where are we?" you ask. "And who are these
people?"
"I'm not positive. But my suspicion is that
we've been kidnapped by the infamous Dr.
Ptah."
"""

# to page 69

pg62 = """
"I  got a note from a  man at the airport that said
the  same thing!"  you tell Hassan.  "I  showed it to
Bruce  yesterday."
"Is this true?"  Hassan asks Bruce.
"I'm afraid it is,"  Bruce answers.  "However, the
Sphinx is  mute  enough  at the  moment.  As  soon
as  the  instruments  are  installed  underground,  we
can  start  our  experiments."
"The electrical lines have not yet been strung in
the tunnel,"  says Hassan,  "but  I  have a flashlight
for each  of us,  and  also a  strong rope  in  case  we
need  it.  Now we  are  ready  to  descend."
“””

# to page 40

pg63 = “””
When  you  are  finished  dressing,  the  niche
widens  to  become  a  door.  You  step  into  a  large
chamber.  You  find that the  humming comes from
a  chorus  gathered  around  a  large  stone  sar-
cophagus.  Inside this is a  coffin in the shape of a
person. The lid floats a  few feet in the air.  On one
end of the lid is a lifelike sculpture in gold.  With a
shock you  recognize  it.  It is  your  own  face.
“””

# to page 66

pg 65 = “””
Did  Mohammed  push  you  into  the  well?  Did
you  really  slip  and  fall?  You  can't  tell.  You  grit
your  teeth  and  wonder  how  far  you  will  fall  be-
fore  you  hit bottom.  You  can  still  hear the  hum-
ming.  It  grows  louder.  You should be  terrified—
falling down a bottomless shaft in the center of an
ancient  pyramid,  maybe  to  your  death.  But  you
are  strangely  calm.  The  musical  note  seems  to
have  something  to  do  with  it.  And  your  rate  of
falling  has  slowed.  A strong  blast  of air  from  be-
low  is  cushioning  your  fall.
Suddenly  you  land—on  your  feet.  You  look
around you, amazed.  You are on a small platform
in  the  center  of  an  amphitheater  of  some  sort.
Around  you  in  a  circle  are  nine  white-robed  fig-
ures  on  large  stone  thrones.  A  central  figure  sit-
ting  on  the  largest  throne  speaks:
"We  have  been  expecting you."
“””

# to page 79

pg66 = “””
Against  your  will  you  walk  up a  short  flight  of
stairs.  Your  mind  struggles  against  it,  but  the
movements  of  your  body  are  no  longer  in  your
control.  You  lie  down  in  the  coffin.  The  horrible
realization  of  what  is  happening  fills  you  with
panic—but  you  are  now  powerless  to  move.
The  lid comes down and covers you.  You hear
the  heavy,  grinding  sound  as the  stone  lid  of the
sarcophagus,  weighing  many  tons,  slides  into
place.
There  is  no way out  now.  You  will  lie there  as
long as the stars rise and set over the desert.  You
have become part  of the  secret  of the  Pyramids.
__________________________________________________
The  End
“””

pg67 = “””
You  are  not  sure  what  is  going  to  happen  to
you in the pyramid, but if Bruce and Andrea want
to  go  in,  you  don't see  how  you  can  refuse.
All three of you  enter. The door closes  behind
you.
"This is a data module," a voice begins.  "I will
respond  telepathically  to  your  brain  waves  and
will  answer  all  of your questions."
"What is the
real
secret of the Pyramids?" you
ask.
"This module is the secret,"  the voice answers.
"It was left here by the galactic traveler Imhotep in
star year four billion  ninety-four.  This module was
connected by hyperspace relay to the main galactic 
computer  located  in  the  Sirius  star  system.
Other pyramids were built to imitate this shape so
that  the  secret  could  be  protected  until  the  right
time."
The door to the module reopens, and the three
of you  step  out  into  the  sunlight.
"This  is  the  greatest  discovery  of  my  life,"
Bruce says  after a  few moments  of silence.  "This
is  even  more  exciting  than  what I  had  hoped  to
find  when  I  came  to  Egypt.  It  would  be  catastrophic 
if  this  secret  fell  into  the  wrong  hands.
But  if  we  use  its  information  properly,  we  might
be able to solve all of the problems of the world."
__________________________________________________
The  End
“””

pg68=“””
"I can do without your infirmary,"  says Bruce.
"The  only  thing I  want is a ride out of here."
"All in good time, all in good time.  First, I must
explain  to  you that I am  Ptah,  direct descendant
of  the  pharaohs.  I  am  here  to  complete  their
work.  I  intend  to conquer the  world."
"And just  how  do  you  plan  to pull  off that  little
feat?"  asks Bruce.
"With  your  help,  of course,  Professor.  Several
Russian  scientists  were  on  the  verge  of  complet-
ing a particle-beam  ray gun.  By various means I
have  had  them  brought  here.  They  have  almost
completed their work.  And now,  with you to help
them, they will be done in no time at all.  When it
is finished, the ray will be directed at a mirror on a
space  platform that I have already placed in orbit
around  the  earth.  I  will  then  be  able  to  bounce
the  ray  back  to  any  point  on  earth,  utterly  de-
stroying the targets that I choose.  If you refuse to
help  me,  you  will  be  imprisoned  on  the  space
platform.  I  give you exactly one hour to make up
your  mind."
The  guards  take  you  and  Bruce  to  a  small
room  with  barred  windows and  lock  you  in.
__________________________________________________
If you and Bruce pretend to go along with Ptah
in order to play for time, turn  to page 11.
If you think that you should try to escape
without delay, turn to page 111.
“””

pg 69 = “””
"Dr.  Ptah!  Who is that'"  you ask.
But Bruce  has  no time to answer.  The plane is
landing.  The  door  of  the  small  compartment
opens.  Three  men  grab  you  and  Bruce  by  the
ankles  and  pull  you  out  of  the  plane,  dumping
you  on  the  ground  like  two  sacks  of potatoes.
You look around.  You're at one end of a long,
narrow,  sandy  island,  bare except  for a  few palm
trees and a large pyramid-shaped building.  Down
the  beach  there  is  a  pier  with  a  motor  launch
moored  to  it.  One  of the  men  cuts the ropes  on
your  feet  and  wrists,  then  does  the  same  for
Bruce.  More  men  appear,  carrying  rifles.
"All right," one of them orders,  "you two march
toward  the  building  over  there."
As  you  walk,  you  realize  just  how  large  the
pyramid  building  is.  Though  clearly  not  a  solid
structure like the ancient pyramids—it has rows of
windows  at  various  heights—it  is  still  twenty  or
thirty stories high. A large mast of some sort  rises
from the top. The mast is bent sideways to a crazy
angle.
An electronically controlled door slides open at
the  base  of  the  pyramid,  and  you  are  pushed
inside.
"Take them to the throne room,"  you hear one
of the  guards  order.
“””

# to page 27

pg70 = “””
The  three  of  you  just  make  it  back  into  the
tunnel  when  an  explosion  rocks the  room  and  a
section  of  the  floor  crashes  into  some  unknown
abyss below. Then there is silence. Clouds of dust
rise  from  the  gaping  hole.  You  wait  for  several
minutes,  hardly  daring  to breathe.
"I think that's all that is going to happen for the
moment,"  says  Hassan.
"Hold  on  to  my  legs,"  says  Bruce.  He  crawls
back into the room and leans over the edge of the
opening,  playing  his  flashlight  down  into  the
space  below.  "Seems to  be  some  kind  of cham-
ber,  probably an ancient tomb.  The floor is about
fifteen  feet  down.  It's  lucky  we  brought  a  rope
along."
"This  is  a  great  discovery!"  exclaims  Hassan.
"We  must  climb down  at once."
"I don't know if we should all go,"  says Bruce,
looking  at  you.  "We  don't  know  what  kind  of a
sticky situation  we  might be getting into.  It  might
be  better  if  you  run  back  and  bring  help  while
Hassan  and  I  climb  down."
__________________________________________________
If you convince Bruce that you should share in
the discovery of the chamber,  turn to page 24.
If you agree to go back for assistance while
they investigate, turn to page 90.
“””

pg72 = “””
"If there are, I've never heard them, or heard of
them,"  Ahmed  replies.
You  pick  out  the  highest  dune  nearby  and
climb  it.  You reach the top and look  down  into a
huge  valley.  The  sand  itself  is  bright,  but  in  the
valley  is  something  even  brighter—so  dazzling
that it blinds you.  Ahmed shields his eyes with his
hands.  "What an  incredible  sight,"  he  gasps.
“””

# to page 55

pg73 = “””
You  decide  you  can  trust  Serena  to  help  you
escape.
She  slides the iron  cot over to the door, wedg-
ing  it  closed.  And  just  in  time!  You  hear  loud,
angry voices on the other side as someone bangs
and  struggles  to  get  in.  You  and  Serena  jump
onto the cot. She cups her hands to give your foot
a boost up.  Her  lift sends you  sailing through the
window.
Flat  rooftops  stretch  in  all  directions,  lit  with a
silvery  light  from  the  moon.  You  turn  to  help
Serena  climb  up,  but she  is  already beside  you.
"Quickly,  to  the  other  end  of  the  roof,"  she
orders.
You  dash  across  the  roof.  "They're  coming
after  us!"  Serena  shouts.  "Jump  across  to  the
other  roof."
You  look across and then  down.  You can't tell
how many  stories  the  drop  is,  but  it  looks  like  a
long way down. The gap seems  terrifyingly wide.
Can  you  make  it  if you jump?
__________________________________________________
If  you decide to jump,  turn to page 103.
If you decide to take a chance with the people
who are after you, turn to page 108.
“””

pg74 = “””
"I've  had  enough  of  being  cooped  up  in  nar-
row  passageways  under  umpteen  tons  of  rock,"
you  say.
"Very well,"  says Mohammed.  "Perhaps I can
take  you  on  a  daytime  tour  of Cairo."
You  agree.  After a  couple  of  hours  of  walking
through  museums,  touring  ancient mosques and
city walls,  and  looking at parks and  monuments,
you  are  very  tired.  Mohammed  finds  a  colorful
cafe  on one  of the broad boulevards in the mod-
ern section of Cairo where you can  sit and watch
the people go by.  You  have been  sitting there  for
awhile  when  you  notice  that  Mohammed  seems
very  uneasy.
"Is  anything wrong?"  you  ask.
"Do  not  move  or  look  around.  Several  men
who  I  believe  are  terrorists  have  surrounded  us.
How  they  found  us,  I  do  not  know.  They  may
have been following us for some time. I can try to
get to a phone,  or we can make a run for it. Since
our chances are about the same either way,  I  will
leave  the  decision  up  to  you."
__________________________________________________
If  you decide to let Mohammed telephone for
help, turn to page 54.
If you decide to make a run for the car,
turn to page 30.
“””

pg75 = “””
"Now!" shouts Bruce. "Put in your earplugs—
fast!"
When you do, everything snaps back to normal. Only you, Bruce, and the Russians have
earplugs. Ptah and his men fall to the ground
holding their heads. Seconds later they lose consciousness.
"Let's get down to the dock where Ptah has his
motor launch," says Bruce. "The guards there will
be unconscious too."
You run down to the boat, jump in, and advance the throttle to full speed. In a few minutes a
titanic explosion rips the island behind you, but
you are already miles away.
"When we get back to Cairo," says Bruce, "my
new Russian friends have agreed to help us
search for an unlimited energy source—something that will benefit all mankind."
__________________________________________________
The  End
“””

pg76 = “””
You stay on the platform and the walls of the
chamber re-form around you. The triangular
screen reappears, and the images change and
flash before you faster and faster. You see more
pyramids being built. Now a different culture
takes hold. You recognize the Romans in their
military helmets. Christian crosses begin to appear. Churches are built, then swept away in a
flash. You recognize the signs of Islam, the
mosques with their minarets. Then you get a brief
glimpse of Napoleon in his characteristic pose,
hand in jacket, before the Pyramids. Then a sign
of modern times: an airplane flies over.
The screen fades for a moment. When the
images continue, you see tall, strange-looking
structures in the distance and flying machines of a
design you don't recognize. The screen blurs
again. The Pyramids are still there, but the tall
structures in the background are gone. The area
behind the Pyramids—to the horizon—has been
transformed into a green, tree-dotted park. Finally the screen goes blank.
Go to the next page.
“””

# to page 77

pg77 = “””
The monorail craft silently takes the three of
you back to the room where you started. A few
minutes later you are making your way toward
the surface.
"Remarkable!" says Hassan. "That viewscreen
took us back to ancient Egypt and then showed
us all of the different periods of Egyptian history
since."
"Those last scenes are what amazed me," says
Bruce. "Those flying machines we saw haven't
even been invented yet, and that beautiful park
replacing the desert around the Pyramids ... "
You are the first to emerge from underground.
What you see makes you gasp. Grass and parkland extend in all directions as far as you can see.
Overhead are those flying machines of the future.
__________________________________________________
The  End
“””

pg78 = “””
"Maybe it is better for everyone concerned if I
wait at your villa," you tell Ahmed.
"All right," he agrees. "I'm certain that you've
worked up a real appetite after your adventure.
We will eat early tonight."
After dinner you toss and turn for hours. It is
difficult for you to sleep, worrying about Bruce.
Finally you do fall asleep. When you wake up, it is
already late in the morning. Ahmed has long
since left to take charge of the raid. You walk
around the villa. It is very large, with marble
floors, wide hallways, and high ceilings. But there
is an ominous silence about the place.
You decide to leave. It might be a good idea to
go back to the hotel and look for Andrea.
When you reach the front door, an armed
guard stops you. You go back down the long
hallway until you find a telephone in one of the
rooms. The phone doesn't work. You suddenly
realize that you are a prisoner!
“””

# to page 20

pg79 = “””
"I'm not sure where I am," you say. "Am I still
inside the pyramid?"
"This chamber is the lowest point of an inverted pyramid, the exact mirror image of the one
above. This is the true magical form discovered
by the ancients. Only the upper, aboveground
half of this form is known to those outside our
order. We are revealing our secret to you because
we hope that you will join us. Your uncle is one of
our initiates. He is now in great danger. If you
become a member of our order, you will be much
better equipped to find him."
"What do I have to do to join?" you ask.
"Psychic energy is collected above and then
concentrated down here. This energy will transform your being—and initiate you into the Order
of Light. However, I must warn you that, if you
accept these powers, you will also be given profound responsibilities. Your life can no longer be
a simple one, but must be dedicated to fighting
the forces of darkness."
__________________________________________________
If you decide that it might help you to find
Bruce if you join, turn to page 28.
If the whole thing sounds too far out to go
along with, turn to page 82.
“””

pg80 = “””
Just before dawn the next morning you and
Ahmed leave in his small scout helicopter.
You fly east across the desert. The faintest light
begins to creep along the edge of the sky. Then a
thin layer of red, like glowing embers, grows
along the horizon.
"I plan to mark the route to the terrorists' camp
by dropping small smoke bombs in the desert at
twenty-mile intervals," Ahmed explains. "The
troop-carrying helicopters will leave from a
nearby army base in half an hour. They will follow the smoke trail."
As the huge, fiery disc of the sun floats majestically up into the sky, Ahmed notices some dark
clouds low on the horizon to the southeast.
Soon strong gusts of wind begin to buffet the
helicopter. Ahmed radios the base.
"Come in, ground control. Abort mission for
the present. Weather conditions unfavorable."
Ahmed begins a wide bank to the north. The
wind is stronger now, and steady. The air is filled
with a strange fog. The helicopter begins
to cough.
"The dust is beginning to clog the air intake of
the engine," says Ahmed. "The air filter can handle normal dust conditions, but we've blundered
into a sandstorm."
"Is there anything that we can do?" you ask as
the wind begins to howl.
“””

# to page 81

pg81 = “””
"We have two choices," hollers Ahmed, trying
to be heard over the sound of the wind. "We can
try to fly through this mess—though I can't believe we'll make it—or we can land and try to find
a place to hide from the storm on the ground, but
that is unlikely in this part of the desert. We are
done for either way. What do you think we
should do?"
__________________________________________________
If you think it is better to keep flying,
turn to page 92.
If you think you should land while you have a
chance, turn to page 45.
“””

pg82 = “””
"I think I'll stay just the way I am," you say. "I'll
find Bruce my own way."
"Very well," says the speaker. "Obviously you
were not meant to be one of the Chosen."
"You're right," you say. "I don't... I don't..."
You can't complete the sentence—you feel
yourself blacking out.
You awaken outside the pyramid. You are lying
on the ground, and Mohammed is putting a
damp cloth on your forehead.
"Ow! My head!" you say as you try to sit up.
"What happened in the pyramid? I don't remember."
"You hit your head on the low doorway of that
last room. You knocked yourself out," says
Mohammed. "Do not be embarrassed. Many do
it in the dim corridors within the pyramid."
Just then your uncle and Andrea rush up with
Ahmed.
“””

# to page 83

Pg83 = “””
"Uncle Bruce!" you exclaim. "Am I glad to see
you. I thought you were a goner when they took
you off in that truck."
"We caught some of the gang members just as
they were trying to smuggle your uncle out of the
city," says Ahmed. "We also have reports that a
severe sandstorm wiped out the terrorists' headquarters
in the desert."
Later, back at the hotel, Bruce tells you some
disappointing news.
"For some reason my instruments under the
pyramid do not seem to be working properly. I
think I'll have to go back to the States and 
redesign them. When I come back here the next
time, do you want to come along again?"
"Now that is going to be hard to decide," you
answer.
__________________________________________________
The End
“””

pg84 = “””
You are anxious to get to the hotel to find
Bruce and Andrea. You feel you cannot go to
Serena's village.
You thank Serena for her help and slip out of
the cart.
Where are you? The pale moon lights up an
eerie landscape. Stretching in every direction are
small buildings, all deserted. You wander up and
down the silent streets until you finally see a
group of people huddled in front of a small fire.
The night is cool, and they gesture for you to join
them. You stay with them until dawn.
With the light of day you realize that you are in
a very large cemetery. Those small buildings must
be tombs! You're not sure of the way out, but you
pick a direction and keep going. Finally you reach
a small store just outside the cemetery. You find a
telephone and call Bruce at the hotel.
"Bruce," you begin, "I'm in this store just outside
of a huge cemetery; where all the tombs are
miniature buildings, and ... "
"I know exactly where that is," says Bruce.
"Just sit tight until I get there. I'm leaving right
away."
In the cab on the way back to the hotel you are
almost relieved when Bruce tells you that he has
to rush back to the States on urgent business and
that you and he are booked on the next flight to
New York.
__________________________________________________
The  End
“””

pg85 = “””
After what seems like hours, the wind begins to
die down and the sky lightens a bit. Somehow
you and Ahmed have survived. You rub the
caked dirt out of your eyes. You massage your
legs to get the circulation back. Ahmed produces
a small canteen from his belt, and you take a sip.
It helps a little. You stand up and look around.
There is no trace of the helicopter. Hills and valleys of glistening sand stretch endlessly in all directions.
"We must decide if we should stay here and
hope that rescue planes find us or if we should
head out across the desert," says Ahmed. "I
couldn't tell whether our last message got
through or not. If it did, I think we should stay
here. If it didn't, I think we should push on. What
do you think we should do?"
__________________________________________________
If you think you should stay where you are,
turn to page 101.
If you want to start out across the desert,
turn to page 93.
“””

pg87 = “””
You wake up to find yourself lying on an iron
cot in a small storeroom. You sit up and try to
move, and find that one ankle is chained to the
bed.
Gradually your eyes become accustomed to
the darkness. There is a small window high above
you on the wall, and through it you can see a
crescent moon shining. You can hear the beat of
the music you heard in the cafe. You sit there in
the half-darkness trying to figure out how to pick
the ancient-looking padlock that secures the
chain on your ankle.
The door to the room opens slightly, throwing
a shaft of light inside. It's bright enough for you to
recognize the dancer from the cafe. Quietly she
closes the door and whispers in your ear.
"My name is Serena. I will help you escape."
She inserts a long, thin bar into the padlock on
your ankle. The lock snaps open.
"Here, quickly!" she says. "Stand on my shoulders and climb out the window. It leads to a
rooftop. I will pull myself up and follow."
You want to go with her, but you have no idea
who this woman is and where she might be leading you. She could be getting you into a worse
situation. You look at the window high up on the
wall and then at the open door in front of you.
__________________________________________________
If you decide to accept Serena's help,
turn to page 73.
If you don't trust her, and try to escape through
the door, turn to page 104.
“””

pg88 = “””
The door to Bruce's room flies open when you
yell.
"Let's get out of here fast—and I mean fast!"
he shouts.
Bruce makes an end run around the snake and
out the door to the hallway, pushing you ahead.
He slams the door shut
BLAM! There is a sharp explosion from Bruce's
room. People in nightclothes come staggering
half-awake out of their rooms.
You meet Andrea in the hallway. She tosses a
long native jacket to you. Quickly you throw it on.
"We'll take the back stairway down to the basement," says Bruce. "I have a special car—built for
my underwater exploration of the Nile—down
there."
When you get there, the three of you jump into
the car, and Bruce starts it up. He heads directly
for the wall! At the last moment an electronically
controlled door opens, and the car shoots into a
pool of water on the other side of the door. The
car sinks until it is completely underwater, and
then it starts forward.
"""

# to page 94

pg89 = """
You  are  relieved  to  be  going  home.
"It's  bad  enough  that  I  am  in  danger,"  says
Bruce.  "If I  have to worry about your safety too,
I'll  never  be  able  to  concentrate  on  my  experi-
ments."
You  hope  that  Bruce  doesn't  think  you  are  a
coward, but when someone starts putting poison-
ous snakes in  your bed,  it's just too  much.
__________________________________________________
The  End
"""

pg90="""
You go back up the shaft,  using the hand rope
to  help  pull  yourself  along.  After a  short  way—it 
seems very soon this time—the  shaft  levels  out.
But  you  walk  on  and  on—and  see  no  exit.  You
stop and go back.  You reach the point where the
shaft goes down,  but now the hand rope is  missing. 
Where are you? In a panic you run back the
other  way.  Your  heart  is  pounding  and  your
palms are sweaty.
Now you edge  carefully forward,  pointing your
flashlight  down  seemingly  endless  passageways.
You reach a fork in the tunnel.  You don't remember a 
fork there before! Your hands and knees are
shaking,  but  you  force  yourself  to  go  on.  More
forks!  You have somehow blundered into a maze
of tunnels.
You stop  for a moment to  think.  How can you
possibly  find your way out? Then you remember
a  rule  to  follow  when  you're  trapped  in  a  maze:
"Every  time  you  reach  a  fork,  turn  right."  Re-
membering  this  calms  your  nerves  somewhat.
Now  maybe you  have  a chance.
Wearily you start to retrace your steps.  You just
hope that the rule works. At best you know that it
will  be a long walk.
__________________________________________________
The  End
"""

pg92 = """
You and Ahmed  fly on,  taking a  last desperate
chance.  Ahmed  is a  good  pilot,  but the  storm  is
too  much  for the  small  helicopter.  The  turbulent
air  outside  is  a  swirling  yellow  haze.  The  motor
begins  to  sputter—the  air  intake  is  completely
clogged.  Then  the  motor  cuts  out  completely.
You  fall  like a  rock and  vanish  forever into the
vast wastes  of the  desert.
__________________________________________________
The  End
"""

pg93 = """
"It is better to do something—anything—rather
than  sit here  and  wait to  die,"  you  say.
Ahmed  scrapes  his  digital  watch  free  of  dirt.
"It's  1:10 P.M. It  is  already  afternoon,"  he  says.
"Our  best  bet  is  to  head  west,  toward  the  sun.
Later we can follow it as it sets. In the morning we
will  head  away  from  the  rising  sun.  If  the  sun
becomes  obscured  by  haze,  we  will  stay  where
we are.  Otherwise we  will run the risk of wandering
around in  circles."
You  start  off.  Up  and  down  sand  dunes,  and
then  up  and  down  again.  Occasionally  you  stop
to  wet  your  lips  from  Ahmed's canteen.
Then  you  see  it  An  oasis  shimmers  in  the
distance—a  glistening pond  surrounded by  palm
trees.
"Look,  look!"  you  say  to  Ahmed.  Ahmed  is
strangely  calm.
"I'm sorry, but that is just a mirage—a trick the
desert plays on the  eyes,  my  friend,"  he  says.
After  another  mile  or  so  of  hiking,  you  realize
that  Ahmed  is  right.  Nothing  is  there.  Sheets  of
water  seem  to  materialize,  then  vanish  after you
have  walked a  few yards.
A  few hours later,  you stop suddenly.  "Ahmed,
am  I  crazy  or  do I  hear thunder in the  distance?
Are there  sound  mirages in the desert?"
"""

# to page 72

pg94 = """
The submersible car journeys up the  river,  just
under the  surface  of the  water.
"Not long ago,"  says  Bruce,  "I discovered the
entrance  to an  underwater tunnel that goes  from
the  Nile  to  the  famous step  pyramid  at Sakkara.
They say Imhotep's tomb is there.  I haven't had a
chance  to explore  this tunnel  until  now."
When  you  reach  Sakkara,  the  car  enters  the
underwater runnel.  Soon you  surface on a  broad
lake  in  an  underground  cavern.  In  the center of
the  lake  is  an  island,  and  in  the  center  of  the
island is a small pyramid about thirty feet high.  It
is  made  of  a  dull,  silvery  metal—perhaps  platinum. 
Bruce  steers  the  car  to  the  edge  of  the
island. The three of you jump ashore. As you do,
a  large  opening appears  in the  side  of the 
pyramid.  A voice comes  from  inside.
"If you wish to know the secret of Imhotep, and
the secret of the Pyramids," says the voice,  "then
all  of you must step inside."
"I guess it's all or nothing,"  says Bruce.
Andrea and Bruce want to go in—which leaves
it up  to you.
__________________________________________________
If you decide to go into the pyramid,
turn  to page 67.
If you feel it might be a trap,
turn  to page 109.
"""

pg96 = """
A  waiter  brings  you  a  long-handled  pot  containing 
thick,  strong  coffee.  He  pours  it  ceremoniously
into  a  small  porcelain  cup.  It  tastes
somewhat bitter, but not too bad. You sip it slowly
as you watch the dancing.  Is it your imagination,
or  does  the  dancer  keep  glancing in  your  direction?
The music grows louder. The lights get brighter.
You  can't  seem  to  focus  your  eyes.  Your  arms
and legs feel  like lead, and you can't move them.
You  feel  dizzy.  You  feel  like you are passing out!
"""

# to page 87

pg97 = """
"OK," says Bruce,  "let's all three give it a shot."
You  feel  a  lot  better  going  along  than  waiting
alone  in  that  spooky  room.
As  soon  as  you  are  on  board,  Bruce  pushes
one of the buttons on the control panel. There is a
whirring sound and  the  door  of the  strange  craft
slides shut with  an  ominous  click.
The  bubble  starts  smoothly  along the  rail  and
into the tunnel.  After a minute or so, it slows to a
stop. The bubble door opens and the three of you
climb  out.  You  find  yourselves  in  a  chamber  almost
identical  to the  one  you just  left.  However,
this  room  seems  to  have  no  exit.  This  does  not
seem  logical to you.  Whoever created  this trans-
portation  system  would  hardly  have  built  it  just
for the  ride.
On  a  hunch,  you  feel  carefully  along the  wall.
Jackpot!  Two triangular panels recess into the wall
and  slide  apart,  revealing  a  large  room  with
slanted  walls.
"Good work,"  says Bruce.
The  three  of  you  enter.  As  you  look  around
you realize that you are in a room shaped like the
inside  of a  pyramid.
Suddenly  the  triangular  door  closes  behind
you and disappears.  You are trapped inside! The
walls—four  perfect  triangles—begin  to  glow
brighter  and  brighter.
"""

# to page 18

pg99 = """
Up ahead you see  another  oasis.  Is  it another
mirage?  You head for it  anyway.  One part of the
desert is  as  good as  any  other when  it comes  to
leaving  your  sun-dried  bones.
You  get  there  first.  "This  is  water!  Actual  water!" 
you  exclaim.  "This is not a  mirage!"
You dunk your entire head in the water.  Noth-
ing  has  ever  felt better  in  your  life.
Later,  when you are both rested,  Ahmed says,
"Some  of  these  palm  trees  are  date  palms  with
fruit  We  will  have  enough  food  and  water until
the next caravan arrives. It is only a matter of time
before  we  are  rescued."
__________________________________________________
The  End
"""

pg100 = """
You repeat Al-Din's spell three times. The room
begins  to  spin  around  you,  then  fades  away  altogether.
You  seem  to  be floating in  a  void.  Are
you  asleep?  Dreaming?  You  find  yourself  flying
high up over the ocean on what could be a magic
carpet.
You  awaken  in  your  living  room  back  home.
The phone is ringing. You answer it. Your uncle is
on  the  phone.
"I'm just in from Egypt," he says. "I have to get
some  new  equipment  to  continue  my  investigations 
of the  Pyramids.  How would you like to go
back  with  me  for  a  few weeks?"
This is really strange. Did you just dream everything 
that  happened,  or  did  that  magician  really
send  you  back  here  to  start  over?
__________________________________________________
If you decide that it was just a dream, and you
would still like to go,  turn to page 2.
If you say no,  knowing what is in store for you,
turn to page 113.
"""

pg101 = """
"I'm sure the radio message got through,"  you
say.
"I think so too,"  says Ahmed.  "The best thing
to  do  is to  wait where  we are."
Ahmed  digs  around  in  the  sand  where  you
crouched  during  the  storm.
"Here  they  are,"  says  Ahmed,  "the  smoke
bombs.  I  was  afraid  that I  had  lost  them.  Each
one  of these  will  send out  smoke  for  an  hour."
Ahmed sets off one of the bombs. A tall column
of smoke  rises  in the  now  still  air.
The  last  one  is  set  off  late  in  the  afternoon.
"This  is  it,"  says  Ahmed.   "If  no  one  sees  this
smoke,  we  may  be  out  of luck."
Just  as  the  smoke  begins  to  disappear,  you
hear the drone of a plane.  It banks and makes a
low pass over you.
"They  see  us!"  you  shout,  jumping  up  and
down  on  the  sand.
The plane,  which  belongs  to  the  Egyptian  Air
Force, lands nearby.  You are saved this time.  You
wonder  how  many  adventures  lie  ahead  before
you get back to the  States.
__________________________________________________
The  End
"""

pg103 = """
You  might  as  well  take  a  chance  and  try  the
jump.  You step back a  few feet, make a short run,
and take a  flying leap to the other roof.  You manage 
to grab the edge with your hands as you slip
down along the side of the building.  You struggle
to  pull  yourself  up.  You  are  about  to  lose  your
grip  when  a  strong  arm  grabs  you  by  the  wrist
and  heaves  you onto  the  roof.  It's  Serena!
"Wow!"  you  exclaim.  "Are all belly dancers as
strong as  you  are?"
"I was trained to  be an acrobat by my  family,"
she  says,  "before  I  was  kidnapped  by  the  evil
gang that  owns  the  cafe."
"Why haven't you tried to escape before?"  you ask.
"I have," she says,  "but it's not that easy.  They
control this quarter of Cairo completely.  Now my
family  has  discovered  where  I  am  and  has  arranged
my  escape—but  you  will  see.  We  must hurry.  
I hear someone  coming."
"""

# to page 110

pg104 = """
You  pull open the door and dash  down  a  corridor 
that leads back into  the  cafe.  You  run  outside. 
Two  men  from  the  cafe  race  after  you,
shouting  in  Arabic.  You  push  your  way  through
the crowds,  trying to  stay  hidden.  Which  way  to
go?  There  is  an  open  door  on  your  right  with  a
small  courtyard  inside.  You  decide  to  chance  it
and  dart  through  the  door,  slamming  it  behind
you.  You  lean  against  the  door,  gasping  for
breath.
A hulk of a man appears. He has a heavy, dark
beard and  piercing  eyes.
"Welcome  to  my  house,"  he  says.  "Have  you
come to buy a  magic  spell or perhaps something
to  ward  off the  evil  eye?"
"I need help," you say.  "Someone is after me."
"In  that case,  you are welcome  in my  humble
house.  You are safe here.  I am Al-Din, the magician. 
My magic  will protect you."
You  follow  Al-Din  up  a  flight  of  stairs  into  a
room  with  a  low  table  surrounded  by  cushions.
He serves you some mint tea and tells you about
the  ancient  magic  he  practices.
"All is illusion," he says. "Here, I will show you.
Close your eyes and repeat this spell three  times:
abah arah arah abah blah ah."
"""

# to page 100

pg106 = """
"Hurry  inside,"  Andrea  says,  "and  close  the
door  behind  you."
The room you enter is dark, and it takes a  few
moments  for  your  eyes  to  adjust  to  the  light.
When  they  do,  you  see  Andrea  in  front  of you
with a revolver in  her hand,  silencer and all.  The
gun  is  pointed  at you.
"Kill! I must kill. ..." she says in a mechanical-
sounding  voice.  Her  eyes  are  glassy,  as  if  she
were  hypnotized.
"Andrea,  what are you  saying?"  you gasp.
"The  secrets  must  be  protected .  .  .  must  be
protected. ..."  she  continues  in  that  same
strange voice.  It sounds almost like a recording.
You  realize  with  a shudder that Andrea's  mind
has  been  taken  over  by some  evil  force.
"Andrea!"  you  shout.  "I  don't know any  secrets. 
I don't even  know what's going on.  Someone has done 
something to you.  You don't know what  you  are  doing."
She  raises the  gun  to  fire.
"Andrea! No!" you cry.
But the 'pffut' of the  silencer ends  it  for  you.
__________________________________________________
The  End
"""

pg108 = """
The gap to the next  roof is just too wide.  You
know  that  you  would  never  make  it  across.  Serena, 
however,  is  already  across  and  has  disappeared.
You turn to  face  your pursuers.  Then  you recognize  them.
"Bruce! Andrea!"  you exclaim.  "It's you.  How
did  you  get  here?"
"The  cab  driver  who  brought  you  here  was
worried," Bruce says.  "He went to the police and
they  called us."
Suddenly  you  realize  that  you've  got  to  stop
Serena  from running away.  The three  of you can
help  her.
"Serena,  come  back!"  you  shout.  "These  are
my  friends."
The  sound  of  your  voice  echoes  across  the
rooftops,  but there  is  no  reply.
You,  Bruce,  and  Andrea  return  to  the  hotel.
Your  parents  are  on  the  overseas  phone.  They
have  begun  to  worry  about  you  and  insist  that
you  return  home.
Back in the States you  find that many of your
friends  do  not  believe  your  story,  especially  the
part  about your  new  friend  the  belly  dancer.
__________________________________________________
The  End
"""

pg109 = """
"You  have  thirty  seconds  left,"  says  the  voice
from  inside the pyramid.  "After that,  you may no
longer  enter."
"I'm not just going to walk into that thing," you
say.  "Not  unless I  know more about it."
"If that's your honest choice," says Bruce,  "Andrea 
and I will respect it. And in that case, I guess
we'll  all  stay out."
"This  module  will  now suspend operations  for
one  galactic  minute—which is  four  hundred and
seventy-five Earth years,"  says the voice.
The door closes.  You can  find no trace  of it on
the  surface  of the  pyramid.
"1  wonder  what  would  have  happened  if  we had gone
inside?"  you ask.
"Well,  we can come back in four hundred and
seventy-five  years  and  find  out,"  says  Bruce.
"Or we can come back now with special equip-
ment,"  says  Andrea,  "and  try  to  pry  its  secrets
loose."
You are  already  looking  forward  to that.
__________________________________________________
The  End
"""

pg110 = """
Serena  leads you  down  a  long  flight  of stairs.
You  follow  her  through  passageways  that  are
so  narrow  you  can  barely  squeeze  through.
Sometimes  you  can  hear  shouting  nearby  and
see  the  flickering  beams  of  flashlights  searching
the  dark  corners  where  you  were  standing  only
seconds before.  Finally,  in a narrow alley, Serena
stops and  listens  for a  few  moments.
"See  that  donkey  cart  over  there,"  she  whis-
pers.  "It is from my village.  I have arranged for it
to meet me here. I will crawl into the bottom of it.
Watch  how  I  do  it,  then  follow."
There  is just  room  enough  for you  to  squeeze
into the  cart.  Serena  arranges the  straw  over the
two  of you  and  then  signals  to  the  driver  with  a
low whistle.
The  cart starts  off.  You  go  through  narrow  al-
leyways,  then  down larger streets.  Gradually the
street noises die away, and you guess that you are
outside  the  city.
"I think we are safely away from our pursuers,"
says Serena.  "If you wish, you may find your way
from here.  If you continue with me to my village,
you  will be  welcome there."
__________________________________________________
If  you decide to get out of the cart, turn  to page 84.
If you decide to continue on to Serena's village, turn to page  114.
"""

pg111 = """
"Even if we seem to be cooperating,"  you say,
"Ptah  will  finish  us  off as  soon  as  we  stop  being
useful  to  him."
"I  think you're  right,"  says  Bruce.  "When  the
guards  come  for  us,  we'll  jump  them.  I  don't
think  they  expect  us  to  fight  back.  It  might  take
them  by  surprise."
"At least we won't be giving up without a strug-
gle,"  you  say.
The guards are taken  by  surprise.  The  fight is
brief and  furious,  but there  are just too  many  of
them.  The  guards  overpower  you  and  drag  you
back to  Ptah.
"Take them to the other end of the  island,"  he
shouts.
"""

# to page 112

pg112 = """
Again  you are  tied  up and  carried  off.  You are
taken  to  the  other  end  of  the  island  where  a
rocket is ready to blast  off to resupply Ptah's orbit-
ing  space  station.  You  and  Bruce  are  dumped
into a  small compartment in the  rocket.
You  are  already  working  your  hands  free  as
you  blast  off.
"The crew is going to be too busy  for awhile to
bother about us," you say.  "If we can break out of
this  compartment  and  get  the  jump  on  them,
maybe  we  can  take  over the  ship.  Then  we  can
put Ptah's  space  station  out of  action  for  good."
You  know that  you'll  need  a  lot  of  luck  to  get
out of this situation—a lot more than you're likely
to  get.
__________________________________________________
The  End
"""

pg113 = """
"I'd really like to go," you say,  "but I have a lot
of work at school, and I already have tickets  for a
play at the end of the month. Thanks for asking—
and  have  a  good trip."
Your  excuses  sound  a  bit thin,  but you've just
gone  through  a  harrowing  experience.  Even  if
you  only  dreamed  it,  you're  not  going  through
that again!
__________________________________________________
The  End
"""

pg114 = """
You don't really know where you are.  It might
be  safer  to  go  all  the  way to  Serena's  village.
You  ride  for another  few  hours.  There  is  utter
silence  except  for  the  clip-clop  of  the  donkey's
hooves and the creak of the wheels.  You  drift  off
to  sleep.  Sometime  later  Serena  shakes  you
gently.
"We are here,  at my village, and with my people."
You crawl out of the cart. Dawn is just breaking.
You are near a field.  In the center you see a large
bonfire. Around the  fire are hundreds of figures in
white turbans and white robes. They are chanting
in  unison—it's  an  eerie  sound.  Then  the  figures
rise and begin to move together around the fire in
a  strange,  slow  dance,  rolling  their  heads  and
chanting, "Allah-Allah-ah-ah."
The  hypnotic  effect of the dancing draws you in,
and you join the circle.
"""

# to page 116

pg116 = """
You stay with Serena's people, one of the many
tribes of Dervishes, for several days while she
manages to get word secretly to Bruce that you
are safe.
At last Bruce and Andrea arrive at the village.
"Thank goodness you're all right," says Bruce.
"Andrea and I followed your trail to the cafe. The
police raided the place and un
covered a nest of
foreign agents code named SPHINX. But by then
you were gone. Later, when we returned to the
hotel, we found Serena's note telling us where
you were.
"Unfortunately, I had to tell your parents that
you were missing. They have been very worried. I
guess you'd better catch a plane home and show
them that you are really all right. I am sorry you
had only one day in Egypt."
Back in the States, whenever you see the
dawn, you think of those white-robed figures
chanting their hymns to the first light of day.
You weren't in Egypt very long, but it was an
adventure you'll never forget.
__________________________________________________
The  End
"""
#Choose Your Own Adventure Ascii Art
#Kaydon Payne
#10/15/19

pagetitle_art = ("""
?????I?II?I?I?II???+++??+==+==+++++++++++++++++++++=+++==========+++++++++++++++
??II?I?IIIII???????+++============++++++++++=====================+++++++++++++++
????????????I???????++++========+++++++=======~=~=~==================+++++++++++
++++???????????????+++++++++++++++++++++=====~~~===~~~==========++++++++++++++++
++?????????????????????+++=====++====+++==========~============+++++++++++++++++
??????????????????????+?++++=========+=============~============+=++=+++++++++++
++++???????????????++++++======================~==~===~~===============+=++=+++=
+??????????????????+++++=========================~=~======================++++++
++????????????????+++++++==========+=+++==========::~~=~=================+++++++
++++++???++++++==+?++++++++=+===========+++======~=======~=========+=+++++++++++
++++++++++++++++=+++++++++++++++===++==+=====================$?+=========+=+===+
++++++++????+++++++++++++++++++++++++=====================~$Z$Z~~========++++++=
++++++++++++++++++++++++++++++++++++++++=+++++============7$$$$7::======++++++++
??????++++++++++++==++====+++++++++++++=+++++++++++=====7$78Z77OI:=:===+++=+++++
?????????????++++++++++===+==++==========~~============7$Z8ZOZ7Z$?~~+========+=+
???????????+?+++++++++++++++=++++=+=================+IZ7$$$ZZO$7$$,=:~~=====+===
????????????++++++++++++====+++++++++=++++===+=====+$7O?MMD8DZDOD8Z=I=?~====++++
???????????+?+++++++++++++=++==+++=+==============+NZ8DO8D?88DDD7$$Z+?8I~===+=++
????????????+?+?+++8OZ=+++++++++=++=============+87N8O8O7ZI8DDD8Z788+++++~=====+
?I??????????+??++7O888II?++++++++=++++==+=++====OO78D8$Z888OO$$ZZDZOZ++=?+=+==++
II?I????????????OZZOO8O?+?+++++++++++++=++++=+ZO8ZOZ7OOO8DDD88O8Z8ZZZ$+=++?=++++
IIIIII????????O8888ODOO+?+?I++++++++++++++++?ZZ7+II?$OODOO88$O88$D8ZD88I?=++~=++
IIII????????$8O8888ZZOO8?+?++?++++++++++++=I8OO7ZO$IZIZIOOZNOMONDZOZN8DI?I+?I=?+
IIIIII????IDZ8Z88D888O8OI+=++??++++++++++OZOO$$$I8ODODOZD$?D7Z7$878Z88DO??$+?+??
IIIIII?I?O8O888888888O8OZ????I=+I+++++++ZZ7$OIO?OOO8$Z888D8O8DZOO87NO88DZ7+I?++I
IIIIIIIDZ787ZD8$Z$OZ88ZO8+?+==7~++++++ZO?N8?O8O$M$Z$ZNZ?D$$ZDZOO8$Z8D8DDZO?+==O+
IIIIII878ZOOOZOZOO$ODZZOO8++?+=?+?++?$IIZNDON$$D$7M$Z8NOOOM7IDOZONNZDZ8DZOII?I??
IIIIZO8OO$88ZZODZZOO8$ZZ8O$?+++++++Z$$88O8Z$O$$OO87$$Z$Z8DMOD8Z878ODDZO$MMNI+?I?
IIOOOZ7ZOIOZO$8OOZ$8OO788O8?+?++=?D8INOO$II?$ZOO8ZOOOND78DOZZ8Z$ZNDOI$Z8D88$+7+?
8D$ZZZ8$$Z7IZZ$ZOZOZOZZZOD8I++++ZI8Z8Z87O$Z8ZZO$ZD$$IOZ8ZO7D$$8$Z7M8O88MDZ77?7IZ
$ZZOZZZ8$O8OO88OZZO$$Z7D888$++IO$Z7ZZ$O888O8O8OZ888Z7$88Z8O$8Z88D8ONZDDOIO$7NI7?
ZZOO$$ZDO$Z77IOOZZ$777ZI$$$OZD$88Z$ZZ8$7I$DD8D87887$7$ZI8$78$7D88N$O88D8OZO88$D?
????????IIII?++?===~=======++7?I8O7D8O?O7$$7$ZZO$$7D8OZ8ZD8Z7IZID7$ZOIO8DNZO8O?Z
7777IIIIIIIIIII??????I????++=++++++++??+??????+??+????I?III???I??I??I?7?DO8$88D8
7777I?I7IIIIIIIII????II????????????????+?????????++++++???????++++++++I++?+?+$ZO
??II?????????++?+++++?++?+???++++++++++++++++++++++=++???+++++++++?I??+++??+7N88
I??????+???+??????+?+?+?+++++=++==++++++++++++++?++++++++++====+++++~=+I7777III7
+?+??????IIIIIIIII?II????I????????????????+?++$?I777III???+++?????I???????I??II?
IIIIIIIIII?????I?????????II??+???????????++?++++???III??I??++????????I+II7I?????
I7I??II7I7?III7II+=?77777I??+++????I????III???I7?IIII??II7IIII7???I$+??+??+I???+
+???????7$777I??+++?I?+????+?++?+????I?II??++$?II7?III++?+?+?=+?++????++=+??+II+
7I??+++++?I??I??++??????8+I???I??+??????I7?I???I??++++=~+?+=++++??+??I??+??+??+?
+???II??I??III??+?I+?????I?++???I?7??II7??=?++??I??+==??+???+??++I?=+I?+?+?????+
????????I?I?+I??++I+?++III????+??++?7++++++?+?+?+?+++???+??I??+I?I?I++??+$?==~++
????????I???++?=??$77I?I??I????=+??++I??=+==+++?+=?????+=+??????++?+I++++??+?+=?
""")

pageprologue_art = ("""

++++++++++++++++++++++++++++++++++++++++++++?ZOZN$++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++I88OZOZI+++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++D$=,::?D+++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++=O+ID:$:D+++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++II8+~:~=~Z+++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++==88Z=:~=:?+++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++~77?+=:+===+++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++?~+=DO7+ZZ+$8?+++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++:D8O?.7==.78IZI+++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++$.Z78$?.+M.I+7II?7O=++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++8+7.O8I?~$8.7?777Z7I8++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++ZIIIIOO7?$88$DIZ?III?7D+++++++++++++++++++++
++++++++++++++++++++++++++++++++++7I?I7IN87Z~$O$$7ZI?I8I??Z+++++++++++++++++++++
+++++++++++++++++++++++++++++++++II??IIZ7Z~O~Z8$Z?$???7I?I7+++++++++++++++++++++
++++++++++++++++++++++++++++++++$I???77+Z+=~=88$DZI?III??I$+++++++++++++++++++++
++++++++++++++++++++++++++++++++OIII$Z++?:?~~:++OZI?I7$+?I7+++++++++++++++++++++
+++++++++++++++++++++++++++++++++D8$+??I?I8++=:~:II7OO$II?7+++++++++++++++++++++
+++++++++++++++++++++++++++++++++?+++?I+7?I?Z$N~I?II+IIII?O+++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++I+DI?IO$$D7777IIIII$$+++++++++++++++++++++
+++++++++++++++++++++++++++++++++++?$+++$7?IO$Z$87I88Z$I7$?+++++++++++++++++++++
+++++++++++++++++++++++++++++++++++$++++?I?I$ZZ$8II$$8++=+++++++++++++++++++++++
++++++++++++++++++++++++++++++IOZ7$++++8??I8$OZZZ7??I?7+++++++++++++++++++++++++
++++++++++++++++++++++++++=+O87:~7$I+++ZII?$78Z$$OI?I?O+++++++++++++++++++++++++
++++++++++++++++++++++++ZDD888O=~78$?++8I7DO8OZOZ8I?I?D+++++++++++++++++++++++++
+++++++++++++++++++?+$=++++++7OND8OZ?I+DO$ZZZOZZOZO777?+++++++++++++++++++++++++
+++++++++++++++++++++Z7=?ZOZ$$77OOI=Z$?8ZZO$OOZZZOZO8D++++++++++++++++++++++++++
+++++++++++++++++++=++++++++O$I+++++++=OZZZZ8OZZZOZZ88++++++++++++++++++++++++++
++++++++++++++++++++++++++++ZII++++++?IOZZZZOD8ZZZZZ87++++++++++++++++++++++++++
++++++++++++++++++++++++++++Z?I+++++++8Z$ZZOODZOZZ$ZO?++++++++++++++++++++++++++
++++++++++++++++++++++++++++O+I+++++++8OZZZZODZZ$ZZOD+++++++++++++++++++++++++++
++++++++++++++++++++++++++++O=I+++++++OOZZZOODZZZZZZ8+++++++++++++++++++++++++++
++++++++++++++++++++++++++++O=I+++++++O$ZZZO8DZZO$ZO++++++++++++++++++++++++++++
++++++++++++++++++++++++++++O=I++++++?O7ZOZO88ZZO$Z8=+++++++++++++++++++++++++++
++++++++++++++++++++++++++++O=I+++++++Z$ZZZOD8OZO$Z8++++++++++++++++++++++++++++
++++++++++++++++++++++++++++O=7++++++?OZZZZ8=8ZZO7ZD++++++++++++++++++++++++++++
++++++++++++++++++++++++++++O=7++++++?8ZZZZ878ZZ8$Z7++++++++++++++++++++++++++++
++++++++++++++++++++++++++++O~7++++++?8ZZZZZOOOZZZO+++++++++++++++++++++++++++++
++++++++++++++++++++++++++++O~7+++++++=OO$7ZODZ$OZO+++++++++++++++++++++++++++++
++++++++++++++++++++++++++++O~I++++++++?N8ZZOOZZ$ZD+++++++++++++++++++++++++++++
++++++++++++++++++++++++++++O~I+++++++++=8Z8OOZ$$OO+++++++++++++++++++++++++++++
++++++++++++++++++++++++++++O~I++++++++++++8OOZZ$O$+++++++++++++++++++++++++++++
++++++++++++++++++++++++++++O~I+++++++++++?+7OZOZOON++++++++++++++++++++++++++++
++++++++++++++++++++++++++++O~I+++++++++++++?OZ8ZO8ZDI++++++++++++++++++++++++++
++++++++++++++++++++++++++++O~I+++++++++++++?OZ8ZOZ+I??????+++++++++++++++++++++
++++++++++++++++++++++++++++O~I+++++++++++++IOZ8Z88DNIIII????+++++++++++++++++++
++++++++++++++++++++++++++++O~I+++++++++++++7OZ$OD$?D7II????++++++++++++++++++++
++++++++++++++++++++++++++++O~I+++++++++++??+$DON$ZD7II???++++++++++++++++++++++
++++++++++++++++++++++++++++Z=I??IIIII??+++++D$ZO$7I????++++++++++++++++++++++++
+++++++++++++++++++++++++7O$Z=Z$O$7II??++++++O?I7ZII???+++++++++++++++++++++++++
++++++++++++++++++++++++?7ZI??77$7????+++++++?NDNII?++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")

page1_art = ("""

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::,:::::::~:,::::::::::::::::::::::::::::::::::,,:::::
:::::::::::::::::::::::::::::::::~~=??+~~:::::::::::::::::::::::::::::::::,:::::
::::::::::::::::::::::::::::::=~~+?=??~~=~+=::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::~=7$777I+++?+??+~~~=,::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::~~:IO7$D$$OZOI=??++=?I:~:::::::::::::::::::::::::::::
::::::::::::::::::::::::::~IIZOZ$Z8Z88D877=+7777$I::::::::::::::::::::::::::::::
::::::::::::::::::::::::=77ZZ88$7I?+?IZ8877?+7$???:+::::::::::::::::::::::::::::
:::::::::::::::::::::::~I?O$ODZI=~::::~+7O8+7+7$Z+~==:~~::::::::::::::::::::::::
:::::::::::::::::::::~:=7+7Z8O?+=~:::::~+77=I?I?I$$~+?=~::::::::::::::::::::::::
:::::::::::::::::::::~~7ZI$$NI?+=~:::::~=?I7?=+?I7Z7+:=~::::::::::::::::::::::::
::::::::::::::::::::~~~+??ZZN$+==~~~~~~==II7$777Z?~7?+:~::::::::::::::::::::::::
:::::::::::::::::::::=:I+7O+?I7O88ZI+IZ888$$ZZ7$7$Z?==~:::::::::::::::::::::::::
::::::::::::::::::::~7+??I+:~I~+?+=?:=~I?==IO8$7I7ZI+=~~::::::::::::::::::::::::
:::::::::::::::::::~:~+=I=::~I=:,,~=:=~:,:~I8O7I$7?I++=:::::::::::::::::::::::::
:::::,:::::::::::::::=7?~~:+77I?=?+~:==I==+7D777=+~~I+~:::::::::::::::::::::::::
:::::::,::::::::::::~$I:~7I$7D7I7??ZZI~=7I7$N$III77$?+=~::::::::::::::::::::::::
:::::::::::::::::::~~+I~:::=:+8I+?I+~++=+I$NDNDD77ZI77=,~:::::::::::::::::::::::
:::::::::::::::::::~+$I=~:,,,~NN$+?II?==7ODNND887?77$?7~~:::::::::::::::::::::::
:::::::::::::::::~:=~==7=~,,,::OZO?=~~=$7ZNNNN8OI?O$77+=::::::::::::::::::::::::
::::::::::::::::::~~?II7?~,~~,=?7:,OZZ7?7I7DDNO7?787Z7=+::::::::::::::::::::::::
:::::::::::::::::~+??+$$?:::,,:,,,.,7I??I+7OD8ZIO8I+Z7=:+:::::::::::::::::::::::
::::::::::::::::~Z7ZZ+$$+~~~Z~::,,,,::??=7++?$O7$OZIIZ+++~::::::::::::::::::::::
::::::::::::::::I,,$Z$Z?~~~+8O+,~=~~=+=+====+?7$O+O?IZ=?:~::::::::::::::::::::::
::::::::::::::~~$777::?~~~+D8??IIIN$N~~::~~~=ZIZZZ7ZZ7I?=:~:::::::::::::::::::::
::::::::::::::7.~7$7:?~:~+$?ZOOOO8Z?I~~~~:~.,$7:$7+?7$+?~~::::::::::::::::::::::
::::::::::::::8Z77.7=:::~$Z$Z$$ZO+=Z$D:~~?$777,.:777,,:=~:::::::::::::::::::::::
::::::::::::::OZI,I=~~~~?Z$77?~:$$,ZZD~~.77.$777::I77I?$::::::::::::::::::::::::
::::::::::::::$?=?=~:~==Z$~.77$I7$77+::.:II~:~7I:~777$7Z::::::::::::::::::::::::
:::::::::::::~+++~~~~=+$7I~.~II?I~778=7:,I7?=77I77:~I+,Z~:::::::::::::::::::::::
:::::::::::::??+=~~:~=+:,?I?+I??I:,:7O7.?IIII7~I7=,,O~?$~~:::::::::::::::,::::::
:::::::::::~?++=~~~~=+?,7II7I,..I7~7$Z77II?7III,IIIZZZ$Z~~:::::::::::::::::,::::
::::::::~:~?=+===~~=+$777..77?,~777$OMZ7I.,,+77:,7Z=~Z$Z~~::::::::::::::::::::::
::::::::~=?+=======+7$777,..IIIII7$$O$:?$7$7~,7$,7Z:~Z7=~~::::::::::::::::::::::
:::::::::7?+======+I$7::77$7II77.,,$OD:I77777777Z$Z$$$Z7~~~:::::::::::::::::::::
::::::::~7?+=====+IZ$=,:777$I:I$7,,$ZD$7$$77$$7$7?~IZ7O:~~~:::::::::::::::::::::
:::::::::Z?+====+I78$77$7I77?,,?777OZZ$~,.,$7:,,?ZOO$:$$~~~~~~::::::::::::::::::
::::::::~Z?+==+?I$~87$77?.,?$$7I777=8~$7+?$:77,~ZOOZ+Z7=:~:::,,,,,,,::::::::::::
::::::::~:O?++IIZ~~ZZ$$77.,:7$7I+7$787?$77$~Z7$$$+Z,~~,:~~~::,,,,,,,,,::::::::::
:::::::::::~Z7+::~=DO:::77II7$$$,,+$$Z$$$7~:$ZZ:OOO~,,~,:,,,,,~:,,,,,,,,::::::::
:::::::::::::~:~~~=ZO$:7777I,:7$$7$$MO7,~Z7?$$O?$O~=,,:,:,,,,,:::,,,,,,,,:::::::
:::::::::::::::::::Z?OZ$+=$7=,~7$7~OD8I.,$$77$I:,,:=~,,,,:~,:,::?,,,,,,,,,,:::::
:::::::::::::::::~:8DD$$D8$$77II7$+88$$I7$$$7++:::~==~,,:,,,:,~.,,,,,,,,,,,:::::
:::::::::::::::::::=ZO$ZZOZZO$$..=7ON$777=,:$$==+=++==,,,,:::::,,,,,::::::::::::
:::::,:::::::::::::~OZ$I=$$?~~$8~,$NO$$7$I,,Z$++?+==+?=,,,,::::::::::::~~::~::::
:::::::,:::::::::::~=7Z~:$7ZI$$Z$Z?O$,.,$777$Z7OZI7I==?:::::::::::~~=~~:=~~:::::
:::::::::::::::::::::::,,:I$7Z+$$O+$Z$+,,~=$?O7$II8$???=~::~=Z?:I$+:::::::::::::
:::::::::::::::::~:::,,,,,:::,,,.,~O$=:,,,Z=8==?I$=+$$$ZZ$$ZOZ$OI~:~::::::::::::
:::::::::::::::::~:+~:,,.,,,,:,:,,:=D$Z+?ZZ::~~=?II======~~~~~::::::::::::::::::
""")




page3_art = ("""
______                                  _   _               _____       _     _            
| ___ \\                                | | | |             /  ___|     | |   (_)           
| |_/ / _____      ____ _ _ __ ___     | |_| |__   ___     \\ `--. _ __ | |__  _ _ __ __  __
| ___ \\/ _ \\ \\ /\\ / / _` | '__/ _ \\    | __| '_ \\ / _ \\     `--. \\ '_ \\| '_ \\| | '_ \\ \\/ /
| |_/ /  __/\\ V  V / (_| | | |  __/    | |_| | | |  __/    /\\__/ / |_) | | | | | | | |>  < 
\\____/ \\___| \\_/\\\\_/ \\__,_|_|  \___|     \\__|_| |_|\\___|    \\____/| .__/|_| |_|_|_| |_/_/\\_\\
                                                                 | |                       
                                                                 |_|
                                                                 """)

page6_art = ("""
,,,,..................................................,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,...,,.,,..................,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,.,.,,,,,,,,,,,,.,,,....,.,,,,,,,,...,,,,,,,,,,,,,,,,,,,.,.,,,,,,,,,:,,,,,,,,
,,,,.....,,,,..,I???I7II?++????I???+=+===~==~~==========+===?+=~+====~====++++++
::,:~~~::~~~+?=$7$ZOD77$$77=+~=~===++++===============I~~~===+++===++~OZZO$ODO7Z
==+=++==+====+7ZZD8NZ7ZZZZ$$+=+===+++++????+=~===~=========~~========$Z$Z$$$Z8OO
==============+88Z8N8$7I7$OZZ=++=+====+++++++================+=+==OZ7ZO???=?+$II
=+=+=+~======+OZDDDDN8I?IIII77II??IIIII???IIIIIII?III++I+~~=$?I+++OI7$8Z$II$?++?
=8D$7=~======~NODDDDDNDZDON8O?II?????+++++=?II??++++I$I7I?I$7?I$7+=$I77$$O$$7??I
DNM8N$77IIII?+NNNDD8DOD88888D+=++=+7Z======?I??=+?I?8OZI??II+I?7I?777$$I7ZOO$8$Z
8DZZ7$Z+++$?==+=I88ZOZ8OOD8OO+?$IIZOZ$7$7??Z8Z?Z7O$7$O$7ZZZ$O$ONZD7++=?$D8O=~==~
+++8M=++?+?+=+==I$$$OZOO$OO$77?$$+77Z$I7?==+==??7+D8NDZI7OZ7+~=?I++Z7+$ZI+~=+OOI
87I+?=ZOZ7?+77M+?7I????I$$I777I+?I$$Z$II+~~+?=$$IZDDNNNNNDOZI$$$??$Z$$I??~$Z7??+
7$I?+==++??I=+?I7?I7OOZ8OZZZ$$7++ODN$ZO$Z$$ZI+==$ODDNNNNNN8I7$I?II77777$$7+II?I7
O$I7==OZI=I~8+++?+?ID8OO$OD8ZOZZ$ZON87$777OII=???888DNNNNDD?II$II7$7ZI7$Z$$Z?$77
Z?=~+7Z77$7III7$7$77$$ZZOZZZ7I7$$OO$7$$$$$I?==?+I$ZOO8DDD8OZ7?Z?~+=I$$8ZZIII77I+
+?ZO87+,:~:8++++?I7II777$$ZO$OZ$OO$$ZZ$$ZZOO$ZO$$7?$$ZO88OZ$OO$ZOZZO8888OO8OO$OO
I$I?7~~=?II=Z$7$7Z$Z777I?7Z$O?:8O888ZII+,.,,,,,.,7ZZOONNNNZZOOZZOOZ8Z7OZ$OZO$8OI
?I7Z$$7IZ7$I$I??IZZZ7$$$O$7$O::,,,,,,?,,::,:,:,,,.7ZZ8O8OZ7+O8$O8ZZOOO8OOZZ8ZO$Z
??I7$$$ZZ=?OO??+77ZI88Z?I$O7Z:::,,,,,=:~:::,,:,,,,,$$I7$$7I++IDD$Z8DDDD8O8Z$77$7
$$$77III$~I$?+?$7NOZ$Z$O8$ZZ87::,,,,,,:,:,::,~,,,:==?I$$77I+?=~~:,??IIIIO+7I++==
,=+7$8Z?=8ZII?7$7$Z777ZZ7I777O::,,,,,~~,,~,:::,,,:===I?I?????++==~~~I$$Z8Z+,:~++
=++7:::~===+=+II77$$7I????I7$7:::,,,,,,::,::~,:,=~:+++?????????++=~~~++I?ZZ=7?$Z
++??+??????III$7I?7IIIO$NNN$$I::,,,,,:=:::,:,:~~~~=+++???+III7777??:~77OZZ7$$Z7?
I?7II?II7777I777777??I$DOI+=?+:,::,,,,:,,,,,:~~~?=?+????7I$ZZ??7?I+7?IZ7I+++$7++
I7I777777II??+========++++??+?~:,:,:::,::::==?II+?I?I??II+III$I7$7???=II77+I+7I$
$I????+++=====+==+++=+++:,~==?+:::,~,,:::,?=III?I$$?II?II?I?$Z7$$7II7I?O$I$$+?7?
D=+======~====:::~==?=77O7I77Z,~?::~~~~,?+==?$$IZ$+777?II?II$O7$$7I7I$II?7$??II$
N7=,~~=+=+7?777I$ZOZOZZ$$III7$7I?+=+=:=:,:=$Z7?$Z7ZZ$II?I?I7ZZ7I$7I$7?I7$7OZ++??
$O$O$?$$$Z87$$?$77I$$7?+==~=~:$$MI??.===++$Z$7ZZ$$ZZ7ZZ$7?7IZZ$I777$$I7$7??I??$I
O$$77OII$$$7I+~~~:::::::::::::~ZNZZZ+?+Z?7Z$I?$$7NI7Z$$$$I7IZZ$?777$7?$Z77I+?7?+
$7I+=~=~~:~~:::~,:::~?7$IO$I?=+=?=:IO?7$=ZZII$8DNZ$ZZZ$$77II$$ZI?$7IZI?+II???+7I
~~~~~:~:,:=?77$7O7?+?+?++++??I?I++:~:?777Z7M8DD8OZ$$$$7777II$$$7??I+I+?+?+7I?++?
=II$OOZI+++??+++=?II+~~~=~=+~~~+I=7I?==+???+$$ZZ$$$$$Z77I$II7$$7I?I?????I=I?++??
??++++?+???II7I7I~?:~===+7$$O=ZMD:+=I+~~?~+8$$Z$$$$$$$7II7II7$$7II=I7+I=?=?I+++:
III7777777III7I7+7I=+$7O8ZO+?+OONDDNMDNNDONDD777$$Z$77II7I?I7$$$7IIII~I++++=?+?+
77III77IIIIIIIIIZZOO7+ON+M8OD8IZ$NNDDDDNOD~~=?$IIIIIII?7$$7I$ZZD$+??7M$7?++=+=+=
7IIII7I7+I+III7?ODM7OO7O$~ON8O8M:::ZDNND=78DODO8O7?IIIZ$ZNMD8D8Z7=++???=I?=??~:?
""")

smokey_da_bear = ("""

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~:~?8DO?::~:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~::,D8888888O,:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~::~~~~~
~~~~~~~~~~~~~~~~~~~~:~~::::::D88DDDD88D88,:~~~~~~~~~~~~~~~~~~~~~~~~~,:,....,~~::
~~~~~::~~::::~~~~~~~~~:::::~8ZZZZZ$$$$8OO8+::::~~~~~~~~~~~:~~:,,:,,:.,,:,,::::~~
~~~~~~~::::::::::::::::::::ZZ$OZZZZOZ$$$7OO:::~:,:~~~~~~~~:~=~=~::::,,::::~~~::~
~~~~~~~~~~~:::::::::::::::IZZODDDDD8$$O$Z7Z?::~~~::~~~~~~~~~~~~~~~:::,:::~~~~~~~
~~~~~~~~~~~~~~~~~~~::::::,O88888888888888DDO,::~~:::~:~~~+~~~~~~~~~~~::::~~~~~~~
~~~~~~~~~~~~~::~~~~8O8D88O888DDDDDDDDDDDDDDDO=,:~~:,:~~~~~~~~~~~~~~~~~~~~~~~~~~~
=====~~~~~~=:~~~~~~~=DDDDDOOOO8888888888O88NDD8888~~=~==~~~~~~~~~~~~~~~~~~~~~:~~
~::,~:~===~?+I:Z7~~~~==:ND8Z8DD8OOOO8DDD8OZDZDD888~~~~:~~~~~~~~~~~~~~~~~~~~~:~~~
:::::~~~~~=+7Z?,,,~=~~~=~~$OOZ888ZZZ8DD8ZZ$$ODN==~~~~~=~~~~~~~~~~~~~~~~~~~~~~~~~
:::::~~::,~:,,,:~:::~~+::=$ZZZO8OZ$$O8OZZ$78Z~~~~~~~~:~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~::::~~~:::~:::::::::~7$7$ZZZ$$$$$$$777O=~~~~~~~~~~~~~~~~~~~~~~~~~~~~:~~=~~~
~~~~~~~~~::~~~~~~~~:::::::$$7$OO$$77$OZ$7778::::~~~~~:~~~~~~~~~~~~~~~~~~~~~~~=~~
~~~~~~:~~~~~~~~~~~~~~~:::=ZZZ888DOZO8888Z$Z$::::,,:~::::~~~~~~~~~~~~~~~~~~~~~===
=~~:~~~~::~~~:~~~~~~~~~::=8Z8O888888OOO8O887:::::::::::::::::,:,7=:::::=~~~~~===
=~~~~~~~:~~~~~~~::::::::DN8D8D888$7OOZ8DDDD~:~:~::~~~~~~::::~::~:::::::,:+=:,~~=
~~~~~~~~=~~=:7+I:~~~~~Z8DDDDD8OOOO8OZO8DDD8~::::~~~:~~~~::~~::~~::~~~~:::~:::::~
===~+=~~~:~:D$8D$=::+D8DDNNDD8ND8DD88DDDD8D$~:~~::::~~~~~~::~~:~~~~~::::~~:~:~~=
=+=~=~~~=~~:8DD8DDODDDDDDDNDDDD88D88DDN8DD8DD::~::::~:~~~:~~~~~::~~~~~~~~~~~~+::
""")


page9_art = ("""

+=======~~~~~~~~~~~~:::::::::::::::::::::::::::::::::::::::~~:~~~~~~~~~~~~~~====
======~~~~~~~~~~:::::::::::::::::::~=::::::::::::::::::::::::::::~~~~~~~~~~~~===
=====~~~~~~~~~::::::::::::::::::=II???I?:::::::::::::::::::::::::::~~~~~~~~~~===
==~~~~~~~~~~::::::::::::::::::???I777+7?I?=:::::::::::::::::::::::::~~~~~~~~~~==
=~~~~~~~~~~::::::::::::::::=I7+7III7$77?III?I::::::::::::::::::::::~~~~~~~~~~~~=
~~~~~~~~~~::::::::::::::=7$III777I?+7ZI777II??I~::::::::::::::::::::::~~~~~~~~~=
~~~~~~~~~:::::::::::::IZ7$II+I$II~~~ZI??II?I7?III?::::::::::::::::::::::~~~~~~~=
~~~~~~~~::::::::::~?I+$I???++~~~=~~7III??I?II7II?III~:::::::::::::::::::~~~~~~~~
~~~~~~~~::::::::~=I?+~~~~~=?~=~~+~I??I?I7I7==,~+++,?II~:::::::::::::::::~~~~~~~~
~~~~~~~~:::::~~~~~~~~==+=~~~=+~=I+77$$77$ZZ+==+888+=I?II?:::::::::::::::~~~~~~~~
~~~~~~~:::~=~~~~~=+==~~~+=+?I+===~~===++$I7I=ZZOOO$????III?:::::::::::::~~~~~~~~
~~~~~~~~====?=+I777??+==~~~==~=~~~======777+?Z8DODO?=++7????I~:::::::::::~~~~~~~
~~~~~~?=???+=II+?=====~+~===~~==~~==~==+7$$7+OOMMMM7++====+IIII=:::::::::~~~~~~~
~~~=?+I?+========~~~=~=~~~~~~~~=~~=~=~~==$ZZI$DOZO?++===?+??+=+?77::::::~~~~~~~~
~=?++?++==========~=~==~~=~~~=~~========+~=?+=88OZ?++++++?+++???+?7:::::~~~~~~~~
+?++++++============+?======~~==========?I:~=+$O8N7:=I?=++I+?++?+++??:::~~~~~~~~
++?7?I++=+=========++==?=+==============7=$7I=$$$DD$=+?++I+???+??II??I~:~~~~~~~~
?+I++++++++?+===I+?==+=+==============?Z$7Z$I+$$$7D7I=7+??I=?7????I???I+~~~~~~~~
??++++?++$?++I?==+II77I?I7+=+?++======ZII$$$$$$$$$Z77II+?II7OZOZ78I+????I~~~~~~~
I?+?7?II+++++===+====+=II??++=+======7Z~IOZ$$$$7$$$777II+??IOOZZOOOOZZIII+=~~~~~
?III?$I7IZO7++I=++====?+=====+IZ++=+Z7I=I7$$$$$$$$$$77II+++I$778O8I$OZO$$I7I=~~=
O8ZIOD?7ZOOOZ$ZZZII+?IIZ$$===++====7$7Z=7$Z8Z$$$$$$$$I$ZZZZZZ$$ZZ$Z7$Z$Z$O7$$7==
888O$O$8Z8O77I7ZOZZZZZ$$$$Z7Z$$$ZZZ$7I=~7$$OZ$$$$$$$$$$7ZZZO$7I+=+??I??I7$ZO8OI+
?II???I?$$?I+~I=======~=~~=~~~~?~+==~+=+77$N$$$$$$$$$Z7$==+=======+==+=+=????+??
============~~~~~~~~~~~~~~~~~~~:~~~~~~~+77Z8$$$$$$$$$O7$~~~~~~~~~~~~==~=======++
+=++=+====~==~~~~~~~~~~~~~~~~~~~~~~~~~~+$7$O$$$Z$$$$$Z$$7~~~~~~~==~=~~=======+++
++++==+========~~~~~~~~~=~~~~~~~~~~=~~~=$7$D$Z$$$$Z$$7O$$~~~~~~~~~~~~=~====+===+
++=+++==~=~=~~~~~~=~~:~:=?~~:~:~~~~~~~~?$7$8OZ$$$$$$$78$$=~=~~~=~=~~~~~========+
+++==========~~~~~~~~==~~~~:~~~~~+++~~:?7$7$OZ$Z$$$$$7D$Z~=~~==~~=~~===========+
""")

page10_art = ("""
.......... .+=,$N8 ~M88=8$88888$888~88$8=:,,,,,,,,.,,,,,,.,,,+, D.+ I..  ..  ..M
 DMD,ND  .NI+=MM.... ..+.......... ... ...   ..: .... ..7? .=  =,O 8  .O.... ..M
 O.. IM.=M..=MM.: NNNNNNNMNNNNNN.8INNNO.ONNNNNMNNNNNM. .O.N  $  :.:.N. 8 M     M
Z ,  .MI M.$NMMM .~  . . ... ............Z$$ N ...... + .,.Z .I.~.:.?, ........M
 .  N M M7MMM=M=~   . ... ,   . .............D ....,:?.D : . .M .+. .. .. .....M
?? . :....  ++M  Z:   ........  ............ ..~........$N   ...... ..I ,. .  .M
.... .. .   ++M ..: ....  .     ....+? .....I..=..... .. .........D ....M=.....M
....:...D...++M,..:... .,...... ...$7$8 .......~........ ... ...... ...O.. ....M
?...:....  .++D . :    ..    . .....OMMM:..=.. ,........  ..  .....N.....  ....M
7... .... . I+M D.: .8$8MOMMD$M~MM88MM8DM~DMMMN+M.N.:....:..  .... =..   M.....M
....  .......+M.  Z DI ~7MZMDM~MMM +~ZMMDMMMIMMM MMI.....Z........D.~M ..  .?..M
.... ........$M .=M . M7=MM~MMM $$M7M8M$Z:$MMMOMMM8=,....=....... M ...... . +.M
 M ..,.......?M .MM.  ..I8MMOMMMMM7MMNMMMMMNMMIMD=. .... :..  ...N..,. ... ....M
.  .., ......?M  ?D... ,NNDMMMM8MMM8NZDZMMMMZMO.MM~?.  . ...  ...Z  .. . . MM.NM
  M .  ..... ZM .7O. ..  MMZMMIMM,M7MMMIMM$88M8?.$NI. .... . .... .$7.. . .$  .M
$: ... ......+M ..M  .:=O MMZMMMMDO$D$MN,MMMMN8NMO=MM.... .. ......OZ....    D.M
.M.+..8......+M ?.M  ... 8MMMMMMMDMNM?,N=MMNM~MZ..88M.... .. .... .,I ....,....M
...,.. .. .. +M ..O...,,,8M$:MMM MMMZMMMMMM,,MI..NN$M... ........  ~$M. ..D ...M
..N I.... ...$M$  O  : .7,DIZMMD:.=MMMMMNDM:MMM.M..~M....  . ... ....MIMMMM.. .M
.. +.$.:7.7  8M ..8 .,.$ DM MZM~7D MMM?MDI~DN Z=, DOM....... ...   .?  . M ....M
~...?.M.Z.8  MM ..N ~8. ?..Z ?=.=Z7. ~.N= .   DN 7 . ... . . ....   I. .D  I...M
7... N.DMM.. MM  .. M D.?M.?D,.,.+.8M,M$D ...8$.Z.:=MI=.    .    M   , =.   .  M
  ....=.MZ . MM .... ...~OO.$: O ,I8MOM7. ..+  M.~=O $:  ..,. .. =.? M ..  .M..M
O8ZZN,.=ND ..MM ... I Z IM.:+ 7.Z,7,==8+:. 8..ODI .7N.I= ..   . ,8 ?...,,ZNN==.M
.=.....+... .MM ...M.... $.. ~.~ ,=:Z O +?.....Z ?7. M$  ..   ...=?. 7.  . .7M M
. ....~M  ...MM ....,M  .O,. .=.+ . M?8.,..,.N +M  ..7$      ,.. ..MNN , ...N  M
.......O ....NM ..  .NI.+=...:,.7= ,~D8  ,: ,..Z,=: ZI?.. .  $. .. Z  .8  ..=..M
.=....... ...OM .. ...MNZMD  , N.D?M,.Z ~ ,..=..,M8?M$$,..    .. . O..I.D. . . M
.O...... ....OM ..   ..... .: + ?, NM=8. Z..I ..II..M...     ..  ..,. I. . .  .M
.. .. .... . OM .. ..... ... :.  .. .M=.,:7~ +~.~8Z?M..  ..   .  .  . D~.M... .M
. ...........ZM... ..... Z.... ..D.NN$ ,.+~ ,..8..~7M... ...  ....=.. .D.  ....M
, :.. .. ....ZM .. .....  .I..,.Z.7..M .=.:= 8,   :7M..... .$ . . ,    :.  . ,.M
..N.... . .. ZM..   ....M~ ., .=.:..M$.  ,~ =,.+ 8N,M  . .. . . .. ..M. .~...$.M
.+8M.  ....,.OM .. 8....O..D. =.   ,OI~..O .:.= . O?M. ....M.    ..   . .  ..$ M
D:8:DD.. ....ZM ...M....MZ  .D .. M:=,=I  =.7 ..:Z~$+.    .   .. .  8.. ..,. N.M
  ..........?ZM.. ......$~..8... 8.MM$ $8. N  M    ,M    . .. .  . .  .   D. M M
.,. D,...... ZM .... .. 7,O.. ,. ::Z:Z?.=,~. N, .O,+M. ?. .M.     ... . ...  $ M
7MI.7..7M,7MZZM .. ..+..M .. .D Z,77DO:    ?I .D . . O. ++:7..  .D .. . .  $ ? M
.. ,,,:MMMMMNZM   ... .OM..M. ,.N=IDMNM ~..O .I.  8MNM ..~,.Z N   ..7......I.  M
....... ...O.ZM ...==$MM=$N...~ . .ODM=?.D? $$..,. .MM8 .:. . .Z..N?.:  .  I.. M
...........O ZM....D.~.~ $M 8 ?.ID M~M $ . I  I8. NM,I Z .  ...  ..D.NMN.  $..DM
...........N ZM ..,.. 87M:.=,.$.DMMM+M7$$+7 ~M .+ .~M .:+..,  . ..  . ~I 7?D.. M
 .. .......D ZM O..M$ .=8. NMD+==7...  .88.M.++~+.OD+ 8M+ =.  ........... $: Z.M
.... .M. ..M I8 ...OMMOZ:=7 ..  ...  .......=.DDM?=~MM......: .............. .8M
      M......:,: , Z  .M. .....~        ........?.... M  :    ....., N. ... ...M
     .M............ ...8........~...... .. ...:.. ..  O.   .  ....    8. M ....M
     .D.......... .....8 ..................... ..8 .  Z...Z.. .. ... ...  + .+.M
...  .8 ...:.....  ....8 :...........+........O ......O ..?.. ....   ..........M
.... 7  ...:...........8 ~...... ....=....  ..  ......O. .$.  .. . .7......... M
  .  .~....:.....?.....~. .......... .... . ....... .. .   .  .... ..... ......M
    ...  .  .. .. .... ...... ....    . .   ..  ..    .  ..   .      ..     .. M
    
""")

page15_art = ("""

 .. . . ......... . . ....  M. . ... . M............M......N. NZN,MM7OM........M
 . .. .. ..... .. .   . .  .O. ..... . M.......... .M.....  ..~Z7M?M +D .......M
....... .. . ...... ........ .........OMO...I .. . .$........7:ZMM:ZMMM .......M
.. . .. ...... .. . . .  .  8. ....... OO...:8...8 ,N...... .7..MMOM.II........M
.. . .. ...... .. . . ....   . ....... OO...MM.. $.D?......~.. .?..?..?........M
....       .   .. .   . .. .I  ......8.OZ...7NII7$.MM.....I~ ~ N , ?I?.  ......M
.. .  . .  . .  .     .     7  .  . .87.8....M7 .$.  7IMM.M~  .$ . ~MI+  ......M
 . :O~~... .    .  . ...     . .  ...87O,,,,,,,~NOO.... ..78. .+$ ?.MM$ .......M
.....,,NN,,    ..DD,, .,..... ..  ...M7.   ,:NDNN.........7N 7.MM ?.MM:.,......M
.... +??MMM$Z ..  ..++DM.. .++++?????++O.ZN8++  M........ .. D MMMM.M8? .......M
...........M....O ,+~....... OOO.... . M........M.......... .M.ZM,M7M$? .......M
....     MDDDNMMMM:.~  .I.....   ?...~M .... ... ...::::MM7  I..M.77NI. ... ...M
....$MM++8++    . M :=..7. .. ...~....M.,..7NN?O..7M$Z$+:  ..I ++ ~M??8:..  ...M
......M.     $..7.M ....I.............MM.. MMM7...7NNMMMOM   . :,MM?,.M~.. ....M
...~...=+N.NNN. M.D. : .I....N$ .....8N .. MMM.: .$NNNN+ZNN I$Z,.. =NDN8.   ...M
.:MM8$7777~7$7?M+.?.....I... .7 ..... M  .++MN,7 .8.MMIZMM ...............  ...M
..... .=. ..M.,=$ O. ...M  ..ZZ.....~.Z ,.=MOM?7.$Z,O??ZO=.......... . ... ....M
..:,NNDDDDN: .=Z$.N.....N....DMM....,.D ?MMD8N:MM.?,:~:$+= .......... . .......M
...=...,:DMNM8,M$.M .?..7....+?D....+.IZMDMDN MMMM,,MMDM== ....................M
..   .=.....+  M$ M ,I..M.... ?......??Z$7$O8$,MIMOMMM?M=O ..........  ........M
. Z.ZZZZ$Z8++?.MN,? .: .M.... ? .....8$D7Z7+M.$$MZZ,+. I:8M......... . ..  ....M
.. O..=++NZM8O+M..? ,?..M.....I ..... D:NM:++N 7O~MM +.. .I ...................M
...    N..   .OM..  ....7.....I.....  MMMMMMM. 7=N~MMMN .  .. ............. ...M
..,8?O$N=:..M. M.. +I ,.7... .?.....+ N8NZ,$$N,.NMDM$.O.  .. ..................M
....7.??MMMMNM$?.NII. ...... .M .. I~?OIN..OM,8.MMM?D$.7..~ ...................M
..O ....N   . +I.D $M. . .....M  .=D.MMMNZ+M$NI. 8DMM~M.I8 ....................M
...N D=~   .?...+8 MM .. ...  7 ...MMMM7::~ON=8? MMMMDZ M+.............. . ....M
....7  .MMMM..M? M ZM. .. ... 7 .MNNMOMZMMMMIN,7DMM~ZM:MM,.............:M.= ...M
.   ....  ....I~ M.ZM .. . ..8$.MDMMZN=+ZMNIMM8OM I7IM$MMO ........... .$Z.IM..M
..$$$$M??... ? Z.M.ZN .... . .=IO8M=.DM..=,D=?$7M$?.7ZZ?M?=?..........8M.?IMZ .M
..~~~D8MM~MD888M~~ O=  .  .... =OM8 =:7I.N,.8Z,I~IZO:??8+.+ Z,....... .MN......M
.... :MM8MDMMDDM.~.O~7 . : ...,=$M.8Z 7O.? NI ...,$,:7D.D$M~ 7...... IM........M
....I.. .OM=.ZNM.8.M~7.. : ..NNMM$=8.8... .OMNZ=.+$. .8.?OM8.?.N...., $:Z......M
.= O8I= M  .. MM+D.Z~7 . : .M$Z..:O.IMO ..  . O. +.. =8:N.?8.I. ....+M+D ......M
..==8:.~8O.M. ..=+NM~M...:  .?M. O=,=8N ..   ~I   .,I M.??NO.:  ...:=M......M= M
.. ....~NZZ$?M .  ?O.7?..,,..+8$ $I$8.$.,. .I7.?..O,.Z.D I8$ =:. $..M7Z?....D?~M
.  D .... NM,, NM.?M, .M N,.. .MI..M,M7  IO..... $$.+.M MOIM=, ...DMM  ....M.,MM
..8O~.. :O~.=~. ..?=. .M.=D..=IN$N :$,~...Z$+ =I:$.,=ZO I:7.8.. .  7M+.....MZ$MM
.7I. 7I7N. ?  M. ......,.: .  MMIM7I77 ..  $I .=  MI ..~.$O:..$..M8=.+ I77 M7I7M
........ .O$+7.........$.N .7.8$D77.M,..O. ~7M,7.M+....M$O. .=MO7MM$MOZMMMN+IMIM
... :8. ....++...... .MMMM~DD8$8M8NM,OI.. .. N7  ....ZM:. DM8MDNDM$MDM8D,:NM7M M
 ...........=I.....ZMMMMMMINMMNMMNMMDMM=. .,. D. ,..M,M.M,.M7NMNMMIM87D=N7MNM+ M
............ :...,MMMM?MM.ZOM7OMMMNMM:D,$.,~I ..$ IN8MMZ, 7M=  ,7M?$M+N.$O~IMNIM
............  ...MM DM.8 MD Z,MMMM,OM=MM$:  ?=.:. MMOMMMMNM~O7..$M?$M7NDM$ IO=MM
.............?...MMDNDMMMMM7MOMMMMM MZMM8.  ..O7.ZMMOOMOMMD8 ID ? :$MM?M?~NZI=MM
............  ..ZMMMM:8.MM,$M+D=ZMMM8$NM8O$. M$?MMOMM:M.:MMOZN=,?MM$~D  =M~..88M
........M...?..MMI$MM.NMMN?MNMM?M,:IM8,MOO.:N8=Z.8.,DMM.DI8~8ZM+=MDN+7,:$:   ~ZM
........ .....:MO$MIMZMMO$M8ND+M7MMM+N8N777~.?,IM O77M78 .7MZMMM7,7....M8Z777M~M
........ .....M8MMM$MZ.MONM?M.M.D8Z8MM~...   ?8M78,ZM$MM+MMM= :?OMD8 MDNMMOMNM~M
..............NMMMM~NMDM$MNM8MN~IM8MMM,$:.Z.,=7D ZODN8MMDNMM=.=NMMD8::,~MM+ Z?$M
.............. MMMMMMM~MMMMM.M?MM,M$+8M .,M+  MIN+M:M.M..MMM=I8,I.   IM..M,M. .M
.............. MMMMMMMZM8$MMMM7IMMMI8.O  . 7OM.778IIIM7MZ.~. .7 . .+MI7. .78Z?IM
............ ..M8MMMMMMMMM7M +?N M~:$+ZN D.8OM =.+M=+M.D.++ZM . .,8.  8=N.$..++M
............  .8MNMMMMMMM8MM,MMM M8OM8 .? 878+ +=.IO:.OMMDN.   ,~8MM.  .~M +N8.M
....... ....  ...MMMMZ8MM?MMMM+ 77?INO7DZ,D.M~.M+,M~,?.M$ ..I =~M=.7 ..MM,Z~~~,M
............ ..? . MMIMMMMMMM..8I$ZN~ N.  D.~ MN~MMO? D+: ? :N.  .~MO.~O .~....M
...........M~I==$MMMMMMMMMM.+.7. =DOIM=OO:I7OM7 .MN.OO8..~ZM. .7..O.=O .M,=... M
........M7,.?O.7MMMM8MMMMMMMMM:Z8MN+MDZ:IDI.Z?$ .M.M8.M7OM .O  Z:$~.OO M ~.Z.DMM
......MI. ...  :D.IDZ8MDM. . OO$MON~DMII,M77.IM~.~MMMMDM.7I.. ..  I7.7..D..7DI M
......NNN,7D$I:OM8M$M7MMI .......IMMM8MMN:,.Z~N....MMMMN+ :M, :M..D MM, NM+N ,NM
.. D:~:$ :::IID$7NN,?MIM,~+887+....$NIZ7DOD:.......MM. ?MDMN.I88=DZZ... ,M:=:: M
 .?  8M ......:MDMM$M8M+.7Z8?=~,~+Z8DZMMMMZ D .....MD8  ,D7M$MMM8MZ, ?$=~,I=N8$M
D~77 M, 7$ZI~8MMDM?:$MM ....  ~ .+MO?$.NNIMI8: .. NMMM?.D O$8..OOMMMMMNMM7,~D?.N
..$88N$.=?7:I8MMMMMMMM8I .  .....Z8DOZ .D.8$NM... M8NM::=.:..~ ...Z~........, .M
 .$N7MD?.ID.,MMM:MMOMN8N8D+:~?7M$ DM~+..87:O8M...7MOIMO$=, $ .... D:.. ...... .M
...DM.. ,~  .=MMMMO8N~~+$7OZ+=$?I=MMI ..,?MNM .. NN:,MN8 =..$...... .    .   M M
O+7=N:,: :I+?DMMMM+MI  ..  .....,+Z78...7OMOI.....: ?MMM78 ........  .. .  .=..M
7DM+D,..  .+7=MMMIM   ,ZDOI=,I. 8MM8...8++.$ ... :7 MOMMMO M,I........  .......M
.MDO:....... IMMZ$.  :=.~,.~=:~,N887..8,+ .D.....:IDI D  .?M8M:IMO.    ........M
. 8O?,,,....?M.,+....... . ...7O=D~. O:D,.,D....D .OZM8.... ..D.,D$.N$~87  ,...M
. .== .~7DZMDI?.................MIN~Z,I .. $=... .=?8MM=........   8 ~I ~Z,~D? M
.O=,. .~7?Z ~.I=D, ID7N87NIO.=77MM7MM7...ON ....MDMM$MMM+N=............. .:=.O M
:D::8O~,..  :,:8~..:$?ZZOO~~N7$DZMDM8...:D=....7 ~~NNZMM+M?$O,,7 ..............M
..  IMOIN..... ..... IZNN~,:NZMM$.M M,$==.....+.. .. ..  87 +? =? +?.+? .   . .M
? .. I$ON7.+8~ ............ . ZI7.ZMMMM$.......I ~..$?Z+.: ...$?~Z?~Z =D ZI .. M
M+, ..8,MZ .=78= :D8~+  $?O$ DM.=MMMM.DM ...  .+M.. OM ..  ..+.....  $,,N=~7 ..M
~?DNM ....   +8M:,?NN, ..=~:MM.  .:=. ...  ..=N?N. NMONM,.7 .  .... . ...  .ZO.M
$D8M+. .............. ... . +8.. .. .. ON+.7I,I= 8+..~ ?+...........     .. ...M
8 .,$,.7... . ...... ...... NZ....8   ,O M~+I. .. ..,MM.  .... ....      .  ...M
8  ~O.~DZ.,=Z8,.  .. . .  ,DOZ. .,:+,8ZM7M+==D... .. .8D7O.....?...   . ... ...M
.... .:.$$.$Z ,?IND8DZZI+,7$M$=I:.........  . :87+..:D8 OO7 ........ . . .. ...M
........... .7I7=,:?77.$7I:=M 77.....== :~ +=78=. .$OM7.D.. ...................M
...........................IM.7.... ......,7. .... . ..MZ+NZ....... ...  .. . .M
....... .,IZ.,........,: NM$ ............,.........N$?:+M.,.......... .  .  ...M
......... ?.=. ~:.~,..IO MZM..................   ....   .MIM8?....... .. .. ...M
............   :=$I +   ...Z........................$....  ~+:, ..... . ..  ...M
........... ........ ...Z   ................................ Z~,~N . .. .   ...M
..................... ..... ................................... ...    . .. ...M
 """)

page18_art= ("""

....................+ .....:::::::::::::::::::::::::::::::::::::::::::=Z ..........................M
.. ................=........................................   . .,~=.8 ...........................M
.. ...............+.................... +++++NMZ$8++ZZZOOO  ... ...~ +.............................M
.  ...... .    ..M.8DDDDD::.DDDMZ::,,: ........,N.................N :..............................M
. ,::NDNN.,.,        .........................?M ................,~. ..............................M
.  ...........................................$ ...............  M ................................M
.  .........................................$ ................? =..................................M
.  ........................................+.................I.:...................................M
.  .......................................O ............... O......................................M
.  ......................................:. .............. ........................................M
.  .....................................~................~.M.......................................M
.  ....................................$................~.? .......................................M
. ....................................?............... $.,.........................................M
.....................................~ ...............~.. .........................................M
................................... ,...............+.Z....................... NNO  ...............M
..................................., ..............N.$ .......................$MMMM ...........I ..M
........................................II$MMD$7I $., ...........................$ ,...... Z7Z, ...M
................ . .. .  .?MD MMMM ..............Z ,........................~... .D ...M. .M.......M
.....    .MMMM,MN .. ..  ...:.MMM=M ........... .+...........................MM=  . ..+N  .........M
D8777. ................... MNMDM~$?7M  .......?.7........................... ...  .M  .............M
N .......................DDM8,8D+OMMDD ..... 8,D ...........................8 .: ? ................M
 ........................8$MMD ....?,MM  ~M7MDM?.  .........................8 ...=.................M
 ........................8N7M. D+ ...M ,7$?M$MMO.ZN..O ..................... ...: .................M
.........................ID, .MMN.~MDO.MMMNMI8.DDN+M+ ..$.N.....................O..................M
..........................IM .:M, ,D.O,8DZNM.:,8DNIM.  .~.M,: ..............8 ..8..................M
...........................M..=MMMMM.87=?Z:~$~IMMMM......D..  ..............~...M..................M
 .........................:M..,.=M...$.MOMMMM:?88MM,. ...ZZ== .............7 ..,= .................M
........................N:Z+.88...:,MM?MNDMMIOM?:.M8..~~~DO8...............I...$~?.................M
.  ...................D+..=..8.M..,M M..MM7M8NO: MO........................I.  MD........ .....:7..M
.....................=I....8MO7O=O7M.MMZM=IMMDO.$...........................?MI~7I . ...7?... .... M
............  .7N,N=.7 ..= . .O. O.M ....=~N.M ~...........M  ....... O,, D.~.IZ...N7  ...,........M
  ......NM~NM.  .=MM$  ...$.~..M . .........    .M .... MMMMMMMM ... .... ..~.MN   ...., .MN ......M
 7MZ7I,  . $D7?MN:~M+ ... ~..~ ~=. MM .............. .MMMIMM8M8~M7D?..I$,.. ..7O?+$I,  = .......O..M
    .MZ:Z8N,ZM+ON,ZN.....:8 ..+.M= ....$ $??M$. ...,$NMO?+7MDOMI+M.. ... ?.7 .  .....,...... ......M
=~+D$=$$.7O::?DZN,8. ....N7 ...8?,.....,. .....7 ..8DM8?MI,N87:NM....=. . .7.,M.,N . O.~=. .7~.....M
=:?7N.+DZ DZ.+OI.N8....... ....7 ......7 .......N  .IMDM8IM.8I8M=.. +$~. .?,.MD..  ...~. . =.MZ8~..M
7=.8D=:~O=+Z=.OM? Z .....~..... .+ ....:........ Z ..M.MM=,?MDZ8 .8  ...  :=.+O.D .. :8= .., ......M
~~~?D=IOMM= .. M 8  ...8I. ...$..N .............N ....~MDMMOD+M. ~NO+:..  .:~.?MDM ....  ..........M
 =7MO.. ...O .MOD8..... .8 ...M..O.............8N ..~OM?N8M+MO8~=M8 .ZI ~.7.=NOZN..  .:+ .=,7OM=Z  M
.. I8. .~I,O~  ..= ......~N+:8~+ 8O ............NN.MM?MMN, ~:M8~O,$.OM=.?M+. ..,..:  ..............M
,...~O:    .......? ....~:  ..=. Z8 .............:,? ,MN=DIDMN:ZNND,8I=.M:7..~7 . ,..:,7....=ND?~  M
7   ..............Z. ..?.8 .....77I?..  .........ZOMO.MI?O.  I$MMMIZDO...+:7NM=  M,  . .. 77 . ....M
 ..................7O. Z=ND... I $ ............. M$~  $MO+I.$IZ8?MZM87.. .,O,I $=M ..M+..8     .=..M
. ...................N ?.N. ~D,,NO .............,+M87=NM?8+,.:=??N 7MM .M,Z.N,7Z,I:,N=  .D,.M~8. ..M
 ...................? N .....7 ..M... .........ZN.M....MI$.DO7:N=..$MM..,D=,8.D.D.8.7,$:DO  ,N  ...M
.. .................$. ?$.... .=.=.............8M.Z88:Z$ ~$$7+M ..N$I...$O.Z M.D.Z ?=?Z,7=.?M~ .+Z M
.. ..................:O  ......8  ............. . Z,+.+$I . ~7MM8.M? ..M~. .D,+7:Z.Z:$ Z.O,O O=~M. M
 ... ...................8 O$  ..I................ZIZ:N$?=$I== OM  ~.... .=M:.=.ZN.N.=:N.N.8.+~~I 7$M
...... ................Z.....7O.....N ...........M.. ,.?778Z,O=M...?=::.....O.+ .  M:O,Z ? N.+ I.N M
.......................+ ....7... I , ...........8.7Z.O?~. ...IO.... ..........O=O    M:Z.Z.8.Z..~.M
........................~ ...I... .$.,DOOIO8N=+MM .=I~~:=,  :I:,M................ ~,D= . .8D O.8,..M
................ .......M ...  ... M...........87.O87.... ~ . .~O ....................~Z? ...ND.OI.M
 ..................... IM......... M... .......: .M,.. .+I8. =:$? ...................... I = .. .  M
................  $D,.D,8 .........$ .. ......,. .. ,M=7.Z?D8I+M=..........................:$ .....M
............,8.. .. . ...:.......=.I .........ION , .....N,  N:....................................M
........:  .............., ......N.. .. ......=M. + ...........O ..................................M
.................................M.....,....... ...8 .N ......7....................................M
.................................MO ...D ....., ...O .........8 ...................................M
.................................M8  ..~..... ?...............O ...................................M
.........................,...I ..O.., .N.....DM ......:......7M ...................................M
.......................... ..=...,..:.  .....~M .... .M .....7:..D ................................M
.........................8 ... ...DI .I......:$ .... .N......: .... 8, ............................M
.........................M ... ..~MM .M .....Z$.....7 ...... M........ $ ..........................M
..........................N,.I .DD8, .7......7......7.......8 ........ ~..O........................M
..........................M 7MM.I,$... ~............7+D ....D ............?..N. ...................M
..........................OM$7M78.M... ......~ ......,  ....  .............. . .D .................M
.......................... M:  .M O .. ~.....D .....7 ....   ......................,. .............M
............................NMM ..M... ~.....O......M.....,M .........................Z............M
...................................MI ~?....$? ... .......$ ..........................~. ?.........M
...................................I..88.....=M  ?,~......$........................................M
...................................,ONMD....:NN. =+N .....$N::.....................................M
.......................................=8MM ZNM+$ .M......$IN ~Z.  ................................M
................................ ....., MMMM, ,.DO,D .....M M ...,.................................M
.......................................N.. ........N ..=?:.:M.D ...................................M
...................................................? ..,M8MO .$....................................M
....................................................$M$? .? .......................................M
...................................................................................................M
...................................................................................................M
...................................................................................................M
...................................................................................................M
""")
page19_art = ("""
........................... ...  .................................... .. ........... ................................. M
.......................... ....  .......  ... ....................... .:~  ........................................... M
................................. ........................ ,,,NNN ....,,DM, .NM,...................................... M
...................................... ............. ~NZ. .... N?............?+    ?+Z. .............................. M
.....................................................D~.....?7I.................. ,...... IM7? . ..................... M
......................................................D.......  ..,MM ....................... .. .M,.................. M
....................................................: ,. ................?Z~,..  ............... .?O,Z ............... M
....................................................N ~ .?  ................  ..?8.  .........$?... M. ............. ..M
.................................................... ,8N, ..  =,  ................   ,N$, ,N: ..... 8...........  ,8= 7M
......................................................... . ~8= .. .,O...................?7..... .=.: ...   ..?8NNZ. ..M
................................................... .:ZI  ....... +ZI:     ~.   .......:=7 .......ZI.. .,NI.7M7.....  DM
......................   7IIMI~................ IM7  . ................  77:. ..,7  ...=O  $+.IO...  ?I.~7Z.,7?....... M
............,,MND.  ....~ .. ..N,IM, ......MN..  ....... ..... ..........7N.  .+M,. . N. . N$  ....O .         D?,.ZM,,M
.......... ..:88..................., .,?Z7    .........................Z.:ZD:  ..=,. :Z~D::8I ,8Z+.:8I8.  .....$ . ..:ZM
...........7,.... .$7......................  7I. ..................... O.. ...,=$I .   O.  ..    ?..I$N, 7M   ... .I.. M
.......... DN ........  ?$:...................  ...?MI ............... =.. ....... .. ?7. ........ ....... .?$,I$ .... M
...........,................,:Z: ....................... :Z~ .........Z.. ..................?D~.  ..............,:~,Z8.M
...........I   ..... .... ...... ,OI.  .......... ..... .M .......... O,.= .... ..................$I. . ....... D. ... M
.............. IOI...  ............... I$= ......... $+. .+N........  ?N7 ..... . .................. .. ?$I ..8..M ... M
....... ..:D: ......:D.. . .................,8,  :8,..... ,:...............,D8.  ....... ................. Z,...7:Z .,.M
.... .8M:..............  N8,. ,+  ............ ........ ~.O.....  . ........ .D...88,... .I ................D:    ....:M
..?M,...................I .87 $I:. + .........,?~ ... ..I. ..... ,.?.... IN8.  ... OI+ MD?  . .= .........Z ~? ....... M
...................... =:8,O.......7D..~?. .   8N  :.7.  ........D8?IMI .......  ~O: IM7+~    .8....I7    $, I. .7Z.  .M
......................Z,D.?.......... ,,+D, ,$ ,.,O.,:D=...... ?ZDMD.......... +... ,.DI   . ...~  ~Z:...~ M= :~. ..  ~M
......................= D D..........N+:. M7.MID. ..OM..,..+NZ87 ...,.........= ..7...... .M . . :  D . .7MZI   .. ... M
...................... : =...........?=NM8:   N....~  NMN. .?M+  ? 8N+...   ~..M7  ........N.    ?.Z.:?........ +M$... M
...:. Z............... N.7..........$~D, D~ .MN.O:8DD. =O .~.?,~ D. :,?.. D  ..... :$,   .:........ ~O:.. ..,.I ZZ+  :ZM
.. ..:~ ...............N.$=+....... ....M$. .MN:Z:O88 =., . OM ~.:,,NO O.....I,........ .I$ ............ .: .......... M
.. M?N7 ...............=..Z .IM....ZZ, ?77ZIM:7= NZ.N8N : ..$ 7MO +. 8=, .... .............  .I7. .............7:. ... M
.?....................ZMM=M= +$Z ..8M$$O:7.8.MI+D, ZM.M?M.~MZ . MN$ .+  ..7...... Z+.............. ?. . ........ I..$? M
.~+...:~N ...... ... $Z I O ..8MI,..M..$:$8.8=  =OD~ M..8 ,.M. DOO.$. .~8. ..... D... ,8,. ....... 7.. ~8.   ......... M
=:,M..O.D8,8, .. .  ,.Z. DMI    ,+. 7O,.:MM+I NN:~.+8DD: .$.Z .MD~........ .,$.., ..... .  ,8,....  ..... .  .8, ..... M
.. M  Z  7I,... ~...?MN: .:..Z~.. ..Z+7: .~M. ..DI?M,D~ = ZM, ND.N+ .............?.. ...........:?    ............N. . M
=.+ ..8ZO NN   ,M8= . Z8MD.... .. = ,$7 :, .O..... DO?~   ?M =7 ....~==.... .........~.. .......... =Z:  ............. M
. +M  ~ .. MM, ....,..MNMIM.,  ..I,,....,MM.$Z.7   8~ ,   ,.D .... ....... .  .........  ,7 ...........  :. .......... M
  M.,D ,... .........I~I$, .........+ ..N8=7D.+M~I=?7.,, M$$I?,............  .7?..........  .,,= .......  . .7$,...... M
.   ,.:...,=8Z. .,: ....Z......  . M?,.:MO8~ N ?8.  O8N,:$....7 .7~.. ..........   O:  .......... N.  .......... .7+   M
.   M D:N .  .....  .7..... .N:,  .Z+ ,   =?N$ ?:.  ...:.....$ ...... N~  ............,+.........Z....,D. ..........   M
..+.M DN7.... ~7Z:. .,Z?=...............  :O =: .~Z8 ~......,,..........   .. ..........  .~Z,........... .=~,........ M
..+ ~DN. :.  I. +8: .~=~.  $      ..=O+....,?OD. .O=:...........O=................  ............O~  ...........:N .... M
..+ ~MNMDI.... . ........  D. .....~ .+  D.,$.N .I .... ........... .7?  ........ .+.. .......  .....? ............... M
~~? NDO  ~O:, ..........Z~, ,.I ...  ......OM ~,O. ... .=8............ . $8 .... ...?  ~8,............ .~............. M
Z.8=.O$, 8.. .  ~8 .. ........ ?..  . .....O? ,?.  .........:~    .......... .7~ .. ....... O=  ............. ~.. .... M
....     +.7 .................D ..   .I...~Z ?....Z?  ........   $+. .............  ..........  .Z~ ..............$+.  M
,~M .. ... ................. . DDDO..... ?NN.......D  :8..........  O.+  ..............................  ..........  .:M
........=O,., .........   .$.. 8.+. .... I.. 7.. ..........Z,......7.....=O... .. .... +.=Z.. .......= . +$. ......... M
.............O ... = .8~   ...  .887=~Z=$........8=.  ....... . , 7 ........ .=   ....  .... .N: ............ $~ . ... M
,M$$7,$+???I$$ ...  ...... .+ ..=...... D ...... ..  .,  ........ . 7,.........  .$~ ........... .:=............ ..=.  M
.......  .  .........,,D=.    .7.M.... 7+ZN,.. ... ......+ ......... .  7,.......... ,I............ ...O.............. M
............. ~:8  ....,.D=... I,7.... Z:.   +M:.  .......... I+.  ........ D: . .........8: ......................... M
......... .,..........$ .7 ...~ I . ..78.I : ,.,I,~D, ,$........ .. :...........IM. .......... ++...............$ .... M
... ~Z.. $7+..,:Z:.....,......ID.,  ..MI,:.. =D= ....+MZ, ...........  ~Z.........8 ,I..........D..$.................. M
. =      O~..........    .7Z+... +MOZMDD:. ?=. ....  ,7 ...=O .............~D=. . ...... I,..  I.......D7 . .......... M
. :Z   ... . ..... =Z.... .. 8D  +..+.I7D. ........ O+. ....N+.77.   ....... ~. N+  ....... . ,............:  ........ M
.. ........ .?.~~O........ =M.D.M....87?...............  ,= .....,+ ,N, ....:. ... ..:...........:7........... ....... M
.... ..............$$D+ ....:D .$.....$ $+  ................=.......   DM$..  ......... 7Z ..........+Z. ............. M
..... .......................= .M . .  I....,.................... .  N,...  :=8  ............   ......... :Z  ........ M
= 7...................... ,...+ .N.,Z.7 ...  ..... .......,... . ~Z  .......  :=O?Z, ........... . ....... .  ........ M
.. ., ................... ....=  M..Z I............$: .......$?,  ........N? ...   ?77$...........  +D,...O .......... M
. , ....  . .M....... ..  .......M... 7:8? .8~~O    . ..~...... ..ZI~~  ............... ?87$  ..........  .. ......... M
...=..,:,. . ........ .. ,D .... I... 7... ....... ,, ...... ~$..  ...................... =O:.ZD........,...,MO....... M
... ..................M,~.+  .:N.I ,.+..... .............M. . .......  .NM,..... ...::I  .  ..  N,,Z,.. 8.... D.  M... M
... ....................  =.. .  M.NNN.. ~ = .........7   . ... D=,..................................M=D8..  ......... M
. ?..= ........ . ....... .  . $ M +.Z  M..................................................... . .......,M  8..M$  ... M
............8. . .....,......... M.M7: D   ...DD8= .............................D...... .....  . D: ..=DZ M:D.~.. D... M
................ . =O.........  =Z~M   ...   =,.......................  .=8.......I. OM=: ...ON==O8. ..  ..  ..., . 8Z:M
MO  ........ .,.. ..............?:MM. ..OZ. ....... , ..............$7   ......Z+.Z+I+....78ND  .ZZNN=.=. .8.... M... =M
OM, ,O: ~O=  ~,.  ........ ... .....:.. ... .I... ............ :., . I .... ?:~I,,I. ..... ?N,,I8,,  ,Z=..:.= ....?$:. M
.,D.~MD..ZM~......... ...  :?8 .    ........ .........    .D.... ...~D  $I $... D$, .  .MD.Z.............. DDM. . 8  .NM
~ 8Z NZ,DDZ,..?Z... .ZM+. ..  ,O$+  ................,:+ ...... .Z. ...N 7~.....?.....NZ~ : ....................=M+ .$. M
7.=M?.M.+DI,N?7Z.  O...ID?,.. ..Z ,.7 +........................ ......Z  ~N7.. ......I~..:II................ NMI  MM$M?M
D,ZM:.N,,N,.D.,O.:.M. .OM............ ............ ....... ..........N$....   MM....7. ....  .,M............D~.,+..OM .M
O~:O=,ZD.OO O:,.=,,~,Z.DD. .8N:....... .........   Z ..........,$8Z8D+OI  ....... +MM=  ...........,D=.  ...:+,N...... M
8 ,M7 ?7.7?,7 $ N.?.I..I.O ZM7. .8.  .......  ,?  ................. .. $$=?=. ......  ~Z+O ............ +$.  N ....... M
M,.8O.88 N,:.? =,:Z,D +: 7.$.Z.M,7...MNIM..    ..~Z .....,DDD,, , ,7   , . ,7:N,.I...... ..=NMD.......... ..,N8 ...... M
.. 8M~:8 Z.8.8.O:=: D.?.+,.:,:.? I,+?ON..,ON. . ... ,   .~IO,:.. $.,,,, ....... ,NMM= ,.........,OM~ . .....=,....$N~8 M
$. 7...?D.,, ? D.+  7 D.7.D O.O~.8.$~.7.N7N?. ?D.  $N? ....$ ..................  =.D~$8NI~ ..........IMNI .,N .....MO. M
.I7.D7.??I  7D 7,D.~.:+:? ? O.O~~= M ,..?$.D.Z77   7$. ... ........ ...........O, . ...  .D8I.......... D+~M77..... N ~M
......8 N~.,=O. ZM:N = D 7.+7.D.+I.N,$?,., + N M.O=M:   D:    ......  ,N=......,    .......Z...7M,$, .,,.+= .. 8ZN:$~. M
........ ,Z~~8: $~  :D:O.D..I D,?,.Z,:$.Z ,=,?.,,8.D.$=OD  .=D: ~Z=. .............??. ..........,O~DMD=NDD.  ......,Z++M
............ .7? $I,...+ 7Z8~~8 O.++ ?..7 I 8.N.+,?::N..7.:MM ...77........=IO77DI........:7I.. ...    M:7M+?I........ M
...................7,?O       ?ZN ,? O.~.:8 ~.$ Z.8~.D,,7 .N$ +NDM:.. ~M .. ........ ............D.........  =MZ?$.  . M
..................... .ZD~Z=  ...,8I:I.8,I.7.:.7: 8+.8,,$,.8O :OD..?.?D~  :O~... ...........  ~   .........7...:78M?++ M
.........................  +7.77 ~... 7M. .7.Z Z,.N :$.,D7.I$ I$D ,= Z=.DOM?.  OO . ...... 7=     ............. Z.77=7,M
..............................  =+IO?M..  .7D~.8:.O :O:.+$,?O? ~D.M+ $+,M  8+:MM$.  ?I.== ..................7..........M
....................................IZ:Z~D$ ..,?Z~?.=D=.ZD.:O:.=,=O,~Z,+Z ~7 ?Z.?DZDD...+8:   .........  7........ . : M
...................................... ..7Z:NID,. .:DM8:ZO~ D, O,~O,~$,=,.N:.?7..DI I.7ZMI. .:O$  ..... .. ,:.. 7:  .. M
........................................... .7IIN,IN. ..IM? ?.I?.7I IZ.$?.78 +$::8~ O =? ~Z:78.. ,M?....I. ........... M
................................................. Z?ID.?.  .,ND?.II.7+ 7?.$8=:I= O~:O.OO ~Z:=I.=$$7...,N7 ............ M
............................................ .........=Z~Z+~N . :88,D: 8,.N7 ?D,.7.?:.7?.7=.I+ 7~ D=.ND=. .:O,  ...... M
..........................................................,M8M...:.   MM..M..=O 8 .$  M  M :+. I.:~.:+ .~ MD . MM .... M
""")
page22_art = ("""
.........   ...   ::ZNM~INDD,, .. ::I8DDM ,   $ M $N ?N ., O..=8: ..O .. DMON7. ..:8ON .78$NI,.$=.,8.:MM~, ?.  8.Z~....M
..                  . ..   . 88MM8OMM~=~8 ,=  $ M.7?.+O  , O..?O...~M8M8:   =,?  .~7OIO~.  ,N. Z~ ,$ ~MZ...  , M 8~....M
.M+=ZZN=+.            .. .   ..?I7:~:.,.N.,:. $.M.7+.+N. , 8 .ID+MI. .I?O,.  +D+NZ    .  . ,MI  ~  ? DMI= .I. .N.$: ...M
.    ..?.?M77:II87~. ...... .    .:.777.8. =.  .M.7+ ~$  N.D .~.OMI .  .7MIM?. ......   7I. . .7 .N=.MMMM..I I...,M ...M
  ...,?.  ....  .:,8$8N++88ND~.  .,.ON:~D ,=.  .M.7+..OM N.D..~~Z? NM?D,... .,..   ,O..  :O~~D~~DON~~=MIM  ..D. . M....M
..    ... ...     .   . ,Z. . MNMM..MMM=M ,=   .M.,   +..M 8. NMMM,  ..N=,   ..O.. .. .M..IM . =. NZ8=MIM :   . ..M....M
:   ..  . +.. ...       ...~.... $.?? .?N.,=. ..M.7 ,.=..N.:..8 ...7..     ......?. .+D$.... ..., M88NM7N .....   D....M
7..    .. ... ...+ +. .~.I.. .  .~=Z+O. Z : . ..M.I...+.=M : .N:...  .I. ...Z$+..8? ............,8M?=ZM7D.8  .....M....M
.  .  +=M8$..... . ?      ,:$7..  ++?DZZN ,+.~ =M77 .Z? Z, :~...Z+.. ......ZZ+.. ...............8:,: NM7D 8. .  ..= ...M
.      .  . .. ..NM7M..   .=.  . . Z.NM.: .= ..=M7M .Z+.~,+:M O.. .~..8M.... ...........  .. ...M.,,.D8.O.8  .. ..8  ..M
.       .     .   .   ..  :+DO=::..::Z8:?.~= + =ZZ,.ZZ8 . M:8 O::O$..... .............. ....    O  ..Z8,.... ...~.:....M
..    .. .     .    .    .......    =7DI$+,= =.=7M. 8MO. .M?M7~ ......................... .IIII ZI ~ ZO=+.=.... $ .....M
.     . .               ................ .. .=MMN D+  MN=.  ~ ~.  .  .   ..  IO=..  . ..7+M?ZOOMON.:~78$O..  .  D .....M
       .                ........ .+D8. .......NM  INMM8.  ..M M.  ... .. MMM7?7MM ...  .MM?:?=M=N $~., .D?... ..$ . ...M
. .... ~~NNN+O.          ......  ... .. ..... ,M . +MMMM..  O M.........,DMMMMNMM.......IDMM?Z?=N ::.:.+??.   ...   ...M
..,$ .      :M?N        ......NMMMMMM7 $......I=.~.?MMMM  . M 7.  ....  ,DOIZ?7MM ..... ~,MM?O~:$ 7D.,. ?I..  ..,.. ...M
. MNMOMMD7NIM.NN  ... .. ... IMMMMMMMMM.8 ...  M~~.?MMMM...:M  .........,.8+7?MMM.......+,M.?Z~:~ MZ., 78O......,.   ..M
:.NMMMMMMMDMMOND..    ..... .MMMM?N+M=M 8.... ?M7?.?MMMM...:M ............Z+M?MMI........:MMMMMN~,.Z , 7MM. .... .~  ..M
:.M 888DO===I8=N  . . ..... OMMMMDMMMMMD...... M$?..MMMM.. .8 .   . ..  ~=8:Z=M?+ ... . .M$MMMM:,:.Z   M8M I.....$ ....M
: =OM+~MMMNNM MD    .   ... .MMMM=MMMM8N...... M?I~?MMMM...I8.~..........+MMMNMM+ .......M7MMMNN.:.:.. MNM.:. .. . ....M
7,~O+IZMM7MIN MM      ..:MM8$$N++MMI.MMMDMMZMI~M?M7?=DMM. .ZO.8 ......  .MM+MMM77 ....  .  I87I ., :.. MZM ~  .. ......M
: ~O??$MM$~?M DM..   ,MNM88:DMZ,.MNM$ M=I?MMMNMMMMMN,,MMMM+,8.8.  .     O.  ,.   ....  .  .      8 :...7?$ 7.... , ....M
D =Z,,$MM.:?8 N,   DMMIMMI=DMMDMOMMMMMMMMMNMMMMMMMMM8MMM=M ::.$... . .....    ............ . ....N :   7D7 I.... , . ..M
8 7N ,8MM IM8.N:.N$MMM8MNI?MM~7MMMMMMMN,MMM?M$8MM?8MMMMMON   ...  ....... .   .......  .  .......N..~ ~ ?7.$. .........M
Z.MDZOMM?.MM$ MMMMMZMDMM$~:MM8MMMMMMMM +MMM8=MN I$D+M8~MMMZD?$ .  ... ......  . ..... ..  ... ...N..~ ~ +$. .,..   .. .M
ZDMZN=MMM+?+.7MM MM787,ZO7MMMMMMM$OMM++ZMMMN$DZMMDM~MDD+MMMNMMM .................................?..~...=.8~......,. ..M
Z.NNDNNMM:,I~N.MMMM..MMMOMO+~N:MN.MMM.D8MM=.M:?$7$IM MM .MMMM$8M8................................,. D ..N?8......., ...M
D:MMMMM$MIMN ?D.8D:IMM$O8~8D.DMN.MNOMO~+NMMO.N.~78N =MIN$=MNMIM7DN .......................  ..+8.,. 8 ..NI8..,....O....M
D.MMM?O$M?$MMMMID.ZDMZM.7MM.MM~8,ZOMO :M8MM~=M~OMDI+$++MN.M:MOMZOMM:..... ...... ..........7MNMM.:N 8 ..ZDM.  .... ....M
: +MMI~~=:M?MNM.OMMZMM.M~= D.MI.8MMM:,OMMM+,M.=,M$ZO:M:M~.DMMM8?~:8~Z....... O~ .. D.. ... MMMM88:N D...ODM., ..... ...M
:......~,MM88NI MMMMM==MOZM=MO? MMM  O88I8$=M.:N=$M7~:8= ZN?OMI7. MM 7~..Z,MIMMMIOM+  .   IMMMZO$:N 8 ..ZNM . ,..., ...M
.     .?7Z~7M.7MO~:Z.8~M,I+8$?.OMN..~8ZMM.=N $$.7NN.DMM::M8~:NOZOI+I.M8N .~IMZM.=NN+ . .  7MM8OM8NM,.~. .7M. .  ...~...M
      M.MM.M$,M?DIM.ZOM.,NINI, MMO.?MMI7,DM I+:O88 $$MI.=N8NZMM8.O~7ONMI  =MIOMM7Z ~. ....OM$+OM8NM  ~...7$.:   ... ...M
    ., M:MMZ 88M?M.D$,NM+OM+$.DOM8ZM8MM.?8,~  ZM7.:OM  .8MM87D?D~$$IONMZI NMMMMMDM., .....7+8+NMMD:?.Z.  8,, .:........M
    .D.MIMM7 ?NN?MZ.DM8MMM:8 :NMM:O=8+:D= DZ8M~M.I$M8..MM: :MMM N M8.NDDM~ZMMIMMNM . ......+7D8MMD,  D I M?I...,  .....M
     +,O$M,+MNDMM MODZM~M8M. $N+~MMMMN?,.INIDN+ O7MO, NMDMMMM? , N8$ M+MOM MMMM=,M.,  .....+MMMODD: .D O MZ?:.,........M
.   .D$NMI:+M.N8M 7DIN,M.O .MM~MM~7MI~M.:,=8M ~MMN..?M88=:8M 88.MMM8M~MMMMMM.$M.,I.,.. ....+MMMMMMM  8..:MMM?. .... ...M
. ..$: MMM?~8MMMZ7IM7MMID +NM NO=M8.IMIM~DM: 8$8M=~77ZO7MM~ II?MM8. DM8IMMMMMNMMIM , .7I77. 77777M   8  =MZM+....... ..M
. ..$N MMIN,Z:M:M:M$OMMM.8DD.NMZM=NMM~I=M,.,MMMM,M MMMM,M $D M,,O.MMM,MMNMMO,NIM$DM. .    .   .. ..~.:..,MMM O.........M
:.M=M=,MMMZ?M8MO?=MM?M~,.MOMI+NM:DMMZMMO$8M8MNMMN?+=DD~,N.OMMDD,MM==8M?MMMO8.. .IOMMMMNZ8MMOZOZMOMM~ :. .M+N.O. ...  ..M
~MM7N7ZMMM,ZM~MMZMMMMON.MDMMMMNZMMOMMZZMO8MNZIM=+MMM?? NM?MDM=MM, MM.MMMM77M....IZM8N=.~MN MD7OZMMM~.,..~$O$.$.........M
,DNMMN ?ZMMM,MMM:MDM=M.MM?NMM,DMMM...NIDMMNDMMMMN. ,MMM~MMMM~I,,NM MMMMM:IN+....IMNN=.,NI. NM  MMMM8 . .=.ZM D  ...  ..M
:?$MZM.$8OM~MDDN$MM NI$MMM.:MMNMZ$ZMMMMMMMMM?.+$?DMMNMN.O7.ZNM,7MM~MM.DMZ.. ....IM?8 ..I=  MM .M?$M$....,.ZD D.........M
.~~?MMM:$MMMMMMMMMM$:DM$MM=IM::=DMMMNMMN=+DMMMM+NII MDOMM=I88MMMI8M?D~:N. .=.....MM=. ~...IIM,NO8DMD..~.7.=$ M  ~.. ...M
:ODOMMZ88MMM=NM8MDD$:MMMMMDD,MMMMMMMOMNM~Z~:+DMMNM~Z8:NMMMMMNN:~. :DMM.... ,.... MD=  ~O  7+MMDNNMMM..M.  +I N .. .....M
:DDO7MMM? MOMMMM$M=MMMIN  MMMMMMMM7 .ZMMMMZ~  ..ZMMMMMMMOM=  7MN~MMMN ..... ....,MD,..   =MMMMMMMMMM..M.,.8,:M  ....  .M
:DDZM MDMMMM8MMMO=NMMM=MMM8NM?.,8OMMM, DZ.MMMMMMMN$MMMZ.O+8D8MMMMMM8.   ...+...  MM  7: +NMD7M=MM+?M..8. .NIZ, ...... .M
:MMNMM.ZM8MMMMM$$MM??MMMDDZ8$MMMI MMMMMMM$MMMZM7M88M.OMM8M8ZM8MMMM. ..  I?I?.. . +N.,?77MMMZ ..MM7MM..8 ..DO$, .. .....M
:MM8+MNMNDMMMMM?MMMMMN$$?MMOMMDMMMMMNMMM7NDM8DD=NMMMMMNMMM=$~MM7M .....MDD:+. .. IM., ,:MDDN.+MMDNMM .8  .MMM . :......M
:MMZZOMZMMMMMMMM$MMDOZ$DDMMMMMMMMDMO8N:Z+O+MMMOMMD$.NI+NMM$M=N .I ...,M.D+M+ ... +M ...MMMM+ZM77O.O8~ 8   N7M . ~......M
:+DZZZM.MMMMMMMMMMMMMM8MMMZ.+M7..I?MMMMMMMM$NMM$DZMM$M8.8M8...... ....+MM=MMM,  .?MMMMZMIM ,M7I?8ZMMN.. . MDM...,.. ...M
:DN,M?MMMMMMMMMMMMMMMMM$= OMMMMMMMMMMMMMMNN++MM7MMMDNMM+ ..... I  .   NMM=MMNMM8=MMMOMMMM.DM=.ZI?OMM.D .  =$$.~.=......M
DMNNNMMMMMMMMMMMMMMMMMMMMMMMMMMM$?OMMNMMN. .M=D, .. ..... .... +.... +NMM=MM7  8MM+7M.DI7.MI+DMNMMMM~:.  .~II.$. ......M
  .    ,,7MMMMMMMMMMMMMMNNDMMMMMMMM.7MM.~.NO..  ....... ..... 87MIMMMD.MMMMMN...MM,M.Z8 NM$ZMMMMMMM.M.MI ?,M$,I   ... .M
,..I?MMM8MMM$$MMMMDMMMMMOMMDII7MMM:M8M .:.MM ...... .. .  ...:7.N7 $MM7?M:7MI  . ?N8M  ~+, MMMMMMMM$M .I.~ MD,=..8 . ..M
NM$NMM:MMMMMMMMMMMMMM8DOMM=IMMMMMMZ: .. :.N:............ ...+ 7=  7,.N:7M+NMI ...~M,  ,M7..:MMMMMM. M .M ? M$.7..I . ..M
$IM~$M8OMMMMMMMMM?MMNMMMMMMMN=,..MO....:. M ...............~8?O= . ..,=MN7~MM ..... .,8M7 .MI. =..M=D..M...M8M? .......M
M+?MMMM7MMMMMMMOMMNM.MI  ......:~......  N ........ .. ...O .: ...~87 :8~ DMM. .. , :Z  M .  ..... 7M  M   M7N?~ , ....M
8MN8NNMM:MMMMMMOMMMMI,?,D,..... ........................ MD..+   :O,..8D,  8I7.. .M$ ...., .. ....  O..$.I $DNI, Z.....M
INMMDM+8DMMMMMM,MMMMM$8.=.?Z......  ............... ..  $, 7.~.. =,......77 $M7Z.  ?   .~N    .. ...M..7.$ $=MI,  : ...M
MDDMN.D8MDMMMD88MMMMM~D8.O.+MM,....... 8...............N~ ,Z77. ...,=7~   :M~=:MM8.Z ...7N? .... ...D..:.M 7ON?........M
8MM.IMIMMIMZMDOMZDMMM?,M.D :M:=M8= ....:  .........   O.  . . .DM~. .D?MN  8$, ...MM . .$M. ..   .  8.. =N .MM ....  ..M
DM.8~MMIZ$M7MM.MMMMMMM.N.ZM~.=:=8 D8$ ..+ . .......  N, ::ND   .:M:? O.  :..:ZI +~=M,MD..MM, .   7... . +, ?MM.   ... .M
+ M7M$MM 7MOMM~MM+MMM8 O8.DZ?D$.MI:7Z8 8MN$~....... MDN+ ....OI:. Z~+.7  +   ~M8N,  M.. .I8 O.=~=.M,M~. =. ?+M. ~ ~ . .M
 M.DMM7 MOMM7MMM+MMMN ..I,7IN,M8+ZD8.7~.$ 7M7:MMM8IM? ?N7 .. I7 .7D,..7M++ +Z7.,O+ ~M~..~M8. 7+:7I .D~..M..ODM..8......M
D8M?7:I:?M:$NIMM$MNNZ.  ...$  =?ZZ,NI,M.=D.+DZ.+.,MMIND,D,.: D. ...=8,N:,NN?  .,8:..M.  MMI.. ,=N+ 8 ~  M..MZD7 : .....M
OMIMO87MM$M?DMMM=M8N7    ........ ...$........... Z+O+7MMM=   .=7  ,=$ M$ .=O= .. +MM.. D:MM  DD   ..D .Z.8$M?$M, , ...M
NMZ.~I$$MM,$~MMMOMM8,   . ..  ........ ..........$~$MIIM7N7N7NMZ, ..:?I,,~  .~NZ$?ZMM+Z.  .~:8 8D  M:M,.O.O$MIMN,.. ...M
O $~$,?MM$Z$MMM,8MM8D    .. .....................$I?:8O?M?M    ?8I...N  . 7I+ 8 .7M8 ..D?,.   ,M,,.  .ZIM O M:MM . ~  .M
$M+N ONMMDMIINM MMMZO    ...  ..........  ......M=M$=$~M+M+.....  7..Z,.  . $M. .... : .        ,M. ..: O 8.7IMM~8 ~...M
M 8,M+MMMM MM.MMMMMMM?.$M~......................7,7,M,D.MM ... .  :~M,,MM,.   ..M.N .. .  7.... N ~ .. ,=$M.MMMN=M M  .M
. ,ZZO8M~.MMIMM,MMMO:8Z,?,N,$?,8.$I:D?.7,Z,ZM.7ZOO7Z7M:7$I........NN.I$M.= ...~ M. :7Z..........., ,,....Z  .7...MM$...M
.=NODDM8=M??,M,M8MM=O:I,I? D+Z? N=$8.N.Z?IM8.OO.O?ZMI$IM+.........,$=7=ZD,...... ...... :.....~O...8.?......Z$8 ...  ..M
D:MIMM7.DN.$M?=?MNM+,O~D D~,M.NI=N.D,DD I~+7,:ZII+O :OO O .......MO.Z+D.?D=?.................  .. ....7, .  .. .      .M
DN:M,O MM. IM OMMM.M.M.M+,M.M: N M.=N MM.M,=,=?MM.M?,.OM,......   M M:~M~M.. M   ...... ... ...........I M8.. ..  .. ..M
MM~:D.MD.,NM.NMMM8~:Z:Z~,8:88~O.8:$Z:8~~~,:+:87Z~7~:D:8:....... .$:O+~Z:D.....,DM.....  ..., ..........I............ ..M
D?I.87O..87 NMMM+.8 Z~?OII$,M,Z+:N+DII~I77$D?I~ZM:M:$:Z . ... .=,O7,D.7?$.. ..~?ZZ.... .  ..7.    . .. . .......  .....M
M?:MM,,+ON8M8:7   . I78=8,M~=Z,N,D+~8~I?+8:Z~DDM=D~8.D=   .....=O,D8::~,?.  .. O$8?:. ..  .. N   .  .. ...   ...   . ..M
=+M? ZNMMNMM =     .. .... Z.D,:. M..    :  ..  7~?,M,$.. ... .M~7 8.M,M......I~D,8~O.  .... .M ........ .   . .  ..  .M
MM..M+ NMM,7..  ..  . ..........................Z.D7$N .......~,?8.$?O~8......$.N:N,N........ :7..........   ..........M
I.7I.OM7~.M    .        ... ............  ......Z7I8ZD .  ...=D Z:M I?7I  . ..N:8:7IM  .  ..I . . . .... ........... ..M
 M$:8?M.?I              ........................7$OO.M... ...:ZO.~MI7?$ ... ..8$+$,MM.. ... ?=..... ...................M
M~,ZMMNM.     .   . . ..........................$?7MN........M M N.M. .. ... 7 8.O ZM. .  ..M... ..............    . ..M
=NMMM8M=$,., 7 $.Z.,.?.. .......................?8.$D......=O:O:O,:?D....... =+ O~Z.M~$ ...............................M
MMMMNM=7=M.M,M,D +=$:$I.I.D.M,+~N 7~$ + 8.D MO.  $Z?I.... =N:$~:Z~O=.   . . Z.D,Z,M,M. .$. ..   . .   .............. ..M
MN:M:N+I+8M+7?:M.M 8,7+=I:D.M M D.M:O.8+M.M?.M8:O=ONM... .~8.OID.87 ....... Z+I$~II~N+  .+= ............ ...... .... ..M
DI$IM?MMI7M Z,$I+?.M M.7+II,7,$.N?8.O:O,I$IN7,M MO==+  ...D?N 7~Z? ...  ...D=Z.D.Z OI+..  . O   ..  .... ..... ........M
8M=N~D N7+~ 8.O~7N.N D.D:8~8.~N$+$~ $~7~:D.N8,7$,$8N....ZD=D:D+.N,... .. .,,N,?:.O M +..  ...~:  ..............~~......M
7NN:8~=M.?7:D.D.O ~8=$ D,$ N.N 8~+?=$I=M.D++M+=DO:=8..=.8,87=8:M..........$=$~M.Z??M. ........ :D..... . .  :D? ...  ..M
  O Z~,M M ~Z M.Z,Z,,I?I=Z.$ N O~:7O.M.N Z=,OO:DNM:7.M~M ~D D.8D..... .. D $ =D~N DZ+ ....... ....8:  . .:D.. .   .. ..M
    .=.+ M D=,M.M.Z:O 8~8. M.O,Z=N M M.O:+M.+DN77IM D~$+:M,Z.8........  O,.?.D:M+Z+,N ........  ..  +8M:. ......  .. ..M
            . , N.Z.8.N..8 8.,.,=$,,7N..,ZD~:DDO,+7 Z,D.N,N~O7..  ...   Z,O?7?:D.MM . ..  ... ..... ...N= .............M
.                   .    .. .........................==D:D:D.. .  . .  8:Z?:I:D=D= ... .  . ..... . .....,$ ......  . .M
                         .............................. N=8 ....  ...$=M~Z~Z:D.M.Z......  ............ .. .?,..   .. ..M
..        ..         ................................... :  .. ..... :N + 8~878+M .... ................. .......  . . .M
            ..  ..  .   ............................................ ...  . +$:O ........... ........... ....   ...  ..M
                         ...........................  ... ... ..  .. ..... .  ... ... ..  .. ..... ....................M
              .          ..............................................................................................M
              """)


page25_art = ("""

....................................................................  .... ..............  ........ ...................................... M
.............................................................  . .........   ..  .  . ..........  .... ....  ...    ...................... M
..............................................~~~~~~~~~~MDMMMMM8D8MDDDMM8DMMMM~~~~~~~~~~:.......  .............. ......................... M
..............................IIMMM77$I   M,?  ...~Z~8......I.O .7+...O$.. ?7... Z.,$7.N7O.M+M OI77,ZMZ77+................................ M
...............=+MMON..:  7 N~:.ON..  .. 8 ,.O.,O+8 + NMMO==M=  M= ,Z7 . =M.I..MO~O..  OM ~+  ... I  .,.$.D=  ..  OOMD===................. M
. ..,,MNN.,  . . 7  $ D. ..~ .?O I=NNNNN..8.  .$ $.$.$,N.  ,:,.D. ..N, ..?M. ..M:,NMMZ,,:M.I..$.   . ..MO.?.  .. . M.~.. Z ,  .MMNM:,.  .. M
.,..8.......M .,O ?N +N..D. M...ZI=MM   :? N .. N...+.~II.:+D ,:M.: MM.MMM  ?~, M: , ... M.... ..... D Z: .7Z ?. ,8.8=+ = NMMMM7 .. I :...MM
... , .....7M ...., ?Z .. ,~ .  ZI.?:. .8.N.=8... ..7+$.  8 :.7 =.:...7Z..  ,D: ..8......Z+.ZDM....,.::O =,+..,  ..:::..NM~:: ~ID ...Z.,.N M
. 7 .......M.. ....M$.7. Z .+. D~.8....8 =,D  ???+= . : +,,$  ..MI:...=Z . ..8,...:. .  . 8.DMMMMM$.  8~I . +O.~ .  MZ? O8+???D ~Z  ,ZMN? $M
. M .=.....~I,..  . 7  7$.. .. .8~...  . . +  MD$   .8,?~ , D .I I: . ...?  Z, N,O..=. =D??. . .... .?,. .. ..I.I  DN~=.Z  ... $7.   ?M7  .M
..:..M ...., .+.....?.M+,...,?+I:?..=..... Z.? ~O8MMD. N ZO?N+,,O+ +M: ...M,8M?7 =D:I.D Z .+$ Z    +, MM. . .... ~8D :,. Z ....::$.I  ,M~=.M
..:~.~ .... MM?II +Z MM.    IOI D D~ ... . ,O ? M? .Z.N~D .+Z .  ..Z:. 7.Z:.... .7= ..8  O  Z7 N..  :,.Z$II =8  =Z8. ,: ..M. ...M.M, .,... M
.. I.~:.....Z ====. MO ..... ..M $.D===MNO.,.M.=...O.I.IN~D ~O8 .:~N :~$. ~MO ~.$+..M.Z$  ~.I ?.   ..$:. ,~=~=  ..D.... ~  ~ ,.Z.M .7 .,.. M
.. O..N ....INNN  ,~,+ .... , I I $. ,:N8DN.N. .M  = ., .:8 .. . I  .DOZ+ .  ~,,.. ~: $....,.. .M .,.~.D..     ..M:?....  ....M.N.I ,. ~,.,M
...7 .8.....I. 7.7 N.Z.~ . :.....N$.I,8DIIZ Z:,=..=.. ~.$.N.,,.,.,... O$    ...Z.:..=.$.   ,. ..  .O.Z~  D,I....::O 8.......I::I ? : Z. :.~M
.. .~ . .... .. I 7.O.$...= .....M.ZM .~+.M,.M.N  ~ NZ.~DZ ~8:,..    8  ~Z.=. .~.  .M. .+MMZO .MZ7 ,+.:M.O  I .I =~  ..OOOOOOO ?. ..+.8..ODM
....:..:.....N... .N.+ ,.?      ? +I ..?.  ..I~... $D.. $, 8$.8I:+N+8+...Z~D=.. ,.Z,7   ..?IM$$. .Z Z.. ?  .  .. .D.$..7$~7== + M. ..+.8 :.M
....O .O.... +.. ,..+7 .~~~~~=~~  Z7. .  ? .  I .D:.O=.8I N=.+~.. 8~ O88   D?DO..+=+ OM?~OMO8. .= ON... . I..?..:7,7$+ ..+...?.D $ .... .Z M
....8..8 ... ,..   .$  +.. ....,D $.. $. .....+.Z~.. . ~~ :..Z .M :N = +  M: =$ .+.M  7.7 N .. +Z= $..... .I  ..N.8: ~ .... ..,+~ MMMMI++, M
....,  7....  ..  . ?.$7$77$II~. +==.= ...M ..?~.Z. ~.8....., ..M=.... +.  . N~ NN ..   ~ .. ?...+Z,.  ~... .7.O.:..7.?.,..I...I?  .8M77:  M
......., .....I ~..O MM.  D .. ,= .:O. ~..,~DO 7,,,... :.,....O.D=+=NNDDNZ$ZN8NN?=~  ? . . +I....O. =DN+=~   .8 ? .. Z Z ~ .?...D.Z =O, Z  M
.... $. ......?,. N M$...,..:.$ .?$?. ~~..:DODZ: $ZZ... :NZD:~ . . ...~:.Z IZZZ...   . ::~Z8?D....N.O~DDN8DD:: .I.....7 7.Z....$.N. +   =. M
.....M .Z.....I=...$?: ..,...? .O..N=.,I,,Z+8?D,?,,NO= . .  ..... ~... .  ..................  .++N~+.,?7MDO.. ~?:~...  .   ,..I D   ...~.. M
.....~..M.....?8MM~.M . ..,  ..+ .. :I7?...~..~O? .......... .......................?Z=7,.   ....... IN+? . +~~~~N. ... .  . ...,? N +.8 . M
.....~:.+  ... .,I~::= ..:.....~...M :.:   :O=..............7= .............................,......... ..N7... ?M =..  ... .?D.N..8.7.O, . M
..... O ,. ....I. .M=Z.... ...7 .  ~Z.  .D,.......... . ........ ......................................... .Z8..~O,8MM$$Z$$OO ? .. :.+D... M
..... 8. = ....8:.=.Z M.,.O .+ Z. D.:.O7........... .I, ..................................................... .8+:. ?NDM7II+  8 ....  7... M
..... , .O ....$  ? OD.D ?. . :.=8.7=: . .. ..... :~.............................................................ZM8M$MM::. ~+ ~....+..... M
.......:.I ......I . .N $MM8,.~ION~7 ...........= ...............  ............................................. . 8.O.=. .~.:.7..7. Z.... M
.......~.,..... :  ...M ,DN+,.,D8D, ..........=,...........................................................  I...... Z..:...+ $ D .~ +.... M
.......8 .N.....M?... =.D.ON.8.Z?....I ..... +................................................................ +......O.=   .D,. $+.D..... M
.......I..M ....D8...8 8....: O+..... .....:  ................................................................   :... .M.=...  = ...O..... M
......., .,.....~....,., ...D.,O... ....... ......................................................................7.... .  .+.O N .,I..... M
....... . ,... . .$.Z.M=  ., =I.......... .....................................................................,.  = ...Z .+.N~$..:N  .. .$M
........O....... M,$ O.8 7.~, O . :..... ,.........  .   ........................................................,..D ..7 $:+, =.  ~7?. OI M
........8  7.... 7.:N?O,$. .,MM ..,.......................... .  .................................................=. Z. $N:7?.+.?   I.N.OO M
. .. ...=. ?.....7.DM MN  .Z M$ ..................+.........   . I ...............................................:... M.O .$. 7  7,I.,,.O M
.........  ? ... .+N , =MN=.:M M . .....  ....... ,.............:  ................................................ O, 8, D.$ .. ,I,M..O : M
........ $..   ...I .M  IZ7 = M. +M:I. .Z........= .............D............. ...  ..?MOO,8OZ .. ..  ...........O~. Z=,~...Z ...? :?  ? $ M
.........M  I ....$.7 .Z  ZN  M M. . M.OM .......Z ............  ........... M=,DMZMD.7 MMMMMMMM. ,MNMM  .. .M?  .~N.,.M.Z..?.. .M :I..~ : M
........ ?..M ....$.? .... 8?8NO?. ~D   .~88.. ..O.............:...........I~M:M,MMM=N~8:$ ,MMM.~?8MO.8DM=,....D.. ..~,.. ,$.M . :.MI. +.. M
......... . I. ..., ..... .8 :MM7     .?MO,  ...?IMO$7.........:.........OI$DMN77M?.77M$O~?8Z7M8.Z ?D8$.NMMZ=  ...?.N.8 . ,? .~MM .7...MZ. M
......... ? .. .... ., .=. O: ..,$ .....D.. . $MM++   .. ....   :ZZZ$MMM8NMN+M:.=$:MM+M:M:D Z?,~  IN  $.~O8M.+8......OI..  OMIZZ:.$Z .. N .M
........ .N. D.....N , .=. NM ..ID8, ..,. . ?....,.....,,,888OON8~~=~~~?8N~ZI.O.OMN+M+I ZOM~7~  O...I..=. NMD.....  ~~, . MZ  .$ ,I....... M
.......  .,  M ....NI. Z. +.M .. ,? D. ..........,...,N....$ ..:... . MMM?...,DD?D?.~M7OD MM.DIM..MM .. .. $II... 7 . ::.$.87 ..88?....... M
......... ,. : ....=OZZOOMOO8ZOOOOOONN8.  . .....,DZ. . ..= ...  .=O MM=.. OOZ?7.+~M:87M+DOM8$ 7Z8. I., M .I M  ?,       .  $. ... ....... M
.........  , ...... ,,,,,,,,,,,,,,,.    N...D,..... .,MDND,    .... MNN I?.,I,DI,8N,N~. MZ8M?,$.D+?:.~:$O8.7,MMNNNND8NM:..DM?~ ........... M
...........$  7.....M~~??~?...M M N ..Z ..N8,..~...........    . ..M~O .~:DO7:O.NOOZMZIMI+DOM8.= DD:,:M?D+7I MMM= DMM8M 8MDDDZN .......... M
...........$..M.....$,$O.  =.+7,?~?+~ ?N...Z M7Z.. .............. N+  ..+=~~MO ZMN.MM?7~ MO+$:+I .ZO. : ~O.?.MM? .....      ..$ .......... M
. ...... ..?  I......7 ..,.. Z=..I$O D. I.N:?, .. IM7.. .........8M8.. ??~.7. .MMM=$M+O 7+.~MM+,. O$..D?:D87 MZMM .......... ,II.......... M
...........   I......,.=  8.,7+D$.,+DN= .,.. .. ?+8M~M.MDN+:.... OI, ~+~=? D~.+MMM+MN$8O7.O~ON  +$O+.:$N+I+=+88MM$: .........D. +......... M
............7 .,.....?.+Z8$, ............ ~D8M8OM,I,D.D,:=N,MN:NM8OZ.D8+ , ::.888NMMN?+M:.8IZM  $.:=~~.Z7?..MN+MMMM~.  ...... .I.$ ........M
........   .M .I.....N...............,78Z?D+M D,D~$IDI~7M,8$O++$M~~. $N. .~Z? 8?NN=M+.MO+ ~NND.?=.,O=~8I=: ?MIN8MMDO8M+.....?...N,........MM
............I .7.....7..........  ,$8M:OZI:D O=7DO~Z??=I =+,~O=8M:,. $:+.+.7..8M+8DMMD8=N.~8NN.~ O=NM~N:=.$87IDO=MMZ.88D... $ .. :8 ......=M
....... ...    7....., .........DMZM$O=D,D.+=$:==.:$,7.?I: Z M ~MNZ :,.:., 8.:,8=?OMD=D+MM:~ZM..8~O~MDI? 78ID77MNDN8=88~7  =  ...II  .....:M
........ .. .N.. ..............$O:~?.,7 :,.O,N.?...7 I.8,=+,D~==?Z+OM,+.DD~:.. MDMMMIDM,MNM,=M ,?,M:MM7.NMZ $.N:?ND+8~DN= .O.... , :...... M
...........  M..: ....M.......=:... ., ,,.    .. .......... ?.+:N7I .7 D7OM7~.+,MDZMM+~MODMM.M.M7.I7N.:I7+.,I87=MZ?I  + ~..Z....  .M ..... M
............ ,. M ....+  .... D....7?.=+ . .........?:. . .. .,,,M$,D,$ ?$+IMZ.:.I:OM8+ O8M8M,O8.M7$.8=Z,+  8M?.8 .~. =.I ........7.7 .... M
.........      .8 ............ .~ ... : ~.,,..,....,..~..... D .$N8:?+N=? O.M8I= NOM+MZD7ND=N.M8MM+D~OM..?ZMM7 ?..7 Z+.M. M.......D.Z..... M
........ ..   7  .   ..: .........=:,, $ +.: ,, ..+ ,....Z... OD:,~M.$I7I?N:?MM?M.?=8MM: MNMI~MM,$MNMN..8O~M.7.....+:,  ..  .......N7 .... M
........ .....M..? ....,.............=N.: .....    = ,Z..  . ... I~ M .8M~MDNMI:N?8,8MMM?NMMM=MN,,M.8ZD=NMM.M 7..~: .....D...... I ~.+.... M
........      I  M.... Z.................. ..,,.  . :    ..,.,ZZ,.Z~$8O..7MMMMMNMN=N=NNMM8M=MMMM8.NM7NM7M8N..+.......... Z ..... 7., +.... M
........ .....I..I ... N ........................~O...  . $ O8  .I.:I+IIONMMMDI=+MM?MMNIMZDMMNMNMMMNMMMMM~ ..... .   .  =. ....., 7  $ ... M
.............. = 7.....= ...............................   =+?MZZOO8.O+N8$8.+OMMMONMMMM.I.NM$MDMMMNNMM~  8  .ZDMM7~:.7= 7MZI....M I..~ ... M
.........  ....O .+.... +................................................Z:III$$7MMMMMM$IM$M~MMMMM$.INMONMO$==+I ......I+  ~$D$I$ .  .N .. M
.........  ....D..$.....N................................................. .+8MNM8,~MMMM$NDM+D8 .MNMD8MD. , I.  ........  ..  I. .$.8OOO~7 M
.........   ...7..$.... Z ................................................... .MMMODMIMMM7MM$ M. =N.?8= :O7I .......      .?. ..,. D  .... M
........       ...$  ...,...................................................... ...8=M7,M$=7Z.?+.  MN~ $ ......... ,.,+MN=:++  ,8?7 ,+.... M
............... ~ .. ...,........................................................,MD=7M:7$M.. DM   N$N.. .......Z :N8~.M,Z $7,?. I7N:.,... M
.....  ..  .... M..,.....D.....................................................M~=.:,  M7M~  ,MM.Z: MD ....  IO.+O,.:,Z,=+,?.M?I . N7  ,.. M
................D..M ....N.................................................OND:DNOO8DMN:..8?+:$ZMO .?:D . 7M?.+I.=8Z8:.,O.....$7~N..7ZN +  M
................+ .M.....M..........................................  .?MOI,~.  ..... I, .8I D.$M.= ,DMZ8O :O7 ID :,:= ........~~7.. DDD ,.M
.................?. .....,......................................  ?M8$?~. ...........:7 8.:M.7 +?.Z..MM :ZM~.7Z,.I........... ..?I7?..,,=: M
.................N .+ ........................................ +,: ................. .O M.~$ .+,,M  ..:M=.?D+ =  ........ ..+$$I~ZDM7 .~=,8M
.................$..M........................................8+~.7:.D..  ........   NMN:D $ .~ .NM :.IO$8? .. ......... =. +:,+?ZII8Z?.D:8MM
.................7.  ..................................... ~=~=:.IZI7=. .Z==I   DD+:~?::+ ~.+$.~Z8=.  MZ  .......... ,. 7N : $I.,?.OD8NNOOMM
................   .......................................D?=:~: .7 D==.,?O~IDO~::O~D7M.I.... .,.Z: . M$ ........8 ?8 +~..8$,:$7, .. +N+M= M
........................................................?8. .  . .,OI7=I, =D..+8D~=,.:$ 7:O: :I. .=...DI.......Z .$..,..~: .+ ........N8$D M
.......................................................D ~:=....... .Z8O7. =D8,~.+O7:8.M   ==+ $ .D+~ MI ?? .I  D ,N..+. . .  .....D7$ND.. M
................................................... ..$..~,+:D8......ZO.$+.,. ........  ++. $  .$ :M:.N?: 7$~.: .O: .........  .NI. ~?:?D  M
....................................................:= ? .,?:,8OD. ....?+ OO.~......  ....: .. .......D. ~  ? . ......... . .,~.,++77  ,O  M
................................................... $+~?..,+:,=.D7~.... .I=O:. +  .=..I:.. ...............................Z. . ........... M
...................................................+....  : =.=:.7Z8~.....+$ID ..: I:. 8=  ............................................... M
..........................................................  ,:.. .. II ....=D8............................................................ M
............................................................   ~..: +~..... 7+~........................................................... M
...................................................................    ....  ~............................................................ M
.......................................................................................................................................... M
.......................................................................................................................................... M
.......................................................................................................................................... M
........................ ............. ...... ...... ... ...... ... ...... ..       .  . ..            ..   ............... ...  . ... M



""")

page27_art = ("""


............................................................I...................................................      ..
........................................................... ZM=................................................,   .. ..
....... ..................................................~+?D8M.............................................. ,........
............. .... ...  . ..  ....  ............. ...... D7$,NMZM ....... ..   ........... .....  ..  ........ ,........
.......                                                .8.MM=D+ ??             : ? .  .=         ,Z       ...~ ,........
......                                7.    .          N8MMM:MNZM8             :..,. =   .      7 +   .   ..~. ,........
.......      .$.      .. ...  ... N +..... ?,.         M88Z O.DMIM+...         ~ :. I.  I ,. .::MI  .=.  ~ . ..8........
.......      .$    ..  :=., . =   .,~  . 8I ..     .  =M.8O$ $8$M.N??II .      :7 I + + .+, ..~~   = D . ~   .=,........
......       .$I...ZN7?.... .:.   ..  I7  .+7.    7ZM.7M=NMM+MNM,8,M NM:7      :N ?..8..     .= . + :,: .:  I ~8........
......      ?7..    ..  ???????~..  ..,..~$Z.+ =DOMM.$NDNMM.DN:D.MM8$MZIO8?....?$.. . ??????????????  . . .. . 8........
......  :+  $MI... .O.~Z77$77IM8....7M?M?ZM7.DMN8MMDMMMNMM=I?7I~MMI8$I=$7MMM..D?? 7?I. $N ?: $ZD~....+7$O ??I$:.. ?,....
...... I:Z .,D  $OO. M~    DM N7?D7 . D?OD$II8M?+?,Z$IDZD8MMO$7M:M$M7Z+8?D8MMMN.ZOND...MNI   M:ZI?Z   IM+MM$  M .$$,:+..
....  :M,7MMMM$D   .  .$N   .:ZM    NM  . M:=IZ DMM?M:I =N7.OMDMM$,M7M$=M M+?MMM . ,,7 ....= .IMD ...,, . ..7MMM,.,MDO..
.......NI.     +DD8:    +,...MD  .N8  .ZM=$DI~$,N8$NNZI .:DOI?N$.+,M M8N?$MD+,ZM$+  .O7~  ~8O $Z7. O$+.   +=.   OM$+:?..
....... NM7  .    .7ID  ..$OIDMII+..:DI,~=,+.MM=:I~. ?~M$D8MZMDM.$.$O.O~~D:77MM MO: ~..$N D.$M.Z D~ .Z.:?ON :NDI. .NM ..
... ..  .D..+88MI .I .MZ,. I,.+O7 NN=M.ND$,ZM=8 ?M?7MMMZ+MM?M+O~O.MMI $7.I=7OZ~,?MZZ....OM87++?O+++ I+D?.  M:.=.88N ....
........  M=I8O.+I7D,  .  .=  .  ..7~:O$8:7M..=?7DMMNIO$?MM$MMDM~M?+MM?. +I:MM+$ =7~~~. .~ ....~7,I:.+ . D7.I7.?7=......
....  . ... N.I= :.D.NIZ+:M,,:,,I8DDMN:MMM,N~7=M8MMZD:M,MD7DZ?MN,Z:7DMMM$D. . ND,N :Z7Z+..OO7.I$D=.$+:: ZIM.N~,=.. . ...
.......    ..IN=NOM==,$Z+ ~I,~.. ~D~MNM.$O+N. DM=$O.8MNM.=NM8MDZMOO7MO8 =+~NZ?:MMO MMI7Z.OZO7.IZ8I.I+ : O+,. ?8:.... ...
........  ..,8?IM+.. ,  ..I7  .  ?,.MNOM$Z M+8$$,~Z+MM7,8OIOOM$M$MNM??~?Z8=MM  .7M$$MI7$.ZZ?7.:ZI? $+., O?:. M8,........
........  .. N:::...+:.=DMNMMMMNNMMDZ NN?MMNMNMM8MO$Z... 8I DMIZ+7 7MMM8?..:,M? ~$MMM,+Z..N. = +  ~.7,.,.7  :D8,  ..    
....  .   ..=.DMZ~ I.7 .7  ..... Z DM8$MN$MIDMMDD8ZI8~M.:OZMDMMM.? ZM8I=88=D7OM:8M MN8MMM8O~Z+~8 ,D,I~~:~~NM8~~:   .. ..
....  .  .  8N,M~.I =. ? ...... + .DN~N~MM+8D:++ ?.,8DZM:~O7NM~=+MM$,DODIMM, O?DM7:M,~,,~..=,~  ..=  ,.. .:  :.~........
.........   .I8M+ ?:..:. .    .,. .+M=?~MZNMN7ZZ.M.INO7,MO:8MM8M~7DM7D:. ,NM$:+MOMDMN8.I :.. . 8 .$+,8$   ..I  ,....    
....  ..    .8 M  O . .$ .  ..:..: :=8M,M?$N=.=M:.O MM=7MMI+IO888~.?MM8, ,=~?DOIZ8Z:O,I  ... .~+, , ..7.  ,. .I,.... .  
.......   .. ??M..7 .  .   . : . . D ?ND?Z,:D7Z$N,.+,MN::+,?MMOM M:IN,:NZ+NOM,N~DM:.8  =..... ,7.8 . ? ...:  M ,  .     
.......     .N M..7 ....... ..~....N:=$M?MD,~MNMD+MM~. N8Z..NM?M+MD$,MO..MM.+O$M M,M  . .... ,..O . . ... ,N D ,        
....     ....?.,..7...... ..   ...ZNM~$D+NMZ8I?=OM +DM.NMMM7MM:I8?MMOMND$M~DM.8 MMMM.  .....I   ..........D ?D ,   . .  
........  ...?NN  I. ,..  ....  .,=,Z8MM$M.N.,Z+D$Z  M.:OI7MMN ZO$NI.MMNID~,IMMDM$~M. .=.. =.  ........ .,:,ID.,  ....  
.......      8., :,..   .~. . . , .:MDNM MMODM7,+.+IDMMM?Z+M8.:MN? . M MMNOMM88 MNM., . .. . .    . ... 7.8..D.:  ..    
........ ....=.,~ . .  . . ....:...D7??::M$8M:O~M?,MMM.MMM$MMNNMOIZMNM.88DMDOZMMM.+ I.. =..:..    .... ?.7+ .,.,.... .  
....  . . ...  O :7......  ...$... ~DM?MDOM.8.MDDZ87:=$MM8I,M.MM+MDN:OMM.,,8M+DM:$ = ..?..... ........~.:....D~,  .. .  
....     ...  I,~.7 .   .  I.:..  .,MM$M?MM 87OMDO?M=~.:N.$,O,$$8?MN~D?DMM=.O=+MM.  ..?  : . ,... . ...7   . M.,   . .  
........  .. . ,  ,.. ..  D  .. ..,Z.=,O$7M=~MM$:.DM= 7.++.MD 8Z.I,$7NMM$Z+NZ=D:N.   .  Z ....    . ~ $.Z   D8 ,....  ..
........    ...,  I.  . .    Z  .? . M$8?M8MM7:Z M .... Z ...   ..  +DNNMM==M+ZM,. .. .=.. .       , $  .   ?.O,....  ..
.......     ,.N.  +:... ~   +   .   7.MM$ OM?DMMI..      .7++.  .. .=.MZDDMM?MMD. =..        .   .. .?      +D:,  .. ...
.......     ,: .  ,...     .     . : .NN.N,:8:=~  .    ,. ?? . .:,.  , 8IIMMONM.    ..          ..   +Z     .8 ,   .    
.......     ,~ .   .  =   . ..       ..$M?M$7..Z .    =$I$ .$..        .M8+MMDD   .    .?      .,  .Z.     N :.,.. ..   
.......     , .  ..  ~    ?    ~     7 M8OMDI.. ?77I7MMMO ..N.Z.MMM8+.. +D=M+7+.. ...     =~  .?.  $.~.  .: I7=,......  
.......     , . 7 ..:    .    +..   ? 7N$.MO:         ,,.,  ..,~=NO7.    ZM.$ ?  ,    ,  ,I   +   $.8.   ..  ,D,   . .  
.......     ,  $ . ,  .?     I       :OM=MMZ.:.. D.MNM=$ Z  8.=OMMM  I .7==Z..O .      ..~  .?  .7 Z     Z Z D8,........
.......     , ? I. .  : .       ..  I= MZI:,~. O  MMMMMO+M  NM.MMNMM  =:M$=,  + .       ,    .     .    . =  N=,......  
....        M+ N. :  . :    ,I,:.  :=..$=+,8ZDN8, $MMM7ZMO   :$MMMM?~MM..= O  ++      .    ..  7.7.    .. ..ID.,.....   
.......   ..M.~  +. ..... ..,     .=  .?.Z Z,..O.~77$7MI .    D7N7I$I,,.  DI~.Z    8.+ 7  :. .=.8     .. + .~D+,   ...  
.......     N I =.  =  ,? ~ZZ$OZ8NNMMNODMM=M. ..+. .$=N 8     .8.=.. 8    Z$. =  .~.$. : D, .Z D.     , ~. ,?$=,.. .....
....  .     N=MM. ?IMMOMDD.7.~.7~OD7M7MIII. ?   . $.  . ?   .,..M.M8      D. ?87.O I ..  .. ? I     ...~. IM?N.,   .. ..
.......   ..M8 I=D M M ?.87M.~ I7N8~M M.? MD~:..     MZ.~8:$8,M? 7       O D.?+MMDZM~M.M,D.M.. M Z,8+ZMOMM+M.7.Z ....   
.......     NM M.7+M M.D.M 7 :,I7=M~+OM.MI:M$I:I . IZ..   ..  . .IM.  .,MM=:$O.:.I.8.7.M,D.M.M.M:8:?+ N+OZDM7M=N.    .  
.......     ?M M ~ M N.MD~.7 :~7I,7 ?.$MM$M7+IN ,. Z..  77=7DMM$7M.?   .O87~ZO.~ 8.8 I.M,?.M.M ?~ZDI+.D+OZD 7M~,   . .  
.......      M M:M.?.N M : 7,M:7I,:.?.$M?MMM=M~=, .+.M=.. +. . ?O. $  ~?=I$D~=.:.7.8.I.?.+ ~ M ?~8D?+.D+$.D.MM~,.. ..   
.......     N?$MIO +.NZM ~ I.N,7Z,~+$ $NZ= ONZ7M.     ~ZM7  .O8?,      MDO+$M7Z: I M I ?.+ M N ?~$DM+=N+M.M MD=,..... ..
.......     N? I,M +.8.M. .I?D.77,~.$?8M=  87~ZO$       O=.~Z7M.      $NM$8?O++:.I N I.?.+.O?M++~NDM+ZN+=.M ZDO,        
.......     N?7,,M ?.D.: :M,MZOIDOOZDO+I$=D. N8=,~D.     .ZZ+..    $.,+N=$+DD.M..,N~.7,.:O7,,,,,$N,,. D ~.    M7        
.......   . D. Z...:.D777MMMMMDZMMMMMD$$M$M..7?,=?.ZIM=...    .. DM$?.~=7$7D+MMM?.7  7~.?:+    +7. ..:,=+??NMN N    .   
.......  . 8.?MMZ. = I  .. ..?   :. ,+..=ZN.II.O$. ? .8MM7D.+78IOMM.+ ON MD~MMN:IMM.?8.7.,. .?.:   D  :. ~...D.8.....   
.......   .   M.  ,..   ,  .=  ? ..$7..MMMMZM78.N7N   $NOZ7$M~M=NM .+M.O$:MMOMNDNMMMMIM.:  , .I.  ,.7Z.     ID 8....    
.......     .~$   ,....: .     .  ~ ZMNOMMMDM+$O+:I:..  DMZ7?:D8M?Z?MM+M+MIIMNOM=8MDMM++DMD  .     ., , :.   =88......  
.......    .  I  $..~   :       .,M+=MM+ODNO8NMM,~,,N. ..+NMMMI?=?8$M NN$NM+IODMM$~MD7DMN~8IZ8,N8 . O: , ,   M 8        
.......    ..  .~. :  .$..   7:MMIO$N,NMMZMOIMMIMMN,, DZ.OMMMMM88N, MMDM+?D+8M7DOZI8OZDM?DNZ +D~DO.~ .. ~.  :8 8.. ..   
.......    .  $ . :.        M7O~8+Z$MN:MM~M8MM~MDM+MMMM,MOMMNMM N=MMMMM$8ND8D$D$M?M?M7O=$N8MZM8 I+I  . + .  .8~8   . .  
.......    . ,: :  . .  M,+N~$?$NZ?D$DMOMZMMNNZMD~MNMM?MMN$MNMMIZM:MDMM8M?N~7+IMM7D8N?DIN8?MM=. DN8,..      .M 8.. . .  
...   .    . ... . .   .M  M,:O87:=7?D..M7M,M7M8+M8$D=78MMMMMM+M7NZ??M~MON78M7+M+D+~NZM+NMNM.M.Z.,.Z~N   ~  ID 8..... ..
.......   .Z   .   . ~ .=M.  N8?7M:N?M?M$$M?NM?O+MMM:.NMM+MMMMD$M$,$ZMMNIZMNZM.D.7M:N7IMM~MMI  ?. .. M. O. N ~ :..... ..
.......    Z . .  ..., .+~N.. :MMM,8+??M7IDM IIMM$ZZ=M.MDM7MMMMMMMNM?MND?MMN7OM,MI=~MMMOMMM=  I .   $ :Z  .  :.:   . .  
.......    $.      .N     .N. :7N$DM7~MM+===N,MDD??Z8:$,88$MMMMMMMO??D:N?IMO+$M:D7:8N$IMM+M~ M,     ,=D. .. 7:O,  .. .  
.......    $  .    ,       +O.:,DNM=ZNINMM+?878+M+?DMMMMD?MZMMMMM7M$7DMMMMZNMOIM~M:?Z?$IDM .N..$     Z, .+   :Z:.... .  
.......    $       Z     N.  :,?,M~O$~.N$,NN~$N+:$DDM,7MMOMZMM8$MMMD7:~MIMMDOM,NN$+DN$IM+= $8.I.      .N:.Z ,, ,... .   
.......    $   .  .=     D.    Z.=I??M~M?7M?,M$~+I?7:MZM8MMN8DDM=NMD$MM?IM7=N8ND.I:M8.M8N.M  .+       O.~?. , .,.. . .  
....  .    7Z ..  ...... ..     ...$$~?,7IN7:I~8NI$=M,:DMNMM~DDMMMMMN,NM??O~$DNDO7,M=N.7 D7. 8 ..     8.M..,..O:..  ..  
....       ?.    .I.       .   .~,Z.,8?NMZO?N:NN~Z$$~MNNMNZMM.:+M$:IMMM=MOZMIM=ZN7M=N.7 DZ .$.,.      : ~. ,. =D  .. .  
.......    +~,..+.         I       ,:.$NZIMM+7?,8I.M~ MMM87$O...D+~N+D8MZMM=M+I8M7:Z~. + . O 8         N.N.   .,..  .   
.......    +. .,.N..        :       7$  M?N=OI?==.M+,NMM8M77M  Z=MN$$~N=?M=D?MM:MMD8.?Z    .M.          $,  + O,   . .  
.......    +    . ..  ..    .I   ....I M..IZ==+.7ZZ$INM$88OOM..ZMD Z?$$MIDOIDMM8,~. D..   O8            ~ Z. +.,  .. .  
.......    +  .   I           8        .,, .:D$8?$D=O=MMMD$8N. M7MMNZNM~MNDM+MO ..~=8 =  .D.            . .... :   . .  
.......   .+  . ..$. ....  ... 7,...  . .I~~ .? OI?8+:$DDIIZM .M.N+I??~87:ND:OO..I7, .., 8,.          .  , :,  8........
.......    .  ..........  .   ..:,.....    7:$.. ?,+MM7MMMD7=. ? 8M MDO8N=...7.?+.  ..   DZ . ...   ..   ? M . 8  ......
.......       .   $   ..        NZ           + NM..  .$NM87I  .+.7O?=DD=     M~         .D:.               M       .    
.......   ..      ..            .,        . .  .+~D.    7DOM.  M +.+.   ..DI7..         .:=  .           +     ... .....
........ ...  .......         . .=.             . I ~O+M. .?   $.I. . IO =.             ..   .           O     .  .. ...
....... .     ..   .. .. .      ...             .    . O,?D,.  .,,.:.O, ..                .=                    .... .  
... ...           .   .. .                                      ..                        O:                   .  ......
.......           ..  ..  .                                                               .                    .   . .  
.......   ... ......  ..... ..  ....   .  . ..  ..  ... ....  .   .. .  ......  ..  ...    .....  . ........  .    . .  
........      ..   ..                     .      .      . ...             .         .      .                .   .. .    
....              ...                                                                                              .  

""")


page30_art = ("""



   .  ..................... ..................................................................  ........................
      ........ ...  ~7Z+?IIIIIIII~IIIIIIIIIIII=III?IIIIIIIIIIII7IIII?IIIIIIIII?IIIIIIII?~IIII..=I.....:,....~???  ...   
. .    ..   . . II:NI. .  .          .     .      .         ..     .   .. . . .  . .                        . .         
 .    ...   .~ 8... ..:=MO.8.O ...OOOZOOOOOZOOOOOO=........,... .+................... O..... Z...... ......  . .  . ..  
   .  .... $7 ..  ~I~ .. .M .Z ...............  , ...... :  ., ~ $ .   ... ...... ... .I..  .....I.... ~.I: . ..... ..  
       ..?=,  .,Z.  ....:.N Z ,. N    ,..... .,  .: ..   +  .$...., I..    .....: ..... .. ... +  .:..=.,I. ........ ...
   .   ,.....+, ........ ON.==+$...:I~.... 7+ ... ..,.  .$..... 8 ~?I... . .. . .............8   . .D. ..... ...  . ..  
.  .  8M, .:,      .  .. =  .7 7.$..~D..... . ..... ...M.   . +..... ?...I: .  . ... ...... .....~M.......... ..  ..  ..
.   .?$...8 . .    ...??,O.7?..= +     8=.  +.     N..:.~.:   .. .    . D .... .. ..... .. .. ....=   $.I. .. ..        
.   :,..    .   ..  +.  I= 8D~...   ~ .. .=  .   I ~  . ,?..,.,: .~= . . .  .  .. .. ..    ...O$~8..    MI..  .         
     . ~..  ..    N .. .$....  ZZ +M    . .~.   .,Z:  +M. ,.:..   .  ~.?  :    .O .. ...+ . ...   ....,: :... ..  .  .  
...   I.    . .  + .  . ?.~..... ~, . .M.. ~  .....7...+..7 +   .7~.IO. : .... .. ....~~..$..   ~.    .. +   ..   ....  
:,.  Z  .          .....Z ~.  =, .... , I . ,,+  +N... N: ~..,$?,:  .    ... . .  . Z~ .  ..... ::, ...  + ,.:.         
,.  Z ......  . ......?$,.. ,  ...,,. ,.....,.,.7. :  :~D8M8N~:,,I :. 7 .. Z  :=..I .....     ~. .? .,...: .+= .... ..  
...8  ....  .. .  .. . ? 8..   ...,D.....  .....IMMMO7MMMM7+M$.MN:I~.....?.?  , .... ...: . .?  +.  . .,.+ O :..  . ....
. O.  .  .  . . .. ....Z., ....=. .. . .: ... =MZ?ZZ.?D?M8NNM=N8~MM+  =:.  ....... . ...... . .. ...  .. +.Z I .  .  ...
.I    .. .  .      ... +  .7 .= ... .. :   OMMMM8NM=M,MMMMMODMMOMMMMMM  .,   ..:.....  . .~. . . ...   8.+ 8.     . ..  
..    . ..         . .Z.= ..   .7. ..7  :8I,NOZ8NMDMM?MMMMMN8DODMMMMMMMZ..7.== ZZ ..   ~. $. ~.+.. +.~.:.+ :. 7   .  .  
.. .  .  .    . ..... 7.Z .... ...+N.  8==I=N,:N+IMMMMMMMM~O~8 N$MMMMMMDD.  ,.DO..    ,  I.,I.., .  .. .. .,  ..        
.     ...   .      ...7., ....  ..  . D.$++ 7N  ,MZMOMMMM8N~NON?:MMN7N$MMN     D.M  I... ..  ~:,... 7... ?  .           
.     ... .... .   . N. . .. . .:.  .8.+I.,DIZZO+MI+.MNM,I.?8=~Z8DMD$=DIMMDM..D:$.,   Z ~. , .  .....   M...   ....  .  
.     .   ..    I: . = $...Z,, . ,~ .:NI,:O?MD.I~8N,MMMD8.+O=D~=,7OD.DM?M7MZ  Z .7.  D=  .:....,O+. ... ..  . .   .  .  
.     .         .    M.+Z,... ....7 7$OM$NIM7,=$?Z=MNM77I+,8ZO MMM~I.MM N~$M..D,. ..... D  ~8,  I ........  .     .     
      . .    .  .. .,,.. . ...:?$ .. OM:8,MDM.D$NM+M7NO$,ZDDZ M8M8 MIZMOO?MM.. .. ..  ..,8    ? 7...~ .......           
.  .    ..... . ..  $.I.. .. .O.+M..:~M,MMM,$8$DM~M.$8?N?II~Z=+:Z ,,+=NMN+OM........ ......Z. .+........................
.  .....  ..  .    ID I  .. I +.  ,.~MM7OM:8NDOM?D~O.=ZZ=8.N?~$8.?.?M=MDZ$MM   .  .. .. ,I ...  . ..  . ..      ..   .  
      ....  .      M7 .Z .Z.   . .  .:MIMMM=D$OZM8M+8??M,M$$+M$=.7NMZMM:=DMO.. .  ..   .  .   . 7 ..  .. ....           
.     ..        ...M.,. .  .,N+~  ...NN=M8MMM8MMMIMNZMMNM$MM=88N.M,?MM7$MM+... .. :N   .MM.?  .. ............  ....  ...
      ... ... . . .? N,. $D. ,NNNN.. DMMMMMMMMMMMMINIMNM8$NOMIMMDNMMI~MMD  ...... : 7:.N..,  ,...............  .  ....  
  ....... ... +   D= ,.  ?Z.:$=M$M.IMMZ.MMMMMMMZ,++ZMDMMMMM$ 7$OI7I8= I.  +8$7II.7~. 7   I  ........ .    ... ..  .     
      .........   M :.==Z:    M$$MI78MM78MMMMN8MMMMMMMMMMMMD8MMM$ .  .MMIIII?IIIIMDM..MMMMM8MM777777777777..            
MMMMNIMM???????+??N.8M+D? 7$~Z8IZMMMZ,~:IMMMNN87?8M+MMMMMMMMMMM.  .   ~ 7  . +?  ..  .8 ...   ..............  ..  .  .  
:7?   .. .  ... OOOM...$+M$N.=8M8.~M:MNMMMMMMNM7MMN=~MMMMDNMM  M.... M~~~~~~MMMMMO8  .~7OOO8,..........,,..   ..  .. ...
..:.D+NND$$$$$$$ZOZ+.  .,++7?$.:.~N7ODM?$+MMMMO$I887DMMMOMM7Z,$.....$......... ..  , . ...       . ..... .   ...........
Z,,,. $         =7,Z~.?.8.D,= +?Z+88MD8M: :NOMO.  ZNMNN+N, .. .....D+?+++, ?~=NNNNN  .  7DNO~~~=.~~===~~==~:............
. ..  NM:,,,,,,O D,?,N 7=MM.NI$DDMD:?~N+?M.  .MI: ,+ZNM: .........$      .~ , ....8 ... ,...............................
........  M ....... M,IZ:M.Z=ZMMDMM.  7 M,M.M.... .~ZN7M8M...... =.............D.?O.....   .............................
..........  . ?~... ONMMNZ?MMM:..I?,$....:II$?7DN .=$N7.8$O7 ...$...........$.... .......Z ........ ..   ...............
............. :7+=.D IMI?MZM8   .7 7 I.,...:.7M?  .=ZN  ... DIMMMMMMOI77?I777$ .........:77. ..   ..II ?.~..............
.............NNM?MMMIN?Z..MN:D... D,.,N  O.  :..........   . ON..~~..D,.. O...+  ...... $ 8?. ??..I8.O+  + .............
.................,,M+,M.IMD  ~7 ....+.8:: :Z  +....... :~$, +=N..++ . ....O7...O:.......   +. 7? :+. O  . .~............
............... .. ..Z=M= II,+=Z..  . ~:,I+O ZI.... ~D$O~..Z+=.7.+, .+: ... ...~$    ..=.. M  7 .ZI  7~..+.:............
....  ....... .......  Z=...,$.+$8..... ~?N. .....I.:N7. =OZ.Z,?,I ..M7. .Z...?. .....:~..:=  7..,M .~$  +.... .........
.................. ...  ,IO...==~OZ+  ...,.. ... ,7...  .,...:..:M, ... ..~...........7+..  ..I . 7 ..O .?  ............
.............. . ..... +ZIZI.....7.I~ Z... ....ZN::?.,   ..... .. MMMMMMMMMMMMMM7 ....?77I8Z..I . O ..+ .+?... .... .   
.............. ... ......=+$?8....+.Z.$7ZM,...   .  ,,.......= ZD~N$Z$ZZ$Z$$$ZZZ..... 7Z...?I:? . :...:.7OD.............
............... ..............+77  .++7?$?,.   Z +:..... ~ ,++:Z=:ZZ .   .....    ..  ........I ......+.=ZD.............
.......................... .......~.... +~M..+ZD  .......=: +=:7.,N?M ........~.......:.......... I.....ZZD.............
.........................  .   .N7 D,....,DMI=?+ ...  , .? Z+~    .. .. ...... ...... :::::::.., ZM...,..ZD.............
................................. :, M8.=~MZ$8.......,IM$O8.......,MMMDOOOOOZN ......8OOMMMMOZ7 .,7. .$.. + ............
..................................  .=?.D?INZD.... ~...+8..... .~+ ,MMI..$..  ... .. NZ..+$..O. ..I. .Z.. : ............
.......................................  .O$NO....?.:..~.....=:7.~ .,?~ :. . ........., O$8.Z: ..Z ... . .: ............
............................................ZM... $.+.. .. Z+Z . ... I  . . . ....... ...... ,. .+...... ...............
........................................ :IM$NM 7.$O= ...$,.$7 .......+.............= .... ..:...+ . +  ................
..........................................,,Z: .8O?.....O$~$~......... :.?~..............~,..?...Z.. :.. +..............
............................................    ...8....,M : .......... .7.......................I..  ...=..............
.................................................. ..M$ :...............~,............ .................................
......................................................:,:......................... .....................................
................................ .  ........~=,,.  .~~MN~.,.......................:. .............. ......  ............
.......................... ........................... .$+ .$ .   ..............  .. ...............................  ..
......................... ...... .... ............. ........=. 7+    ... . ... .  .. ........ .....   ............  ....
.................................................................,: ............I.........................  ............
......................... ...... ..... .  ....  .............. ... O ......... ~..... ..  .. ...... ........  . .. .. ..
............... ......  ........ ..............................................  ... .....................  ............
........................................................................... :I ................................ ... ....
.............. ................. .  ....  ... ..................... .......... . ... ...   .................. ..........
 .....   .  ..  ....  .. ....... .  .. ................................. .. .. .     . .   .  ..... ... .   ......... ..""")


page35_art = ("""


... .. .............................................................. ......... ...... ............ ......... ...... ...
................................................. ......................................................................
 .........   .. ..................... . ... ..  .. .... ..   .. ...   ..  .   .  .               .  ..  .   .  .        
 .................................... .......... .. ... ..  ....... ..  .. ... .. ............... ..  .. ... .. ........
 .................................... ..  ...... .. ............... ..  .. ... .. ...  .   .  ... ..  .. ... .. ...  .  
.......... I ...........................................................................................................
  .   .....M....=M, ....................................................................................................
............ .. M?.:M: .................................................................................................
. ........  ~  .MM .. IO+...............................................................................................
 ...........N ..DM .:8+...8~............................................................................................
............8...=MZ .OI8=, ..N7. .......................................................................................
........  ... .. MO .Z?+O,M7~..+Z?. ....................................................................................
.............?.. $M. :7M .  N:Z8:  I7...  .. ... ...... ..   .. .... .  ...... ...... ..............  ...... ...... ....
........ ,...M ...8.. MD......=M$.   O=O,. .............................................................................
.........N...+.. .OM..$+..:Z. ...Z IOD~..MN.  ..........................................................................
.........D....+...MM  :?= :M.$Z=... $M7. M  .N~ ........................................................................
 ........,..... ..=M= .IZ. M   7=8.....Z7M.,.. .,?  .... .   .. ..  ..  .. ... .. ...  .   .. ... ..  .. ... .. ...  .  
 .........+ ..Z ...MM..+8M M=  ,. .:N, . ..MMD?  D.Z7.  ..  ... ... ..  .. ... .. ... ....... ... ..  .. ... .. ... ....
..........M .. ....MO. :+...M. 7..  . +Z.?   +$78M    +N..   ..   . ..  .. ... .. ... ..   .. ... ..  .. ... .. ... ..  
......... O... 7...DD,..8.: M:.$... ...  =D~ .  ,?.?N .$.?N: ...........................................................
. ........ ....?....MZ..~M$ 8M 7. 8.O,  .+  ~8. ...:D $M.=. ~8: . ......................................................
.......... ~ ...... MM.. ND. : ...~: M?,~+   .. I~.. .,:MM.8~ N.I+,.....................................................
.......... M . .,...$?:..N . N+7.. M$. MD?.M:....  NO... =N  Z= ..,NM...................................................
............... 7 .. O8 ..~D..O7.. O:~?+8=MM8~~ .....,I: =...8?~8:,.  :8,  .............................................
. ....... .., ..: .. NN  .7M..O7. ..MN~ .+$ $$~  .+    =.Z7   .. +~OM,....O?............................................
............:....... DM,...M= Z7....M.IM?N  .~78,MMMM?. .+  DM ...,7M,MM, .. N=.........................................
 ...... . ..$ .. +.  =M7  : ,..M    I, Z  ,~....DM:.D 78 =   ..,~. ...?IN. : ..M8+... ..    . ...  .  .. ... .. ... ..  
. ....... .. ..   ..  M8.. ?8: M= ...MM?,8 ZM7  MM =? .+OMI.. . ..IO?:   $~~ 8,M  +7M,..   .. ...  .  .. ... .. ... ..  
............ ?.. . ...8M.. 7$  MN...?M ~NDI,MDMI?MI . O+ =.IMM?......ZN=...?. .MI$+....8+ ..............................
.............M........:DO...MM MN... ~DZ:+DN~~?:MMM.=~ OMMM~M.M?M,...=..+8:?...M..ND, .   8~ ...........................
 ............ =...~ .. ZM,..D$O:MM...8~ON.M. .=ND:MMZ..~.~Z. .~~.O? .O.  ...?$ ?. Z+M DZ7. ..?M+........................
..........  .. ....,... M$..?I7 ~O.... $IMI.M I8 M~M..7OM .$N :I ,.M.MM    .   ID  .I.IZ8~.I....?8+. ...................
........ .        .N ...MN   Z+ :M.. . MN.M.M$M:. ?..N+ZZ=  ..:?.=~ .DM:M,M.   .. +O. ...: D=.Z    .=O...... .. ... ..  
.............. ..... ...MM . ,N, IM .,.,O.N ..M..+MM?M,=?.   .M,.D+M M7$7...  .......,M=....,MD?+D  . OM~...............
 ...  ..        ..., ...~DD ..M::.M     DMD M:$~.$M?..M8ODMM  87+~+Z.D~... .    ...,MMM    OM$?:,  .NMM+ ... .. ... ..  
 .......       I  . ?....ND ..=N~.M=   .=NM D,.O8IZM:DM?:DD7 ~~. OZ: O.... .M  .ODOD  .  D+: ...:OOMD:.. ... .. ... ..  
..............  .... ....DM...7+N ~N ... ZMM8. ?M7.:=DND$ D:~.M8$. ..8  ....M ZMM:.:.8M+DN  . 8MMMO .......7 ...........
  ........  .  .. ... .. D:N...MM .+.   .+D .M?DM N .  N7M8~.~. ..  .O  ...~MM:.Z .8,MM.   :MMM7. ..  ...M.  .. ... ..  
............... . ........MM...$I.8O7,.. .MNM . $M.I8  +M?8 ..~~...... .Z8M.M .:N~7N, ..$NMMD.  .... :D .. .~8..........
................+... :....M8...7= ..D,....M8  ?:$ID:.ZDO, ....~~.... ~IOI ..M:,+8= ..:MMMD,. ......8~,...,Z,  ..........
.....................+ ...:M=...MM. M,....M,.Z. +M~ZN. .......~=..+877. .II7MZ,.$ 7MMDM~....... $I ... 7,...............
.................I... ~ ...~M.. MM8 I8....M~D  $ M~...........~+7?D... M,N. M..:M+IM:........:8 .. .:  .................
. ....... ... ...... .   ..MD:..8$D.I:    MMO:O8.$ .    .   .D88+  .OIDND ? =M8+M$.........M? ... 8.  ..................
 ...... . ...... ..   Z.  . ?7. M7?  8+   N.7          + .7ZI:~~~D..I. . :ZNIM7.. ... . I7. .. Z?  .  .. ... .. ... ..  
......................: ... ZM  NO$~I~Z...M......+.... $MM. ..$M$IZ I ~NMMZ7  ...... I$ .....  .........................
. ......    .     .  ..7....M:. NI D  N.  .. .     .:DMN  .+MM:~  . MM$?M..... .. :M ...   .    .  .  .. ... .. ... ..  
..................:....7 .. O7+.N.7D? 8$.........$N$I..+7 ,~I   .7NI77. ........8: . ..?  ..............................
. ........  .. .... ...I.....MM +.~$  .8....7 +N88...D~MI+?~  7M~NM~ ........7I ... 7  .................................
 ........................... M8 Z $Z8. M    7MO, ~:+ MM+. .$M:MMI,........~7 ....,?.....................................
. .................N....O...  ?7$...I  MONMMM  O$ ,N.  +IM,=M,  ...... 77. ...:~........................................
........................D.....MMZ..O ...N= .MI:7+... IM7IM+.......   D... ..............................................
 ........ ... ......+...= . ..MN+. 7MD  =?8:D :,  ~8ZMN~.       .:$,..  ..,... .. ........ .. ... ..  .. ... .. ........
........ .  .. .....?....:....ZMD...M~D~OND:M..,DMDM, ... ...  8, ....8... ... ........... .. ... ..  .. ... ...........
.. .......  .  .  ..$....8.... NMI..M8DI.+..MMO:NM  ..  .   .,. .. .....................................................
..........  .. ..... ....D ....MM:  7.. .78:MM8  ...... .:  ....:Z .....................................................
..........  .. ................7MM. 7 ,8NDMD: ........:,, .. .................................... ......................
  .................. Z....D.....MM..MM7?M.. ....... N . ....,...........................................................
..........  .. ......+ ...:.....M$M=$N................. ................................................................
. ........  .. .  ....: ..:.....OMM:..  ..  . I:.  .... . ... ..  ......................................................
......................=.......... . ...... .. ..........................................................................
.............. ...... O ...M.......... .+ ..............................................................................
 ...... . ......  .  ..   . ... .     D                              .  .. ... .. ... ..    . ...  .  .. ... .. ... ..  
.......................~ ...=.......  ..................................................................................
. ......    .     .. . . .. ~ . .  .      .  .   .  ..  .       ..   .  .. ... .. ... ..    .   .  .  .. ... .. ... ..  
. ........  .. .............O.......... ......  ...... .. ... ..........................................................
. ........  .. .........................................................................................................
 .......................................................................................................................
........................................................................................................................
........................................................................................................................
 ........ ... ...... ... .. ... .         .   ..      .              .  .. ... .. ........ .. ... ..  .. ... .. ........
........ .  .. ................ ................ ........ ... ........  .. ... ........... .. ... ..  .. ... ...........


""")

page41_art = ("""

. .............O................,$...............M             ... . ...    ..~8~~~+Z8,,,8Z,,.       ,,                M
..............,Z............... O .............. 8 ...        ..?..  ..... .   ~7.... . .   D8MD.DDMO$+ .              M
..............  ... ...........:8...............?   ..          ~        .      M               .I .. ,8O~,7D:         M
........  .. Z:.        ..  ?7$~MMMM8N$MMMMMMOMM+. .?$$$MMMMMM ~.$MI???~..  ..  M   .............O ..........=7M ......M
....... . .$N.~,::: .. ZDM::, .   .... O  ............Z ............. .?   .:::M8  :N~. .........7............. O7.....M
... ++++.      .     :. ..............+......... .....Z ...............$ .......... . ..+=$M$ZZI,,M,...................M
.. ..... ..... .... :,................M ........ ....., .............. ? ............... O.......MM.. MN.. .. ...$.....M
.  ....  .   ...  . M.... ....... ..  ?...............Z .............. ,..................$............ 8DO+~Z?..I ....M
........ ..........+: ......   .  ...=Z   . ..........$$................D ................Z.............=N . . 8?O  ...M
,...... ..  .. ....,.   O8888MD~==~M8O8O8O,OOMO.OOMO8OO88OOO8O,....~ ==,  =+N88O8.........D ............ N.............M
+.. ...I7M$7MIIMMII:  . ... N. .. ............IO............... O .............IM+   IIMMMMI+.   .. .....:.............M
,MM.... ~D  ....... ...... .+ ................I ............... M .......... Z     ,MMM+... .=M:,MM.+MM: D. ...........M
........N ..................N ............... Z  ...............M............? .........    D=.Z....    =+O,+O.........M
 . ....:= .... .... . ..... ...........   .. .7. .............. O .......... ,............. +..Z ............ .8:8=~...M
.......O ... . .   ......  = . .     ...... $$=M7$$.$$ .. .   . O. .  ...... =..............+. Z,$ .............  +.+ .M
 .  .. $.    . .   ... .  ~DMMMMMD8Z$M$$..  .   ...   $?MMMMMMMMMMMMMM~$$$7 ON$7............+ .8.7................8 ...M
 .. .DM .::DDDDDMM=:  .  ...:DDDDMM.....  .   .. ......M .............+ ..M=?Z$.7~=M=MMNDD. =NDDMM8.. .. .........+~...M
$M?:  . .......M=       ......... M,7..................M..............:.. M:7D$O+.Z:..~=MM~?+$ZI... $OD7,M$.. ..... ...M
 . ............ZO.. . ........... 7 +..................M..............:.. M  O 8I.Z :.+MM$......... ,.... .,D=O~  .:...M
.  .  .. .  ..... ...    ...   .. . $ . ... .... ......M..............:.. :.I, M  D.D :.Z.......... ~.......  ..7?..O..M
 .........  .. I...............?+ .7=7$M?????+~M8I???IM ..?$$$$:??????I:??:. , ~..N : ,.? ..........O .............  :.M
   ..... .....I  . .Z$O.+....:ZMM=    ,.......M...........     .M,....?~. 8. , 8..:...N ?  .  ......Z..................M
.     . ..?ZMMM . $M?I ...I ..    ..      .  .M. ............... ,.... .. M O. ~..:...77MO. :8IIMMMM.M$ ...............M
.:D8NMD:..  ....  ...   .=7...... ......  ....$ .............~...,....... N.7..=.::.:~ZO?... O........~8OO:N8,. .......M
O. .: ....  .  8~O$  ....~ .  ...  .  ..  ..  N...  ...  . ..~   O ....   NM . =I....~.~?  ..Z............ +==7:~M:. ..M
 ..:8 ...................+.......+?==7$M???MMZZZ,,,,.,:.....,I,7ZMN+??+N,.DO  ?~M. N, ,O ~ . Z...........M N .$~.......M
.  7  ......... ..  ....7N=I7?I:   Z$.................?......8......... ..N~..8.D. DIM777M7MIII+  ..  . .N.N......I, ..M
.. I........7OI7:77III. . .......M..$.................?......,......... ..N$.== M7:7.....=.... . ~I7M?7I.DID+..........M
   =$O?$M=    O   . .   ...    . ,..$..   ...... .....? ......: ....... ..NN?N+MI. ......=..........  D 7+O8,+ ........M
MMD. ... .....M ...........   ..Z. Z$...... .... ...,,? ...... D....... D N M   .........=............+ .D ..N? $......M
   ..... .....+.  . . .... . .~. , NI =:?+NZ8888:,,::..O.NN. O8O,.~~. ,, .O...........:Z.DD~    . ....? .+.......,O+,  M
.............:O.......... ZI+7MZ$.  .. ...7+,     ..  ....,Z ........ .D. ..............8.M=+= ~MMMM8M$. 7ZZ,. ....8M.OM
.............ZM.~7?MMZ.,~ $ .. .................... .....I  .. ....?~ ,...........I.... 8,... . .. .?....$+?:$~. , =M  M
...... ..~:,Z8.I. $?,..................................I+.?.. .......8...................... ...  N.....  ?+7. ?N$?$D .M
....  ,M8.ZD....  ~ ............................... ..   . .,. .... . .. ...... ....     ... ... , ............. $  M.,M
+,8N ?=. ...........D:, ............................=. Z  ..~ .....:..... . ..? .... ... . ..  . + .........,88 ...~   M
 :D .................$ ...+ ... ...... .. =..  . .. ..    .. .  ...+ .. ...... . ... .+8O...  ... .............:. .... M
......................I:... ,,  ..I. .,8MO~NMMMM......=.. .=.. $I ........ .  ............  ...?.. ............ ...... M
.....................I. O..........+..~DIM$7MMDMM .  ............?MI ..........O........MDI ..... . .............7.... M
....................O...  ........... MOMNM MIN,$..  . . ....  .  .    M.. ...$ ..   ...   . ... .. ........... $ .... M
8 ................. ~................+M8MZOZI .DMM~... .  .................   ..................  . ......IO O?$...... M
...I .............. .................DZ= .  . :  M....... ...~........  .... 7..........  .. ...................I......M
..   ::........................... ,I8NM.~NI 7M+MM?:.  . ....  ......... ...I .  .      ........ . ................... M
.......,=.........................Z...M$.. $ : .~$I.+N+~7I..  ..  . . ..   N... .. ., DMM.  .     ....... .......... +.M
.........=8O  ................,..NI...I=  M7.M, ..7 .~O7.  :  ........  88D... .. .MM$MMZ~N.=...... ..887~=.  .....D.. M
.......... I   .N...........8 . 8Z. ..78D$$ ?+Z$7? ....=..........N .. . ,D..... .8~MMDMMMMM$.,. ..   .........? ~.... M
............  .....,ZD:.. .=...O,. =M $,.O+I N.7., .7 ..:,:... .:+... .. +.....  MM=MMMM$MO.MM.:   ........... ,...... M
..................+.......  OZN.:. .,.+?.Z: N,.7 8? N.. .?Z? :M~D,......? .....~.IOMMMMMMMMM7MM: .............$........M
.........................==I.Z 8 .IZ.. ,NO.$.Z I.$7.7Z....=D~ MM?   ...:M +.  . M+MMZM8Z?O8NMMMD... .....  .+I ....... M
...................... I+.+.?.. ..$M ..: 8,$.M.I= ,..+ +....IN+.   .  ,??+. .7~DMM... ...MMM8M.MM~,....N= .. .8....... M
................... . . .~.=.... ?MZ .. ,N:$.M7IMN. = + ~... .: .   7OO?...,.,D?8N:D+.I$ N ...MO M, .............I,$I..M
....................=.... M......, O....Z?:N I.I:.. ONN7    +~ ... :NN8$ . :,:.:NDM.I  .,MIN$M~,NI.?..........  ..$ .. M
...................8 . D78..... D88M... . .+.M7I: .. O N+. = +.=8  M $N.......$+ ::Z:88~M  .7Z.MO.M~...............:.. M
.. ....   =.OZZ::,,+OZO,7 .....~, :......,:?.MM7,...D .=Z,,Z,.. ~7O?.$D.....  IMMNNMM=?8ODZII8M:$7MI8 .............= . M
...... ....... + :7 ....8......:..8OOI ..,:?.OM. . 7,.Z.?. M ~.$O8=?ZM .I   .. ..?, ........ ZMMMM...8: .............. M
.............:O?........7N . ,.O...+  7M Z:..IM. ?:, MN$.. M$. D ~=..$, ..?  O .8INMII~DO$8I~D,N. I...,:.............. M
.......... $,...... .N7..,Z8+ O...:....+.~M. I7.+.  ?.+.O .....:=.+?N... .  .,. .D:O  ..   .,OMM.  +... .............. M
.........   . ..... MZ. .  . .... M M ....:IM,$..,N  8.  8....8N.~=MOD    ZO?..M,~8M?8=:$~,??= MM==7..Z Z............. M
.......... .. .....M8.,.. .D~:...  N..$. ~,.  N.  . $ ....  .,NO.N+$D...   ~  ,$ 8~~MID$$,O$???Z  .M..7NMD. .......... M
...................M? ..... . ....+ZM~ ..N ..?M...=Z,..I ....DMN N7........M..=.M ~ :...Z.=MDN DM..7..+D. .D.= ....... M
................... ..    +MN.,.....ZIM..+MMNM. ... +  ....,8ZMM=+.?+.     . 78Z  ? D $.  .... .M+$...+ ....7 ..,,.... M
.....................I=,+ ... ,IIZM: :O? :.777M8M77,~ ... $8IZM,~=O7=  I. N.+     Z.I......  ..?,  .$.+......~ ....... M
.................. ..  7..=??NI?I 8:IDI 7? I?8~I$I?.7MO .:= 8ZM?, .   ,...,.~.  . :M~ ..... ...ZM. ?. :,.......~...... M
.. ~~~NZZ,.. ........N. ,OI8O.+,8:~I.DD= ,,88,:..~N88,78+=$Z8ZMD= ..I ...O.,  .....~:... D.... ZM.7,O +N ......I.......M
..........  O .. ,NO   MN=DM8M:~,DNMMIMMMMMM:. O.OMM .N$N=:,8ZMZ.. ..... . ,?=... ?. ...?I ... :,... 77:,...... ...... M
............. = .. . ONNN=IIMMMMM=+8$ .,MO,?.,M78~. 8:D.N$.7DN? .... ...:.N ..7~==D ....? .......  ...?ZIN............ M
...................I,IMM7MMDMMMMMZIIIMMMM7,IM = 8I,M. :7 O87.~ ......... 7NI~ = ..  ... $.8. ... I .ZM.M ............. M
................ .M 7+M$MMMMMMMMM?..$MNDZ?  M+8~..M.,..~?..~D8 .... ?...~ M$ 7...M.....=. =......77??, ............... M
......... ......:~.O=M+7M=M?8MN~MDM7:7Z.=ZN~:.? D  M=.O.=I8O~,+,+I7 .... ..,:....8.... M...O..... M.  .=I...... ~ .... M
........Z.  ..: ,.:8.8,,NIM=M~, ??8~:M+..8.IZ,.M.D M.N$$$N878~?.. ...~O7...  ....8.....~...~ .....N............I. .... M
.....,.......NMZ==OD. 7~M 7.:.==.+IN:Z.N . I  7 $:? N,+ZD7 MZ ...  ,$......,.... 8..  :  M .N... .N ...:. . . ?....... M
.......... ON+O 7+7 ?MONO?7. 8?+? ~..7O .Z .D. 8?..N8?,.MO8   .Z$: .=   .. ......M.  8 ~M ...+7 . .I.. I?. ..M. ..... .M
........+ ~ 8 8O O,..,?NN,7= M~ ,+ ..~:O Z=I $D.M.:MNM.?MD=.D..Z ... ..... . 7 .  = .O.M $7. =. ..N?..  ....$....8M~OM=M
... .=N:  ,.O~7.$~,.+,8I M7  ~.~.Z Z..$.D.. D. 8 ?MMNN7.M+.=..7................. .D .. 8...  MN ..N.Z=Z . ?N.. ... Z.. M
 .$:D?.=N8+~:MO ~$.,$.I 7+M ~.,$.. ...,. ~,$..Z...MM=87M.I,I ..DDD. ............ .: . O.. .,.~   ...M .:NN+....+:,: .. M
= MM: D+8   .$M~8 8= 8 :M=I D D.. 7 .. O N8.:I,.,MMMD.7,7MM ~.. :~ N ..... ... ..8  ..:   ....,D ...MD :M ..... ~$ ... M
.......:.....,ZM.7 ..+7 Z=78.O8 ..I ..?+.=  M+ I~?~M ?~.$?MM.$.. ,.,.~...........O....Z8~.....M. ..I8.M?......7...  .. M
...... .......MM=...DMI 7M7=:=D ..? . $  +  D7 I,D..N OMM. $  M   M .M   .  ......~:N DNI . ?...~,M MI?  ...... ..= .. M
...  .........+O,..NDDM.IO7 : : ...:$ .  N..D7?. .~.ZM, $. M8 ~ ..Z..~.$.... N??? MN..ODM$?=.?..M8??$M ............~.. M
...7.........N M ,~.. 7=M   ,8: .. , + . 8..N 7??M:MO ...  M  .~.. I. DI....IO8,,::~MM7,M,, ,.  M..N+, 7...........8.. M
.............MD~I M.,:7:N. .8~N+..  .O..., I.$ NZ DNI .. NMM.. N...,=.N?,  ...... DN M+D. ..N~..MM.M~M8 DZ ........N.. M
...........N+MD.8=~.7N7 ...ON~8M: ,$.O. D..=N8D .Z M ... D: .. 8... ..N ~~.   . . +8N.. ,MZ7,..::~ 7....,  :, ........ M
..........   MM :=,MDM :IZ7=~~:+:.?MMO. ~.MM.. ..MZN.....M. .  8....    ,~ .MM?.,..    .  .MZM.Z . ....D....  ........ M
............ ?..Z=ZM7, ~I=7 .7: I+M.8Z 8.7~~Z .O$ ...... 88.=~ M... .....IN~ 8I ....:.ZI  .D. M= .$................... M
.........   ?.NN~ O.:,.:7 I ,88.,IMZ+Z=$.8,?.?$MN . .... MO~~~ N... ..  .N?~ .O ....: :. 8 .. MZ.N.................... M
IOOOOOZ..+O=O 8.MDM.OM7:. I ?MD.:ZM,~ZZ.?O:?$MM7:.    .. 78I~~~...  .....ID~?.Z . .., :.  .:.  NNO.......... ......... M
......... .OO.N? IO=  $=.. ..M. ,ZI $M.=.N 7,7$D.........MDI:Z,.........::D$7.$.....  O...=,...N I:=D~ .......... .... M
.   ..M= ~ ..M.$.M.DN~,M...88M .: I..O$MD,,$877 ...     $M M8 ..........N NO..$ .   . Z ..Z, . Z.I..NM. . MD. .  ,N .. M
.......I,   ,.N8O..+ O.M$.Z88~ M ZI .+ ,MDM.?D7 ...=M...,DMN ...........$:8O: Z .8... O8..$, . Z.I..?.  M,,=.,8=... 8. M
....7~. ...... D?7I,8 .MM. ~7.:M.Z~.M?~8,=M.: $...8  ....   ............MIMM7 ?.. ... 8O..Z,., Z.7.I.M .+.+   +7:Z.77  M
......... :..  :~MNN~$ON~M :~ 8M :I 7 D.7$DI,. .. Z7I..  .  ............N...=.~..N, . ?IOM77+Z.O.7 I+ ..=  .. +7..=$ . M
,OO,,,,,~......~,8. ~MI.D.I,~.,M DMN.O?~?ZN$MD......  .$ :N. ...... .....8.=...~M ..:..   .  . .:~O~?.......   7..==NO.M
. . ..N. ~~~~:MM=,NMNM~:IOM=8~,M ,M.Z.?+N=. . ........8 .... :M:........ .N~I~M.  DZ M:  ~I$ .  .. . ,M.....Z..7...NM.MM
..  O...... ..ND.D,8O=MDI?M=,MD?8D.+.$NN:,~$ ,DN. :DD.:M..8$+NO. N....  Z.O...,=NNNNNMNNDN:DN::.   .  ... :DN N$  =DN NM
.. .  .IIMMMMD=Z.  M.NIMI 7MINDMMI.MII+: M7..... $+M   O..?  8=  NZ8  M.I ....  .~::D8,? ~.=N. ~,.N..M7MMMI? .  :$7N. DM
.MO... ............. 7DDIMM7,.,~M +.D7$M++++++++++?.N+.  =ZZ8M+ .=.$.+~.......+M$   .Z7DMZZZ$ZZ$MZN+?++NMNM+?MMMMMZZ~..M
 .....................  D+M+.M=N.M~+8.++++++ $Z . .  ++M?......  I8M, ..... D ........?D ....+...~MM8++++++........... M
.........................MZD. ++..+  ...........$......~M~. .  7...D?..... N...........+?  . ..... DO............... . M
..................................................,8Z. ...=8 .  ...Z, .. .D.     ....   I,..? .. .. $7 .............,  M
......................................................Z8$    ,D....,Z8  .D  ........ ...,?~  :?  I,?$M+ ............ ..M
.................................................. ....  .DZ. . $M...N  N  ... . ...  . .. ~:     ....+D ...... .. ... M
.......................................................... .$:Z,M. Z~.?....... ............= ..........??............. M
....................................................  .......?ZI8.   O.$ ..... .. ......  .  :..........+ ............ M
.........................................................  .8... +. . M7 ..... .    ........ ~~  ... . .NM...7 ...  8::M
.................................................. ... . . 8 . ...+.....Z  ...  ..    .     . $+$+++$IO+=.........N... M
......................................................... 8 ...... $?.... N................... .D     ...:............ M
...................................................... . 8..........Z+  .. ?.  .. .. ...  ......,O  ......O  ....=.... M
= ...................................................... .  .........+7....  I. .......... .......I........N ......... M
.. Z:D..............................................  ..,...... ..  .. ,:.... M.. ................= .................. M
... ..:,........................................................... .   =..... N..... ...... .... .D.................. M
....... .. . .....................................  .. I .    ..  ...    8O    ..,      ..  .      .M ......... .....  M
..........,I.I,.....................           ????.   .. ... ..  . .    .,I  . ..?. .  ........ . ..=,............ .. M
.............=,.. .......:8$.~~~D8D8  .  .  ..   . .. Z .................. .:,.....D .......................7,.... ... M
............... 7I.Z+,D= .............................+..... ................:+ ....~  ..... .........$ D ............ M
.................Z:................................  . . .......  ........ ...?Z......O... ...... ......$N............ M
.................................................... . ........................M$ ......MN ............. NO .......... M
...................................................  M............. . ........ ..~~........~Z.. . ........7: ...... .. M
..................................................   .         .  .      . .     .D,+   ..  .MI,7M7........ID.  ...... M
 
""")


page43_art = ("""



$.................................... .N.~8 ++MMMMZN$M.MMM7MOMMM+$MDMO,+MMMN..= 8= .....................................
$.......................... ... ..   I=..MMMZZMMDMMZ?$DMMMM78M77.MM.+$MMMM7MMO  .? I....................................
$...................................O .7MMMMD8MMDMIM8DDMMMMI8OIOM~.MMMMONDIMMMMN  .$ ~..................................
$................................ 7. ~MMMM,7OMMMMDD MMMM8M.MIM:M.+MOM MZMIMMMM$MMM  .? I................................
$................................. .MNMMMMO?$$OMNMMN$MMMMNZZM=N~MMIMM:MZ..$M$MDMMMM.... ................................
$................................ NMMMM,MMMMMMMMMNM8$MMMMNMMM7.MMMMM:7MM.MM+NMMMZ,M.... : ..............................
$............................... ?M8ONNMMM$ZMMMMMMMMMMMMMDMMMMMMMMMMNMDMMN.7MIMMMMMM=  .: ..............................
$........................... ...+DMMMMIODMMIMM8MMMM8MMMMMM,M+:MM:MMNNMMMM8MIMMNNM~MMNMM: , .............................
$...........................?...7~OMZM7ZMMMZO8N$MM$8MMMMMMZZMMOOMMMMM87O,7MIZM8MMMMMZMMM$?..............................
$......................... ~.7.NMD~8MMMMNMMMMMM+?MNNMM8NMMMMMMMDMMZZMZMMMNMMMMMMMOMMMMMM?ND   ..........................
$..........................??..7?$78?MOMDMMMMOMMMMMMMMMOMNMMZMMMMM?MMMN7:8?=NO.~ZD$NMMMMMM8N.8. ........................
$...........................8~MMMNMNMZM$MMMMO87MMMDMOMMN  M:M.8+MMMMN8MMMMMZMMMMMMM7MMMDNMMN8.+.........................
$..........................? ZIMMMMNMMOMNM,MNI+MMMMMN8  .,=DI8NN.D+D.=,MMMMMMMDMMMMM8MM7MMM?+.+ ........................
$......................... ..IZMMMN=M8MMMDMMNMMOMMMM....MO. ,MM?NMN.MM  ,:MNIM7MMMMM+MMMN~M=M   ........................
$.........................M..MDMDN88D~I,?8I7?8NND. .  =,~=...,?.DDM8O8:8  $ :8M.MM8MMMMMDNNZ=...........................
$.........................  7MMDM+8NZMMM8+MMMM,  .7DN$=:.$.~7  .,8~..8?MN.  ?..MMNMMDMOM8M~8N., ........................
$..........................7DN~MIZ?=8DI.,:.  . ,=N~D7$I..~.~,, .....,. ,NMD$...MMMMMOMMMDNNM..I.........................
$..........................D?MMMNNMM8  ., ..Z., .. M$==.I.. .7......... ..M$~..MOMMM8MMMODDM?.  ............... ........
$.........................MDM,M~MIDM .? 7Z.? 7,.   :8=.=  7 ?? .......... =M:..MMMD,MMMMNM?M8.. ........................
$..................... ... ZIOMMOM:.? 7.  ..$ MM, D  ~~D ??.I? D .  . .....8 $   MD,MMM,MI$NM...........................
$..................... ? ZMM8MMIMO .M=... ~$.?.... .  O ,7.+.+,. :~~~Z:... ,D. ~.MM?M7=MND?MN...........................
$.................... ,. 7MMNNMN  M. ~ .:D,..I ...:  .+  $.,I=.78Z:M .  .~  ?. ~+8?+MZM8?MDM,.     ...       .  ..  .   
$.....................M.. MOMMM.. Z..., :  $.~.Z .,,~OI ?~.~?,$I. .. :~ ... =..:.MMNMMD8O+M.............................
$.......................:, ZMM.,. +N..I   ..$  ., .. O+ M,,:7.I~M,NMM .M: ......MNM~MM?M~DD.M...........................
$......................Z.I .?  :N. $..: . ...$, .?.. O8:I.,$..$:MIMMMDO ,?........I8MMM788:O............................
$..........................~...:..+ . 8,.D..7     .. M+D7.:?.==DIMM.?MZ . .I. ...,+MMMMMM$,?............................
$......................... O:  +NZ+   ....$. ...=....++:? ~+..M:.N$MNMM.. M........$$MDI$M . ...........................
$........................ .  Z ... ......... +Z. DZ   MM~. .  M8. MMMM  ,, ......  MMMM8MM   8..........................
$.......................M ..... ,+..... 7$, ..+ 7...M.8,7  I?.M=MMMM7I,I? .......  DZZD78D O D .........................
$........................O . .= ..+..~..   . . ,  ..Z ... .,. I ,7,, ............. : .NMMD +.+  ........................
$..................... O +..+~,...~ ...$ .M .....D.$ N .~?,+? Z=.=+ ................+.MMM : ... .............. ... .. ..
$.................... DM.. ... ,.... ..:N.. Z. O. ~8.N.8.:.~, MI,=. ................?MM :  .$...........................
$.................... .$M  7:+ ,...8M, M..+ .. MI:.,7I7D.,~.?~7+Z, ....... .........M+?  + . .................. ........
$.................... .,M.. = ... .7.   DM..~D~   D.?8M:~ 8 :I .... ..  .. ... .. ..M?M ......... ......................
$.....................,.M.. :.: ...,...:..:M...D$.:N.7Z...,,~ .  .7................:ZMD ............................. ..
$.....................?.M..  .  ..OO :~+.. .+.   Z~ ~:=,IM,M$7   ................. :$MM.................................
$...................  M M. +  .:..+~. .:O . ..  ~.~+.:7,~$.+.............. ........M7M .................................
$...................  N.M...M . M ,........... . M. M.,: 8.~.......................MMIMZ  ..............................
$...................  ~.M... M+:.8M.......7 .,~,O,ID.+.$.=,N8~  ~N .............. M7+M8NM8..............................
$..................I. ,.M...+ .:  +.... . O.N..,?,M $$ , ,N .......7............Z MMMDM=:MNM.   ........................
$..................?..: M..$? ...:..   :OM.....$ID,8 :,~I............7........ , MMNMMNM~M+MDID,........................
$....................7M.M   .O? I8..?7D  :7 . II.,?~:~=. ............ ?Z......I.$MNMMMN=MM$MMMD.M.......................
$...............     DO Z.  . Z  :  7~?ONM. :8,O~O~ = I ............ ?.........+DMMMMMMD:MMONMNZ.$8.....................
$............... O8..I .... ..D.    .8 7D ?+.7:+: : I?OI ...........:.........=.+DDMI8$MM:NM,ZMMZ.7$ ... ... ...  .. ...
$................,:. ?   .. .? .~    ,I  :,$:O.,7.7$,~8.D8........ :..  .. . .  ?M+MD:MNMM+8M.MNDM.$$ .. ... .. ... . ..
$...............$. .ZI ?...  +N =. = =MO8~,.I.8 =O: I.7 =$.8 ....Z .........I. $+MOMMM8M+N~MDMIMDMD ?O .............. ..
$.............. ,:  Z  7. .?Z.,..   ...,.O ?+..:=.7.?,:8.OZ .::,..:,...... $...8?D+=DM.M8I+7IM7DDM$DI8. ................
$................  IM...M:..+  D..  O . N.. NI  .D8O $ :.:..,,,,  ........M....D+NMNNM+NI8MMOM+7+MM, 8? ............. ..
$..............:  .:+.MM. M.D?...,..N :M....Z .....OO~?+::~7I ...........~.....D 8$8~DNIMND8,MOMDMM+M I$................
$............. I...O.,,.M  8.==....~.$...+,.+. ... D$.M77D+ ~........ .Z.......~.MDMMMIM:M:MNMZI$.MM7.7~ ...............
$.............. ..7?.7.?.   = I....OMI8..8.  ...... ~MI.ZM:O?   ..+MZ  .......  ~ M8+.MM~M+M8.MDMMN:M:+$Z... .. ... ....
$.............. ..N  ~ . 8  ~. . ,7 +~. 7 ,.  .. ... N .+M:$?? .. ..............: =MZM8MZ,MMDOMMO.OZMM~O?...............
$............. . 8.. .,  ?78.~.. D.O.+ N:. . .........:, I.:87...................D .MMMMMM$MMDMIZN8M8M =.......... .. ..
$............. ..~  M.., .M7.I., ?8I.  8..I.     .....=  ,.+I= ... ..................:M=NNM+$:MIMMMMMM  I... .. ........
$............ ~ =..  ......??..   N +.I.....   .......= =:..I=.~....................... DMMMM?Z.MNMMO?...+I$, ..........
$............ .. ..I....... Z . 8: ,.~I.  . Z    .  ... OD .   M  . .   .  .   .  .. ..   .MM        .MMO.  ..=.   .. ..
$............+.... ..Z.: .. . .. 8 N.7~....:........... ++.~+ =?.,......................I..=:~. 87..$?.  ...N  .........
$.................8 ., 7  M:  . . . $?....=...  ........I$:.7,.D=  ..................... .8:..,$ ......  .  ..7 ........
$.................M~DI.  ..~.= D~.O.M7.$.M. ..  ....... +I+,7~.IM..................... ?:8+ .  =.......... . ...........
$.................D...?$ $  ...N7D$OZ .:. ...... .....II ,7 ~I~,$7 ............... ..+.? .. ............................
$................,O..=...8 ....M7: .I...$. ...........I7 .I ,~ .+I. ..  .. ..... .I I:? .. =Z ... ................... ..
$................8 .M .?.+M ..Z8NZ  +.$?: == .......... 7.,I.~I~ +.............? ,?I,. .?++.............................
$................Z, $. ... ...M=.+I~ ...+NI..$:.. ...?..?.,7,,?=,  .......... .Z....  ................. ................
$.............. D.: .... . ..   .: : .......Z. ...N. M+ ?..O,.?ZD ........ .N.I ..  Z,..................................
$............. ==.D.....D.  .,M.~  $ ......+:OD$,.7,:O N8D:=D7??8 ... .IZD~.  8, 8$8 :.................$................
$...........I  NN....... $ ?  = M IZ ..........?. ,8 =,?..~N=,=,     .~ZO.=+M~ID$8  ... ... ........ Z: D...............
$.......... ,: ~.N.... ? +..  M +. O.......... , . M8MNM.8:MMMMM++NM8,,+~MM8.:DM ?............... ..  ...M.. .. ........
$........ ..= :M.......Z. . D+$ M. O+.........,.,, ..?:ZM$7MDM8M.777MMMMI?I7O7.I+ .........................,............
$........ .M.=.8...  ..7...I..=:M. ,D........:=:.... ~NM=$$~NZ:M  . .....I ?, . ................. .........:......... ..
$...... , 7.   ,..IDZ.  .,..+.8.~. $? ..... ? ~.I ,.$+. $MDZM IM Z..........................................8 ..........
$......=.., :. Z.~..:....  .?...~   ....... ... ,.= .:,~.=$.I M+ D .. ... .... .. ... ..  .. ... .. .........+..........
$.....+ .8 ,.  .~= .M  ...:,. .M.:..,...... , ~ 8.: ?.+.=.7.N$7+ = ..........................................,..........
$....... : .,.+. .DI ..  ..... ..D..N, .  :., :,= :.,:,:,,Z.8$.M :............................................+.........
$...... O, .7 M:,:. M. .. ....N:,  ..O7...    7.~,: ? ? ? N.?I.7.= .....................................................
$..... O  ..7.N , .: ....N ....,Z M. ?7.  $ $ ~., ~.,~~ I.~8?..? D ........................................... 7........
$.....O.+ .?$.Z. N+O ....,.. OZ. D.Z .=.. =    +,, , ::,D,MN=7 ?.?.............................................~........
$... O ..?.:. M~, ..M.    M ...N D..M . ..8..   ,:..: +.+IMD.D7M7 ..................................  ...... .. ........
$...+..:...Z  Z ......  .+ ?O  D .~:M8.... ,.  =... ~.~Z.$Z$.87D. ......................................................
$.. ..... .M   ....I .....  ..IN . =8.M ..,..~ .Z.? ,?.I I I 8 =.+......................................................
$. M.....8+M7 ,..  ?  . ..  .7.. NM.M M ~  7,.D,:., . .:.,..,....N .....................................................
$..~......:DN Z..D MN.M ......7   M .8=:,$.=$ ?,.=,=.~.+.= $ ? ?.I.7....................................................
$.Z.  .... .M.Z..:    .......$ ,,OD: O  OD=I?....8. .,.~ O.O.I.? =.: $............................................... ..
$. ........D8 M D:. ....... ..:..8  .. . :.:D:O? .,+ +.7 ?.. I.$ ,.,,~ ~ ...............................................
$...........ZZ~ Z.I+.... . .DZ 8$ ,?   ZOM..IZO8+,ZM+. D.+.~.I.~ .,~:~.: :..............................................
$..=.........8.,..M ....M  8.  .. $.?N        $ DIZ :  MMZ   ~~  . =,  D I.I......................................... ..
$. ........... O. ~....MM. $...   ..O.,:,  ... + .~MMMMD   . OM. :.~.7 O.I D+........................................ ..
$............. ,   .I     .=... .,ZO. +,  +  ...8. M  N+I,MMMMD~.=Z?.+ I $.?.7+ ........................................
$............. .N M M .? . ..M ... 8..I :..   8.NMM.  ... ,8 N.DN N .M..,O.N.+.  .......................................
$...............,D .  .,:. N  .. ~ZN,:,:. =~=. . .~.....=NDZZD~O:~ $8MD8== +.I.8 O......................................
$................$M ....M.  ,.. ..  N..M..Z...~:....   ...  ... .~OZ: 8? . M Z.+.+ .....................................
$................. ?,...D~. . . ..ODMDDNN~=I,.7. :O ...:...O. ?. =   ,O   :M8D.:,= O ...................................
$................... 8Z?  M.  .......:  N .7 .+ .....Z=.  ..MMMMMMM+?= .N..,. .N?,.?$...................................
$..................7...=  MM~7... ..~ M 8~. =..Z .Z . . 7..., .....7 ...N$M+7. M8.=M.II.............................. ..
$..................8:... .$.... . Z ..... .M. I:IMM ZM+.. I..:......:...,..+~.I+IM? Z? ?............................. ..
$...................OD....  D, .D  ..N?   .7.. M .: ..Z. ,. .. I..=D  DO8, , $,.. M.?I, , ........................... ..
$.....................MI.......N  ...8....8N~M8+M88 ~MZ..N...?..:  ........O..$M  +NI=O7.. .............................
$..................... =MD ..... O~~~Z....... ....: .O 8~M. 7 ~. .. ...... ,. ID.O:~I+.Z..  ..  ..................... ..
$........................ M.M ..... M ....,.M. . .:. M : . N+ .Z... ..... ..,MM  .. O  =................................
$........................I..OMN+ .... 8...,..D.. .:+.I :.. D.......:..........  ..~+.O~,I ..............................
$..........................O .:~,?. ...,?77Z:O.  ...... ~7.D . .7.. ,..........$  D.ZO8,,.. ..  .................. .. ..
$.......................... .7  $,=~ ....,,. I:DI ...., ... .7 .....D...... ..~. O, M 8:,...............................
$............................ : ..DO$ .....= I ....8. O.. M:. ....... ......OZM... N8.M.. ..............................
$..........................  ~. 8. $Z$.....8 ...... :D. 8.= ..........  .O ....ZII. .DM$................................
$.............................,.., ,.~I ... +.   ,..$......... ...... . O .,...... ...M~................................
$.......................... ...,. ..M~?   ..M O...DN,~ 8 .....ON......  .Z.. .I..:.... =............  ............ .. ..
$.......................... ... ..O.Z+ .  ..M. O.,..... .. ..7........... ... .M$ = .. .................................
$.......................... ... ..Z ?I  ....+ .I, ..... Z.8 .7. .. .. ? .M  $.... ,, ........... ..   .. ... .. ... . ..
$...................................=$..... 7$  .N D~...   ..?$ ......:: .O . ..........................................
$.......................... ... ..    ..  .~....D. .,N........ ....... . ...............................................
$.................................  ......=..O ..:. ............. . ..  ...... .. ............... ................ .. ..
$.......................... ... .........=Z 7....:.N.........?.~Z  $Z.  ................................................
$.......................... ... ..  . ..  .  .   ,,..........,7.:M: .7 ... .........................  ............... ..

""")


page48_art = ("""


..........................  ....  ...      . .  .......................... ......... ............ . ..  .... ........ .M
............................  .............  .................................................................. .......M
.......................... .... ....... ........ ......................................................................M
................................ ....:........   ........  .....  ... ....    .   ....  ...  ..........  ...........  .M
 ..   .  .  .   ........ ............~. ,? ... Z:.. 8+ ..... .~,. ...:. ..+?....:.  .   .. 8:. + . .  .=..   ..,   . ,.M
..........  . . ..  . .. ...  ....  . ..I.. ..7....+: ...~  ..~I. ... . .7? ..~7 ...,~....~ .. M .:,. ..  +~8M? . ~ZO??M
...........................   .. Z::~::$:::..?   .O~    :.   ~D .  ..:::D?::::: ::::::88D$NDD8$8ZD.::::7Z ~.... ..... .M
 ....................... ...........+.....Z=ZZZZZZZZZZ. ..ZOZZZZOZ7ZZD... .  ...               +.......................M
...................................++   ??? ................. +......$........................ +........?$~ ...........M
....== ...............8=N.........,=$======..~~D ... .MO......:...... ....?=~D ........7 ~  .. +.......I..D ..........+M
. I  +$ ............ $...D ........,O==$Z$$:.+:Z .. D ..O ....M.......~. O  Z ....... ...$7... + .....N  I.8 ........,.M
.7... ,$................ 8........... 8 ~ ...~,I ... .... ....M........., ..,.7......D. Z : .. + D.. ,... ~+.........,MM
.~..OII ............Z. $ O...... ......  . 8.Z7MM:.8..I I.....N.  ... ?.$O=D:M  .... ~.7 $.....+  .. .M ..  O....... N.M
.......Z........... ?=  .Z=.  ....  .+ 7,I 8. +... M..... 8.. MM.MM$N?MMMMI...7.....: .....7.. ... ..,. ... .O ..... ,.M
....... 7..........7................I . + O~  MN .,   ..  ~..MM~:M.ZN,I=,ZM+M  ~ ...  .....= ..,.. .., M.. ,7~.... .  .M
....... . ...........=....~O.... ....  . . ~........7....7 +M7?8=,NOM.I$.M7~8?=, ..D.M ...Z. ... . ,., $ ..7+ D D ,..,ZM
......?8.:......  $.. ...=Z .       .      ~.   ..D I+....?78D?: 7,..$ N Z$8+~MM   D $ . ...Z  :.  :.,..,. ?.~,DDM  .,ZM
......Z~ N........$ Z?...= .?,. I$  .MM==== ... . D I8..$D:.8DI MO ,N+$NN M$=,M$O. D$7 ..I.. ONZ  .~., .: O?.. M:=   ,OM
..~:.,. I.= ...  ~$.+8Z8D, +..+.DM..   .... D :.D ..IM, MMI:8DN::I ZZ.M+$NO,N8DZ8:~D,7.  Z,. :D .  , ,.7 ..D .. M8...=OM
..   . . 8 M M:. DM.?...O8. .=:.M   ... ...8. .Z:.  I: MMMM7N:M:,N ?M.$. M? MMMDMN.NM?..  I..=N. ..8..~..   ...~.= . NZM
......Z . I,IM:...?7$. O N..   .M,  .  .,= ..7IM:., Z 7ZM.ZMD:7?MI.8 N :ZD 8Z.$,D7$DN= .  = .7..,....M.I. 77M7II7N.  M?M
......+ ....I+,...?Z+ $  N..  . O .. . D.  .~ ...., M.M MM~O7NN8N8$ON= 7M.MM.D=$.7 D?     . .~  ,. ,..~Z  .. .. .....$+M
.   .O888~ 88 ... ?N88MMMM8~~ ....  ..I.  .~. ...8M M$IOD8.MM?IN=OO NIMI.N$=,M ,:M  .7~=$. . ~..,....... $  7 ....... .M
..........7.D... .MNO=++7ZO....   .. :. I$8Z.....= ,, 787 M:$MM8.DMMM8 =N.$+. $N=O:..?.Z $ =.~..,.... 8..  .7 ..  ..  $M
..8.D + ...........7 ,..Z +    ..  .I :..78+.  = .=.$..,MM=MMMMD.MNMN.M.NNI:MM:M$N...+.  $ M ...,.... 8.M., ...... . .+M
. , ..  .......... ..?..=.    .  ....?. .7M+ ?M~.. 8I 7.8MNOMMZMMMM8IZ=$IMMM$MM.D.... M..Z M....,.... ~.:. .. .... ..  M
...  I  ............ 7.... ,  . Z.. ..  ..,, ,..,.. I I $MMM?M+MMM~M MNMMNMMMMZ:. ..N :. .?~.Z..,.. ..~... I. .... .   M
.... $.8........... Z.N .N.O    :  O? N.,. M7.=MM  .I   .,+ZMMMMM8~DMMMMMM  ..D. ...M.  ..$ ?...,.....:$ . 7.8.      :.M
...... O..........$ +...= ~=  .    NO 8I,M IO+O~M . I. ....:NMM.ZOMMMMMM ....  .....M$ ... .$~..I..Z..:I.. . 8.... ..N.M
......$...........M.+....=+ ~ ..           .  ....  D $7. ~:~+MMMDMMM~.   .  ~.     ~ODM   ~~~. , O $,.::...7=.     .N.M
......I..?$ ......,MZ.D$$$ZZ$ZNM$N+?+??+?????:+=,$$$$$$MMN,.MZ$=I+M?. .=O, .????$???????????. ..OD+Z$?,:?O$$D.+.  ...I.M
.... +MMDDNMM8DDDDDD8...... . ,  .  . ...........  :D8+ +.?M.N$D~MNMMMNI:D.......=........  . ..M.....8. .DD7:. ..NM~NIM
....................:,~~~~  .=~ ....~~~~~~~~~~:8~.$~  ,~:.?,I$:$?NM7M?8ZN8DZ: O88888888,::$:,Z..Z.....~N ....    .:8Z=~M
................. ... II .+ . .... ..???M$$7ZM,N ~$+ Z8+O??M$. DMMM~  ...  +IZ:M.........DM +8..$ ....:=I.$$? .........M
... .... .........  .....~+  Z .... ? .... MOD== .~=M87+,,~MO .MDMMMMNN,  ...,M8=N .     $?  MO.$.....:I, ..M I.... O  M
 ........................~   ,..... I.   $..==D=~$.   :,.MM= O$ZMM?,NOOZ$~8D,...=$+N     .IM  OIM.....~. ?... D....  ..M
.........................~  .......,I...M~ ....~ ....... $?7..ZMM8N.8D7:=D~.7I+..NDO~...?.ZM....M ....:  I... I....  M.M
.........................~. I .... ,? .=D,$~O.  ..,7 .7O?$MM8OMO,$ .. ,ID =77=O~I=MO==  M.7 .....N....~. I.. .I..... M.M
... .... ................~ .. .. . ,N=77+,N:D7DZ,7?I+,I8=$D~I?:MII.+... ..=:8=$77D,. .$$D........ O...~  I... I.... ,M.M
.............. ...,NMM:,,  .: .... ,$,..:7=~N+=.~.NZ..?$MN~M M8MN~,$.,,++N, .+.DZ . .?D,.? .......+...+N,.....I.... ,M.M
................::::::, ... .......N ...:8:=NN7~..:,.....M,M~DII,Z~?~=+$$::$D?, . O:=7:N.., ......$....O: :DD 7.... ,D.M
............ ............. ,......~M~. .  .MM8... .= : :  Z. DM.  ... =I8,  ?+D$ D I$.I,..7 .....N ..... ...87 ......,.M
.................... .... .Z.  . .ZO=Z,8 .7+I$I~,O$7?.?=:IM7MMM8Z~,IZ.   ..=~:~.MN D. . M?I.....=N.~$, .. ..........,,.M
.............:. ..=. ?.. , +O D :.M D,D:D8?O=ID8MINNDO$N?+NM?M,=M:,:MM$.,Z77Z.MM?,N....+?D? ....MD$M.D.M  ..........?D M
.............,....I. +. . M=~.= ~.:D$I:+MMMMM?D7......  .? NMI,:N,.=8N7..7DNMNM8~ ... ~D$N .....+....N,M.I.D.. ........M
.. .... ....,..I.. .  . .+D... ...7.+ DMM8MMM,.......... ...8:..... I..~:OZ7?8M~ ....IM878$....~=..... INI ? MI...... .M
.........................:.... ..  . . +.  O8.... IIDI+:. ?ZM .7.........   ,O=$.IZIN7I= +?  . +=...... ?~ M ~: D.+ ...M
.........................$ ..... +  ..  ..8 MZ=ZDDO88~?.,ZDMD~DO8.=DO,,~= O  N7?$=ZOZ$~~:I ....+=........I...~7.I.$.=M M
.........................,......:........~ .M:,77OD87=: I$8D7$ND=,,?+~:~.IO$OMMNMNMZMNZ..?.....M=. .... ... ... $.8.=N.M
 ..........................   . D.......~...M..?. .. ...+...  . ..,8D$7.=:~.+MDNMZMMZO.   :... Z=.........I.......  ,N.M
........................~......7...... .. ..=  .     .. .  .   .    .......~O+MM8+.8......:.....=:..  ,....O... .......M
.........   .. .  ......O......~...... ,.. .==  ..M?NZ7? ,::~=8~ ZM7,.?..   M .,:.............=,=...........  . .......M
........................ .. ..O..   ..M ....~?O?.,~DIDII:I?,:~+. $OZ~~:=:+:,8.. 8.............Z.. ..........  . .......M
..............................~. ....~.... . OD:....   .   . ?: ,IIOI++.8Z.:8 ..O:........... ,.? .....................M
........ .......... ....     . . ... 7 ... .  ........... .. ........... . OZ...O:. .......  Z,  I............ ........M
............ ............... 8 .........  ..=$:.,~:.7..,D?=,OO=,.:~=  .. . .M.. Z.8 .........:Z.   :.......... ........M
........................ ... . . ...7  .   .=~,7,OD8O~. DI.+777?=:,=,8~~ .M?M .  . :........O Z  ...... ....... .... ..M
 . ...... ......... .. $O . + ......8....O  MI+,,.:=+   ....,.:7N88=.O8O7N8NO  :..  .M  ...7 .$ ....?  ... . ..........M
... .............. ....$=   N ...   . :..: ,O... ...................  ...  DD?..    ....+M$ ... .:....   .. ...........M
.......................?... ~ .... 8... ~.. DD8..~OO$   ,.....:   . .     =:.M.  ZN.........  =M :.........N...........M
......................  .,..~...  ., .  . ..8Z8+. :DN:,.M$=..O+=::,+DN7ODM:7=M .= :. .....I . ~ ,:$ .8.....?..  .......M
.............. ...... O  , =......~  . I  ..MI$=  IZ8?, O8:++7MDI:,=7$:ZOMMMD. .  .. .   ?....O Z:.D.... ............ .M
................... . .=  .D......8  :+7.. ..+, .......... ....  ...... NOMM     MM  .. ?:    +:8I.,......Z ..  .......M
......... ............  +..8.....    ..7..O  NZ~ =:.$8I?M.  ............7OMMMOMMMMMMM.... .=D$,.,.M.N ... I ... .......M
........ == .======NNNZZZOOO.....MOO.,,,,,?==I,MI8+,DO8M788M?7,$OONZ==:MMM=.. .ONZZ,,ZO....... ,D.,,7, ..ID ... ...  ..M
..............  ... ...... ......: .. .7 N   ,. . D+7MIM$ 8MM??NDZOZ:OD.+, .....+ .... ?.= . . , .....,,... ..  .......M
..............?. ...... .. .....~...D.. .:  = ..:...  .... .MZ...8I$M$  . D . ... . .. ...... ...........Z  ..$ . ..=..M
............:........ .+:...... O.,  .. .   :.......:::8ZZZZ$~...........  Z......... .. ..  , .:ZZ$,:.   ,N  7 ....=..M
.................... I.....,... :.. .?...    .............................,I . .=8.. ...  .............. ... O?O.... ..M
...................~...... ....8  ... ....I~ ~............................ .+ ... .? ...... II.= ...? ....   . N I .=..M
..........................+ ...M.:  +==$8=O8 ~..............................~  ..... ........~.......... O...... 8.Z= ~M
......................... O....8D..........~ =...............................$ .....  .....................:  .... N==~M
.........................~......,.......... Z~................................8......I.......................:.......Z.M
.........................D ..... N......... O~................................ NN,,...., =.~...........  ......O...... M
.........................,.....   .?........M..................................:MI  ...................................M
.........................,.....M ,I,........=.:................................ +......................................M
.........................,......:.........,,M ...................................:.....................................M
.........................8.M M, D. ..  .++ZZI~...................................N.....................................M
........................ O =.= M+ : .......~.~..... . .........  ................   ...................................M
....... . .. . ....OD:?. ,?.?..,8+. .......$ .......  I??I?II~................... 7 ...................................M
................... ...... ,.~N 8MI .......O.................:.................... ....................................M
............................ :O:~MM....................................................................................M
..................................  ...................................................................................M
.......................................................................................................................M
.......................................................................................................................M


""")


page51_art = ("""


. ..... .......................... .............................................
. ... .   . .... ................. .............................................
..  ... .....................: . ...  . .$ .....................................
............................+.. .......  8.D....................................
.......  .. . ..............,..... .......+?D...................................
  . ....................................... = ..................................
  . .................... ..................:8=..................................
  . .....................O..................:,8.................................
  . .......... .........7=... .............. . .................................
 .  ....................7:...................,..................................
    .  ...  .  .........O..................... ZM...............................
.....................=.. ~...................?. ~...............................
..................... ..:.I .7N8Z8$.... . +I... ................................
......................:......=87++$....M++=M.,DN................................
 ......................O..,NM.MMM 8=.. MM.+D:O. ................................
. ......................~D.. :M$MO.:..O ~? . 8~ ................................
........................M ....??. . .. :MO.. :..................................
........................ MM......+:I.M+N....+O..................................
...........................??............... ...................................
...........................MO:...........M.:8...................................
............................. ...~O.O88.+.?88...................................
............................:N.....  .  , ,~M.............  ....................
............ ........,II~~+=O~O...... ..?= .N.7ZMO=.....8 .MO7...  .. ...... ...
........ M . ..DMM8Z?$MMM MM8.D:....  ..M . . N=MI+DDMM...MD .?.................
......... 88..:MM=$:N8$?,N: = 8.. .. ::INI......=N8D8M   ,. :N..................
........  ..M.. M$D:M~77I?:M~.8:...=  .?N ...,8.. .   ..=.I??D. . ............. 
........ . . M...N=D:Z.N7?M8NOMZ .,ZNNN..I .M.... .....  +M7.  .  . ............
......... ,: .Z..,O=M$,$M.M.+O,IMNNM~MDO$ .N ....  ...  .$=.=   :.. ............
........ N..   N...~,.?~7M~M7~:M$M,=,8D?ZO ......7..... +7..  =I... ............
......... ..~7  M...8=.$,MD~~NDZ.7+.,=.ZD8N?~..,N7?... N, ?.?7...  ........... .
........:........, . NIM7O.M+NO77+,..O:M+MDM8NM....I...~8.~.. ..................
.......,.........=D8...M7?MZ:, NI.$=:8,. 7 D=N8:? ..7 .:,=  . ... .... ..... ...
........ ......7=..,D$ . $D,~:OZ.+M$=:M~?~N=O$O.Z+$ ..OO~ZNI....................
................... . $Z....M=M II?8,M=MM+Z=.N.O...? .N:.+?I....................
......................  MM......MMD~NM.MO~..:..  O$N=..,~ O+Z ..................
............... .......,N, 8.:. .............~=N87MN:OD:., ..  .................
............... ...............+MO.==+=.=DM, ,=  ...MN M8. ...... . ..... .. ...
........ ...........................................=O= ,...... . ..............
....................................................  ........... . .... .......
....................................................... ........................
................................................................................
................................................................................
................................................................................
............  .......................... ........ ...... ..  .... .... ......  .

""")

page52_art = (""" 


.................................................................. .....................................................
........ ................... . . ....... ... ....................,..........,.::::,,:.............,.~. . ...............
 ....... . .::::,::::::::,,:::,:,::,:::::,:,::::,,:::,:.         . : .,,,:,:,   ...: ,,:.::::::::,,. : ,,.::::::::::,,::
 ..........$ZZZZZ$ZZZZZZZZZZZZZZZ$ZZZZZZZIZZZZZZ$$+ZZZZZZZZZZZZZZZ$ZZZZZZZZZZZZZZZZZZZZZZZZZZ7ZMZ8ZZZZZ$ZZDMMMDMMMMMMMMM
 ...... ......  .......................................................................................................=
....?... .... ...... .......... ........... ...................... .................................................. = 
......8.  ..................... ........... ............................................................. .........  ...
......  $    .. ... .    .  ..... ....  ..... .................................................................... D ...
 ........,?              .      ......      ...................... ...............................................,.....
. ........ ~$77777777M7MM7MMMMMNZ?I?IIIIIII?II?IIII?II? .$.....,.. .....?.,.77$777$$$$$$$$$$$$$$$$$8MI$MMD88MMMMMM .....
 ..........~8$, 7...=........... 77?~7$=777$7$77=~7$7$$+77+777?77,7+7~77,7$ 77+$D777Z77=77777777777I7?M7MMMMMMNM + .....
...........~Z :=: . .     ..  ...     ..  ...     .............. , ..........................................~~N.+ .....
...........~Z : . ?                 .           . ................ .........................................O. Z.+......
...........~Z : .. =,     .     .     .     .     ....................................................... .I ..Z.+ .....
 ..........~D ,      Z    .       ... .       ... ..............  ...................................... =. ...Z.+ .....
...........~8 ..     ..O===============================OMMMM8NMD8MM+=========MMMMM+====,================O......Z.+ .....
.......... ~8 .        M=$MMMMMMM??????????$???$MD8MM$M???????????I+??8D7N??O?????????????????????Z???=$ ......Z.+ .....
.......... M8 .        M=M          .... :I7MMOII .O: ..  ...  .....  ...  .....  ...  .....  ...  ....$ ......Z.+ .....
 ......... ~8 :        .=Z.,        . .         . .Z, ....  ..........  ..........  ..........  ...... Z ......M +......
...........~D .       ..=Z ?      ... .       ... .Z:..................................................Z ......N + .....
...........+8 .     .  .=M.M      ...         ... .Z:..  ...... ...  ...... ...  ...... ...  .........,Z ......N +......
.......... ~8 .        .=Z O....        ...       .Z:... ........... ........... ........... ......... 7 ......N.+......
. .....  ..88,.       ..~D Z,7 . .+++$N$$,,,,.    .Z:.....   .. ......   .. ......   .. ......   ..... $ ......M + .....
.......... M8 .       ..=Z?.      ..  ===:NMOOO . $Z:................................................. Z ......O.+ .....
 ....... . M8 .       .D=Z =      ...  .      ...  Z:...  .... .....  .... .....  .... .....  .... ...:Z ......N + .....
........ . N= .        8.O ?      ..          ..   Z, ... ...  ...... ...  ...... ...  ...... ...  ....$.......N + .....
 ......... M=~.        ..M.?      ...         ... .Z, .................................................$ ......N + .. N 
.... ...   M:N.        M.M ?        .           .  Z:... ..... ..... ..... ..... ..... ..... ..... ....Z ......N +Z+....
  ... .7,. N:N.        M M                         Z, .......  ..........  ..........  ..........  ....$ .... :D.+ .....
........ .:O:N.   .   .M.M  ...  ....   ...  ......Z+ .................................................Z .?7   N.+ .....
. .....  . 8,N O,.    .M.M .        ...         ...Z:O.................................................Z ......D.+ .....
 ...........:N.    D,. M M                        ,Z~ , ...............................................$ ......N,+ .....
 ......... M:N. ..... IM.D.~......................8 $II      .    .      .    .      .    .      .  ...I ......N.+ . ...
  ........ O:N........ M:M. ...................... 8..,M. .... .   .  .... .   .  .... .   .  .... ....D ... ..N.~ .....
 ...  .....8:N.........M M :  ... ......  ... .... N$,.M ...... ...   ....  ...   ....  ...   ....  ...8 ......N +......
  . .... ..8:N.........M M........... ...........  NN.IIIO O.IM,  .   .,?7M$I+=           .         ...~ ......M +. ....
 ...  .  ..8:N  ... .. M M. ..... ..... ..... ... .NDD878.+,?~ZO?... =O~Z.D?N=.+I.  .,,.  :,.      .  .~ ......N + .....
          .8:N .  .... M M........... .......... NOOZ:.+M?:. ,=:.D .:MZ? ~MM77,MMN:N=M MM:+ 8: .   .   O  ... .N +... ..
 ..........8:N ........M M N.................. ?I~MM.=O, IZI~OO$+D7+?M~MO8=D$O8O.,N?M=?78M==?M8 . .....7 .  ...N +   .  
 . ....  . O:N.........M M $.................MM .M Z.:.I7$~+.N:8:,+~$:,N7.$NM.. 7,MM$MDMOMMID,D~.  ....O ..... O + .....
 ..........8:D.... ..  M $ $????$?????I?I?I?MM7 8+8~D 7$+8=$?:$Z+++M:.M ... +. .:$=NM+. ?  7$~?M?... :ZO ......Z + .....
 . ........8:N. .. ... M M    .. ... ...  ...M 8 ,ZDZ7 7MO???~~N+D?ZMM  .7Z O .IZMOMM:...... 8OD$.. N~ Z ......Z + .....
 ......  . 8:N........ M I.   .  ..... .  .DN, ?$.:D,I=.,,O,.N8N?M+OI=.+MMM MM, .,M: .DI.D .  ,= .:$D.:O .... .Z.+ .....
....  ..   8 D...... . M 7 .  ... ...  .  .$M7~~$N + OIM8 8O.~DDMMD=M+... D..... M? ,NMI MN. .O8 .,... Z ........+ .....
... ...  . 8 M........ M.+  ...............,.IM8M7:8 87Z M~M$I7DMM8M8M....D.:=+ .O=M.. ?.... . ... ... Z ......Z.+ .....
 ......... 8 M. ...... M.+ ...... ..........$ZZ :Z$87N$+Z78M.,M~ZM MM8  7MDMMOMM.$8   .Z++   8=    .  .Z  ... .Z.+ .. ..
 ..... .  .8:N   . . ..M.+ .  . . ... ..  . ..ODO=ZZMMMMZM.ZM~8ZM:MOM,  =  I~ . =  .I Z7  O:.D.~  . .. ? ......N + .....
 .. ..=~~~?8.M8N8N8ZZZ M D ..... ........... ?$8,ZM8$8Z~?ONMMM7NMMMN?M~$,. .Z  O.O...N  Z$. D, D.  ....+ ......O +.     
 ...... .. 8 M. ...... M I ....  .....  ...  .$Z8~MO8NMMMMMMMMMMMM7M.8MM8 +M~,MO:.  , $.. .M7....  . +M,~......Z.+ . .. 
  . ...    8 M........ M + .... . ... ..... . .$:,Z?MMM8NMMMMMM=DN~O:8DZ...:$,N     ..O?MM MD    . .. ,= ......D.+ .....
 .. ...  . I M.........M +  ....................=DMMMM:, .7? MMNM78 N8:. O+D7~O.       .N7Z,~      . ...  ... .Z.+ .. ..
 ..........M.M.........M.+      ...... .    ...... ZN,  $I.$M8NI DMM?ON$8,:8IO?N..  .  .O.. O~  .    ,M.  ..  .Z.+  . ..
 ..   . .. 7.M.........M +,........................ZN... .M?Z?,ZO,=Z+M8N8... .$77... ....MD.=~.......ZM. ......Z.+ .....
 ......  . = N7MMMIII I? . .IIIIMM$7+MD8 :IZI ...  ZD  =MOZ .,NN+~8MM$.M~.,$IO$D7I.7.7.   .~ .      .:.I ... ..Z.+  ....
 .. ......Z7M.,M:MD.? ZN,,:M $. M. O.O~.....  ,,I..ZD~8.8?.,ON8~M+.7M~:DNM+87..   .M7  .  ,.7   .  ... O ......Z.+  ....
 ... .~  MO=I.O   .  . . MZ...=..=O ...$M7 . ...... = .. . ?I,.. =88M :MM:.. OMNIN8.+     . D   .. .   Z ......Z.+ .....
 .............  . .N7 .N. ..=M,~,NN.$N 7N..... . ..N8O:...  .~8OM.MZ+,,= ..Z.= D7:MM,       ..  .      ,  ... .Z + .. ..
 ...  .  ...,, N7 ~. , M .+ 7  +?.Z. ~+  .77MIM=.MM8N$,7I.  .I8,+==DM,:M,~~ I8I  .+$N.  .. ..?. .  ... Z ......Z = .....
 ...... .+. Z=ZD . MO. ,= ..O Z$ ,~ $+$NM. 8 ?7+M   .I:7D7: .  O. ?MO$~M+I~~ ,:87N$M?        .N.?   .. Z .... .Z.+.  ...
 ......+.O? + ~?  ..7:~~..8.M,.....?7~NOM.. NZ ZM. .   ID7?M7  :+7+MM.DD+:: .OM:7.Z ZM=.   . ..  .+...,Z ......O.N .....
 ...    ~+.. M .. ...  ~...7.. .  ..  .7M.... I7M.+    .,I?MO:. N8?MMMND:OO8IDI   ..,=,,   .  . ZDDOD:.?  .....N + .. ..
 ..   .MM 8.=DN= +.=  .  +....?:. $ .MM .+,, +7.$+?N,  .  N7.:M:Z,N.MOM~8:::  . . ,.Z+?M, ..  Z. . ..  ?.......N + .....
 ......MO  M..$M.?.=Z. .?.I... +. .?....O . .$   ++NMO: . ..+DOM~.IZZMO7, .  O7.7.===.,IO,, 7 +~ .  ...?.......M +  ....
 .  ..OO +..M..... .. $~=I  ...ZN...,...= N N?  ...NM8,7N:.. ,+N88I.ZMM.Z ~.IO7.  7,...,..M  ..     ...?.    . Z 7      
       .Z.D .......  MN  .=.....,,.... Z   DN?7 .. .. ,7N7+~ .7MMN+?+=M ,:=8OM=...  OZZ$D7~7Z    .  ...? ......Z.+ .....
    ....:..~ .    . I~. ZO.  I  . 8 .  .M,.,M?7 M...  . =7?M+:8D+++  MN$:.:~:.  . , ZM$M87=.O.  ...  I.?M=  ...Z ?  ....
    ..N7+..  .    ..M.,.:8.~  ~  $ :.$..N=.7. D ZZZ=.  . .N$8M8:...I+M+ ~~ ....:I,ZM=+ .     O...  . ?.?  ..:N?O M .. ..
      . MM . .. .. .. .M .N$.. ,...,M?.   D .. .MZ$+N8:I . M=ND   ZZ+M:. .. 7MI:?N.. ..  .MZMM. .....Z ?.......Z MM.....
 .     $$Z:M? ....... .7?= .=.,D...7: $=I,  ..    I+D8,.ND.  I .=NZZ+ 7...:8$=ID..  ... MOO=D~=~..   . ? .... .Z O. .. I
     ,,N7 .8?.O     .   .. IM~:,=:.,7  D   ..   .. ..$888   7:8~MOZ    ..Z887~.. .  .8ZM7I.. . ...  .?.?.......Z M .....
 .     D.  8Z N=D .. ..............=== ........... :NN, ...? ..~+~ ..  8+DO~   . .,.O+7?...  N=$M.  N .? ..D: .Z.D .....
        .  ?I.I7=ZD .                             D~MMM 7 .. . D.     :?,. .    =,,M=. .  =NO=ZD+= ... ?..M ...Z.D .. ..
   .     ,ND.,N.I,.::Z...                       D+I:~8~? M,MZ...?Z+.. . .   .O7:.:D,.   =7M+=,.  N ,  .,N?. . .Z N  . ..
   .        .: 8D~ .8Z.8? ........  ......... :MIM?$8MNI8:=M8.Z, O=.....  .8$M.+7... .I,8I~.. ..M7~NMM=8...... 8 D .....
           :..  O,.8:Z.M.D:N~  ............. Z$7NN$M==+= ?78D=M8,M..    :DD8N++... NZ:O$   ..~MMN=MMDMN+Z .: ..Z + .....
   .     +$ I..I~,.:~.~.8..?M877:   ...... 7M$.=ZZDM:DDMMIO=7.N7O8M+. ~,:8OZ7....D~7Z+:. ..,=$8I7?OM.M$7I$I8  .Z =......
         Z. ..  Z  ? M8. .$ZD .?.D:?87DOMD:?I8M7O,$O..?7$M+ 7D.D7MDM8M?:... ..~NI,OM:    I MDI.M8~8I7I +7O~77+ Z.+. . ..
....  ..  . ,N,.+ .=~ IZ,~=$.. N:ND..NI7,OD$MZ?M $Z++MMD,+8,+$D:~:MZ=. 7.7:8I8I~8N..... .Z . . =?:O,NMMZ+~ .I OZ.+ .....
   .   ,.NM..., ..,8... . NM8 OD M,MMMMN~,8,N$I+$OIM MMMN.Z.,DN++:?M,=Z8D~D~7 ?.....,.Z .I ... 8I:M$MMNMM.$.,MZZ.+ .....
      .Z8 ,D~MNND88:::,,,:8ONM$~?.DMD.., M8~ $M$=OMZ:O.. M$.~~.:NM=OZD?~+Z: .. ::M8~..7,.  .   .NDOO:.,+.,O7Z?+8.?D . ..
.      ,..Z D D: .=.ZM=M~= ,.+  .ND.,Z?, Z,ZMOM?~7OM~D= ..?M.Z 8DD8?M ..:OO8O .  =$O       .  ..MO$..Z=N,.,?M=O=M~ :... 
      .  ..D88M.MN. ..O M:.? :.M,.N.=,8$. .MM+7:NM~?NMM~+$    .OON=      88   . ..   .    . ..  M,,===~,.Z~MN=7$M~ M.., 
      .   ..7MMM=~=N=N..~D? .=+7 7Z?+=~ I. 7I,M  M . ?7O.= ~7.M$7  .  ... ,.   .  ...  .   .   .OI=MI~7I,78MMD O$= M.7  
    ..   .   M=,D+.  .  ~.,,+ =. N,, ?N.  DD::  M?Z:~ZNMD?:~D.O.   ..... MM.   .........   ...  $I~MO:~7N:N:+O?NNI.?.D  
              :Z.=:.ZM +~I?7 N.,.~7:DDDD  . M,7 MO=~M? =   +O..........OZ .....................M==== D  ..$~==O7N~DI~=..
  . ..  .   : :~.M 8.MI,,. 7,O. ~8  ?DI.~=$8.O.DZ.~N ~.Z.,N  . .     ?: .. .      .... .     .M8+Z?  =~..I,=7O:O8+~7~ O$
            . ...   .,  . ..8M.DZ  M.7MM,Z.,..7 I=MMM.MID..........M.......... ...........  =,Z~$NMM :MMNM,. O==:~NM=,MZ
 ..   . .     . ZO . $,  7IO.= . 8.7.?MN .M,?~=IM$M, 8I+......   I~ ...... ........... .. $NO7MMD M=M,$.,M?M.?M$?NM=??II
             .  :.M.. ...D$D.:O......O7= +,OM$7+8 ~~IZ. .......:: . ........... ....I .$+MMM?.=N~,+$.I$ZIZ~ D$8,:77=7..O
   .        ...  .I..$...=I. ..8 M= .:.O..$?$: $  $O7. ......$? .................Z,?.Z+ ..~,=?O.Z.I.  ?NI8:$I,~N7INO7D78
            ... ...87+ ..7Z:~?,+ D~ $:??,:+I.:,M78I~  ......7 .   ......... . ~ ,=.....   O:OD=8?I+8D=MNMM. M M7I88D,$,+
   .            .. Z..D  ~DZ   I.M~N...~  :~.DM:=7 .... . ~ ....... ..  .. .+ :, .  ... ..O:ONIM=Z=8Z~ .=$D M7.~.=$7=O.=
   ....     .. .... ..  ,,  ..ZD M$ ...7.$:D.?MIN..      ... ..          ::  $       ..$,$D.O+:DD7:?MD=? ,. IDDDDD8,D.: 
 .           ...+... .7.8Z~  ~.7.7+ 7M=8...$.7.I .  . II......    .  ..... ?...  .   .+7..8DMIDZ~ .Z$77:M ID:8:$I.D   78
.            ?8O7.$+  .+,M:Z+  IIM.+8..D :..MD+    . :    ..          .. D  . MZ?...,   .+.DOZZ+ZZ:7+~MDMMMNO=8=M8N . . 
   .         ,8M,7.   M.7+8$=$ +I M.,ZZ =+,.DI... .~Z . .......     ...D.ZN=.   ....Z+.   O 7N78MOMN~.,N.I:8MD??:$=.D. .
            .:D:~$.. ~O :..: .:8.:=...?., ~$M    .:~.   ..  .. ... .~M$, . ...  ..  ,Z ...~ .:+:7.~O++M.~MMZ+~,=~$~I=:Z~
             . ~,O M..:.~..Z.7.:.    ..? MMZ.....+........  . ...M ...  ... ......  .$  ..=. ..M?IM$MMM ,,I. M.~::DI:$O.
      .     ....+. +Z+:,: 8.O: .8..=Z . .8M~..  .ZD.  ..+++N$.O.  . .......   . ......,    ..,I+?$.8MM$.MD.DMM=Z  ..:7N~
    ..        :? ,.8MM. D8.M..  8~MD ?.MMMN...  ?  ?O.    .,7..     . ...       . ... +    D=D.?M8O?M7M+D$MM:MN.O= .Z7= 
      .      ?D$7.88=M.I.ZD.M  :=M~:.O.MIM... ..~$ .....$I. ....  . ........... =MII$ $.   ZMD NZ7Z87=7MI78$I=.D,? . $..
             ,MMM. .N.M.N.$=.I,=O.IM?IZ,,7,..$...Z: .,. ......       .....,., ~. .., .+   8,==D8ON8~,Z8M~7.7,=~$  $..:..
   ...    ~ O,Z ZMZ~MO:N ?,I $=:.NM~MM$Z~NM8ZN    ~O   .M...   .  .+O~..~.     . .Z.Z=8 =,MMN::MMO 7M7,:N. ~..   ....  O
  M:$.MZ..8M8  8IM7~M,NM=.N,M,D.=M+:MM7MMM.MM?....Z..~N7, .. ~MD,N.  ......  ..  .8M.+=7M.MD?,MZMNDMD:DM,......... ,~,.N
   .?OMDD+MZ8,MO7M?D7N8.Z?N8~7~8~8.ODD8,~INNNNN?  M ..M7,DD$ D.8 ~M .......87.,: :NM$ZZ,8.8NDDD:::77 +:....O :. ?:O :MO?
.    ,=7~MMM: ~OD .MIDOON,7DD7O.8?.M7+.M ,ZMM7M7$.O,  M.NIM..,~D~?=~8~ =NM~M$::==+NO==. 7.~?NNO8OO .....O=    .....+... 
     $MM=$DM8~,87DIM  N ~M=M?77+:8~:=MNNMM.~MMMM?O7MMMM8MMMN=M$8~M.I,$OM+D N~7=M7,N.N$.? $8     M  . N ..  .. . ..  :.~ 
 . ..  :D=$D D:DI$I M,7,IMD.O M8 MZ.IZ88NZM?.:IODDOZ77IM7OO$?M,IM MM7N$7D ?:7~OM8,II..O?=.N,:,I..MM87?..................
       ?M+M ~MZ .~7MMMDM.$MM.MOD+D.MZ..NM?D.MM.MMZ++M:M?.7?,MN~:$D....MMMMM.$.M ?:+M=MMNO7MD,8+.M . ........... ........
   ...M.O+N..N? :~    ..OM+OZN$.8.:Z: ~...M:N$.:~~D+:=DIO8Z ?NZ+7,~O=.=D?.Z7+7 =M.8MMOZMO+MNO.=. .=.....................
      . . ~M,.~:.  ?MZ=N .=~MZ7...7 =D, ... .:.~...=..:,....~I,+MD.+O~8..~MMNO:D$ 8M,D=M= :8  I... .....................
   ...      N....  77$,  .. .O  ............I. .....  ......D NMZ7I+ 7 NI.7.O+~,  II++I7?8 .+7..~ . ....................
            ...7 . ........ .. .........  M........     .   ..       ., ..?7IZ . .  .~.7.  .  ?. .. ...     . . ...     
         .    . ...  .    .     .     .     .     ..  .. .......  .. .......  .. .......  .. ...........................
                                                         .  ..       .  ..       .  ..       .  ..  ... . ... . ... . ..

""")


page57_art = ("""


.           . .     .     .......    ........ ....  ... . ..  . . ~MMMMM$$$M7??.  ..    ....    . . ....  ....    ..   M
.   ...  .  . .     .    ......................................,M:,ZZO.......... .$=.................................. M
. .   .     .     .     .....................................7+ $............. . .:8 $................................ M
 ....... ..... ..... .  ............................... ... O.O ... ................?.I......   ...................... M
................... ..............................  ..  . D ,   ..   ...   .     .   .?.~... .    .... .    .. .... .. M
... .... .....  ..... ...........................   ..   D 7 ..   . .    . .     .  .. 7 D.  .    ..  ........ ....... M
... ..  . ..... ... .... .........................  ....N.D........ ..  .. ... ...  ... O 8  ... ..................... M
.......................................................D O................. ............  ,~,......................... M
......................................................I ? .................... ............7 I........................ M
......... .......................................... .Z= ...................................:.M....................... M
.................................................... I...................................... +.$ ..................... M
.................................................... $= ....................................=.N....................... M
....................................................:.8 ........................ ........... ~: D .................... M
..................... ............................. M  ..................................... O :...................... M
............ ......................................:..D .......... .........  .............. I.N ..................... M
...................................................?..D .....................................,  ...................... M
...................................................?. . ........................................D7~................... M
................................................   .~ O=.............................. .... .: ,M  D.................. M
... .....   ... ..........................$7MMNI.M.:M...N... +:+O:7 .  .D .. : ...  ..I  .I,...N.~ ................... M
......... .........................$M+.$,.O: +IM.+M.ID ...IMM???MM8$7M= ......D$M.   .  .......7.8M................... M
................................ $ I:O ..=.M=.ID,.NI OZ .....78:D= . ?=, ....... O :..,?... . ~+ M ................... M
............................... I$+.=Z~ ..8I8 .~M.ZN..:.....?+.?M=, + .MZ ..  =Z MDMM ?8==I:.=..:..................... M
...............................+OO  ?$,Z.. 78M 78= ,.O :.$MI  .MMNMI.. ? ....8?..MMM= :Z$ ,  DD8M .................... M
............................ .ZDMMMZ. .?M ..:I..+M.$MIM:.. .~8. NM+ MM.M......O+=OMMZ:Z 8...., O~..................... M
.............................IDI . . +7MM7 ..OD IN=??D ... ? ~N8ZZM+ 8.M......       .+ ..... ~.~..................... M
........................... IDMM:O=~ ...~N  ..M  ?M.~N~.D  .,I. . . D..Z........+...7........,?, ..................... M
...........................NII...IMMD?. .,DZ .M$..M..8DDN. : .. 77...   .....,.............  DMD...................... M
..........................I. II  ..... ,NMM.~.~D. M..M::,  N,. +. .I M +..... . .........., = =N...................... M
.........................Z MMNMN? :I, .. ~.M.. D..77 7D~ :ZN ..M  .+ O N8 .,MDD....... ... ,~.$ ...................... M
........................,,D+.....=MDDMO,...8:..8D.,M IND DZM ..8..D~. $ .~M,..   ....$: .~.~.......................... M
........................:D:.   ...... . 8M8MO~~.8O.7O=MD =D8M D+..Z..=7  . ~D=+. .... + O.7........................... M
...................... O,MMMZ.:?MZ........8 MM++ ~?=ZZZMMMM$OZMZ..~..I:MDM+,. ......+MMM,M............................ M
......................? :, .. 7MM7M8MN+I~.,MI. ,7III77?+.+?=M.I. .~OI,    ...........   7+............................ M
..................... =M....   ........NMMMOO...........  ~$N? +.. M$M8.=MMM= . ...?..7 :M.............................M
.................... D~NMMO8:..7..  .....,MOZ ........... :~:$D .  ~ID8?. .  .D   :O7=.=MD:..........................D M
.................... .~7 . .+OMMOMMMMMD===OD8...= ........ $~  +I .. =8MZZ:~=NMN:  . 8.M.:N.......................8+~+ M
................... Z8Z............... ,,M7O.~..I7~~N. ......=MD M88I. .,. ...... ... O=  .~................  ..~ Z .Z$M
...................~...O$$$Z+.. ....    ONZ+:~  ..:,~$.....O,:::DD7$= .... ..,$$= ...:MOMOMN............ ..OMMNI  .+=Z M
...................8MNNMNMMMMDMMMMMNMMM.OM~=DMI .,,,ON8.. ,O:+N .+  ..~MNM~~=MN ....7,IM...~O....... ,IMM8MO ,N ..OM   M
..................=: .................. .I~~8MDM..7,:$D .. N,M  $=I.+:DN...= .... :D NNNMM8$N~=NMMM8,,~N8MIDM8$..O8... M
.................. M.IIIIIIIIIIIIM77.. M:$~:D:~NMM8+.=I... ,NMI.M7$N=ZIDZM7  7  IM8I78 Z :I77 IMMMMMMI7  ... N  +M.... M
.................7 MMMMMMMMMMMMMI7MO$N777M,::=.,......7 ............ .,D.......  ....8..~MII. ..?I7MM8O7II~$M ?.Z .... M
................ I=~    ...    ...... .. M?...........D..............+:+ ....., ...,DNI.MMMN8MN+~:  ...,. ..,+.=  .... M
............... ~ 8.  ..      .        ..M~ ....... .,...............7MMNMDOOM?M.DO .M MMM8N8DN8ZNM$:DZ?:,Z$I O=...... M
................8I====. ==+============+=I~= ...... ..N=. ............8Z ... .......I MMDD8MMM== .       .:. ~7....... M
............... =7+++++++,=+++++,++?=++==,NOII=. ?..... . ..........+ =  . ...:Z?ZM= M+IMMDZ,+MM=INZ8MMIM  .+I........ M
............... .I.         .  ........ ..DO,. II.................. IZ777. . , ...~~8MOZZD.7D~NNI.  .=7M .:?,......... M
...............7+       ..  ...      .  ..., =7, .I ,,  ,=MNM, ....+  ,......... D MMM7NM.N?M, .M$:NMMI..,=  ......... M
...............77ZDO$,7MZO$M8MMMMZMNMMNN$$MMZD~ =D=   .............?MI?IID7I777$ 8=$8ND$.MM,:MMO?..$M  .I7. .......... M
............... =Z ...  ...    . ....... ~DMN  ~7N7?..,..=+...... ?NM. 7.8 +DNMMM.D.M M MN $8M ,N8I+I.:O?............. M
.................MN. .. ....  ..?....... ~..M=$8I+  ..::~ ...... .IN,. . M.DMDM7MIMN7M M,MMM DMM~$  .M$ .............. M
..................~.I.O=:.:... ......... ..+8I8I,..,.Z$$$$. ....:.MM ..:...7:~$: ,7$NDZ MN M7O.D, ,$M ................ M
..................=N 8 .D. :.....I.,,. =MMNZ MNM..7M .,~,, :....7NMO.M...~ .D.. .. .MDM= MM.=M,:,7M.  ................ M
................~:~::.~..=?. . ............ :M8MM=ZM+ .++??$   D:N8.  ...........? .=N=8N N+  IIM..................... M
...............~..O7MN.M. ,DO. ............. +7I=OIII87 I77M7O?~=DM ~........... ...., .   .$M$O:..................... M
...............I ? ..?8 O. . M? ............:.Z+,MMN.+DDDDNDMI ..MI.?$ ............... NMDNNO=MOM..................... M
..............$. I .. 8+.= :,. 7,........... ~M,I87N..   ..~=,, :I .?O:,............. ?.D=~:.8+$$7 ................... M
..............M.:.....$MN.+. D:..............8 ~IZIMO=MMMM+MDO  .M...I8, ............?...$ 8. 8=.I.................... M
.............I. 8.....  ,O,: .77?=......  . ...M7~Z.      .?M?.  M..I$7  ...........   ON:~,...$.~I................... M
.............M  . ......+~$= .... DD ......... 8 .7M+: .ZZMMD.. :+..:8,. ...........:. :$$8.....?~M .................. M
............ ..7........ZZ: N..I7?.. :.........8 :$ ~NNNNN=~D  =M.. I,:.............. I8,,,.....N78................... M
............ . I........:,~8 N., ,8N=ON8....... ,?$ .  ... ~,. .$..+ . .$$:..........NI.:?......8?,N.................. M
............Z   ......... ~~O ~ $I..,~:7........Z7M?MMMMI7MMN~. M ., .I77I:=......... MIN  ..... ~ .. ................ M
............D.,=.........~8$I.Z..,.I+:..........M87  .,OOOOO~+ :M...I~Z.. ........  888$N ....... ::$ ................ M
............? Z .........~:. M $.$8$............ZZ.   .... Z.,..M. .  .. .......  8I .78,........7,$M ................ M
..............M+.........  :I~N?,........... =NN?I.=..=8$O,.8....7,O8MMMMNZOO::.. .Z..?O.........:D7??................ M
.......... . .+7...........Z$ N NMMMMMMMMNDDD8D.$ ..   ..........,..N,.OM:.D8 :?N$.,:. ..........?.,,M................ M
.......... D.. ~........... .M:+..7 Z,.D?ZZMM8~   ............,.O  .D.+8Z.+DI.,~I?I?Z?............ =$M................ M
...........M.I. I ...........  ~ I.=:.?I?.,:O.  ............... . =.      . . ..  .. ............ :IO$................ M
.......... =.I... .................I..,... ...  ..................................................DI+.7............... M
...........: I.=.7 .................................................................. ............D. I7 .............. M
.......... . I .78........................ ...  ................................N=7.~ =.,N........ ??8M............... M
..........7..I,,=D: ..... ...... ... . .......  .............. ..............$,8.,.+7D8O~ =N~..... DO?7 .............  M
..........7..+.:=D .......  .... ........... .............................. +8$. . Z7O  .7:..~.... 7= I .............. M
..........M... .OI.,.......:I:  .............................................. IN. . ...= :~:O8Z...7.I?............... M
..........M...:=8 .D...... ~7?.I=.N=,..... . .  ..............NO..I. .I ......... ...?7. ZO, .. ...M+I8 .............. M
..........M.. =7I ??....... I 8I .N~,,.IZ7  ............. .. O. = ..7=.+:,...........: .8:...::I:..7.OI............... M
..........M.. II.,~$..... ...+7. 7Z?~:.=~.~O..  ...........~..~Z .7=..8  =:Z.................... ..7ZDDD.............. M
..........M...IN~ ~8.......   I :  . ....................... .Z..M? I+ $Z, :.=:....................77NDN.............. M
..........M .,DD .I+  ..........  $ .I. ~$=.:~ :7.. .........:.=I..Z. $,..,~Z7O: ..................MD7,N.............. M
......... ?..7:= ~7: $... .... . O.~..=8$DO$D$8DIM..,,...........:I I=. +?DO7,..,..................M8. D.............. M
..........I. .+8 :7 ~?...........I+I ?Z$O:+OI7+=?.~ . ............ ... 8D=ZZMN ................... OI  N.............. M
.........: .7.+I ?+ :Z$......... MN$=O:   ~::ZDDDDDDDDDD88DDZ8DDDD8::.. .Z$88O.....................,I,.M.............. M
........ M.  . 7.I=  ,O~. =~7D?..? MM~.:M8D =Z ~I.7I $N: ,=D8 ~+M. OMNN=~,=MM:  . . . ........ ....I$NMM.............. M
........., I7 ~~.II,.?O,..,,+?$I~.Z=DI7++,$ ,I.I?ZMM7$77I.    ............$$,N.88.,ZI.~+I I8,.O? =,OM. IM ............ M
........Z. ~?.?,.7~ OZ$~,:,O8N+=?,.Z....  ..  .............................DM:.=Z,:$?.D=,~8:.+D.,.+88+ O7............. M
....... +...I.IM .I 8.,O87N. .M7$..MI.. ..................................~$:,M .D,Z:M M:M~~I~I.  N$ZN M7D............ M
.......O. 8,ZN=....N...~ M:.=Z,M I..M..8.. ............................  +,.Z+. .?MM. I=M$,, M..88 M..+DDM............ M
.......8.M O?M ....M ..,.8: .. M  O.N8N.+.....  ..................   .  .+=:.? $.?M?7 INM+ .=M.8 .:M.M7N,M............ M
....I.,D.: M$M =  =M ~.~.M: ...O....~M.N87?$?$.................... .. ,~O=M .M.O7?M?8 M$MO, 7M ?, :M+ 7:=M. .......... M
...... D: ,:.M,7 .=M.= ,.M~8..IM,...~M.N88+, ................. .?.,ZIN8DD :~ M~I,DM.DZZ+M.~.?M,.+.:M$+I=MM,~.  ....... M
....... D.I.$M$I  =M,$7~ M8$ $$DI...:M.~:8..................... . . : ~:D$:~$D,:+$M ,7$MM+=.~D~:$.8NZ?$8M:78~ ........ M
....  $D+.:.$M8Z ,=NIN=:+M8D. ?M8...MI.NM8. ~.. ....................... 8:NIO+:..OM.  M7M$I,7M.D+.8MZMM?7 ,. ......... M
 D::..ZZ+:::IM=D?I~M Z$ OMZ8.~ZMDD. 8M.D88 == , .:?I ?. ................M=,+~8+:.MM: .DMMI+,?D.:: ~ZM~7MI..$88~  .O$~  M
,$~, ++N$Z ..MZ8 I~M+?7 ~MI, NZM:~ 87M.I$N.II7~II7.................. .7=~7Z?7D,8.?M$+.:=M::ODMI7M IMIDZM~ ,D8I ,=7D8.. M
..  . .  D.:.MNM=7+N,=M:~M==,:?MZ.8IDDMMM  ..   . .............. :: ?ZO:.?.~??DNDZMDN.NNM+?MZM MDM8MD$IM7.,D$8. . . .. M
.. 8....  D+IDZIDDNMM7ODM8+O?:$$M?=M:DNM: ...................: ,,8,= .:7.,8OOD::?,MM7Z?+M+OODDMI7:M:D$78+  :   .   ... M
.......  .  ...ZDMI .OMM~.,MMN ..ZZ ....8..? .................. = 7:. ~~ .+...NO=O..M+M .~MM,  MM+   .++DZZZ... ...... M
... :???MMMMI~ .... .....?N. .~OM~I8I ..I7. .................... :....M. .. .7$$$$OMM$ M??DI?. ....................... M
......................... ..  ... +=......................... $..............  .   .,.$:+=~ .......=.................. M
......................... .... . ...... .. .    ............. O.,,....,, ,=N~.    .........,,.............  .......... M
""")

page61_art = ("""


............................................?Z..I...~ .................................................................M
..........................................Z.M..NZ..M...................................................................M
...........................................   I$ .I....................................................................M
.........................................Z...,I ..$....................................................................M
....................................... Z..M.?...N........................................... +,.. ....................M
.......................................  :M IN  .,........................................O.. .~.,.....................M
...................................... M.Z~ ? ..M...................................... 78 ..7O. 8.....................M
......................................=.  ~IN..  ......................................O  M I?..M .....................M
..................................... N... =~. O ..................................... ,...:~+. . .....................M
.....................................:. ..:8. ~ ..................................... M....8O..D ......................M
.....................  , .  .  ......N =.:. . $......................................$   .,+ .~ .......................M
......................       . .,+ODM =M.:D..,. .....................................= O7.=$..Z........................M
....................................D..M?~ ..7 ....,::::ZZI8~,,.....................D.D..,O.., ........................M
...................................: ...?D ., ........................ .. ???ZD$$$,.:Z   ~=. 8    .....................M
...................................O ...$.. +......................................M.,7.78... I77$MMMII7:... ..........M
.......................................N+ .$......................................~.... 7. .M ......  .......    ===~..M
................................. O Z8.$.. ?..................................... 8 ...8$ .I ..........................M
.................................., I NO..8......................................., N:.~...M...........................M
.................................:. N,I...$ .....................................Z I, $N.. =...........................M
.  ..............................D...+D. ,...................................... I7M..I:..O............................M
.....................................~Z. D........................................~M.,M...N............................M
. . ............................7...:8...,......................................M. . = . ..............................M
............................... I.Z78D..$ ..................................... I...:Z . 8.............................M
...............................? $,.,,. M......................................~.   8N...N ............................M
.. ............................$.:.=M . . .....................................8.8    .. ..............................M
....... . .......................  MD .N  ..................................... I. :D...N..............................M
... ... .  .   .   ,,,DMNNN~I $ . . ...M.      ...............................M Z .N8...7 .............................M
.........    .    .$ZZ?M+?+:+ ....== ..,.   .ZZZMN+++....    .................+..Z:, .. ...............................M
.....................  .. ::~N,  .ZO..=~::~7MMDDDZ ,    . ....:::::N:DDDD+  . .  .7: . M...............................M
............................ .   .= . 8.......,..................=:===MMMOOO8. ..==D ..?==+MMMOOO:.. ...,   .    ......M
. .... ......................O.NI ~ . $.............................. ,,,8OOD:D.. .,..:=,D:N8ON8N:::::...   ..,:~ODOND:M
............................ D7O.+N..:..................................... ? ,Z,?, ..=:.:::,:.....         .  ::~::88$M
...    .. .................. ~+Z OO .8..................................... M ?..NN...N................................M
........................... I..  $, .D..................................... Z.M. ,8 .,.................................M
... ... .    .............. M....?...~........................................NZ.,: .8 ................. .   ....... ..M
........................... ?.. .8...:..................................... ... ==  .N.................................M
............................ O? 7$..: .....................................$..  ?7...=.................. .  ........ ..M
...........................O ~ .M$..M .................................... M..8.MO..:..................................M
...........................N.$  7...D ..... ?~=........................... I.+. $O..D..................................M
.......................... =...   ..D .NMMNZMIO7=~:8 ........................M ~ ,..N .................................M
........................... ...+7 ... ,O$OMO8ZMM=O=~M....................... NZ~?...~ .................................M
..........................,....?7....8, .N.D?:MN7NM=MM ...................~ ...??...,..................................M
....  ... .. .............. .M +7...D..+., D+ZZDMMO7:MM$..................N....8D......................................M
.........=7,.$$ ..  . ....M I..ZM :.M7$. .,7 .. .,MM, :N$+.. ........... .M =Z.88. : ........... ........    . ...... .M
............ ....   ..   .M.?..ZM.OZ~O=.M  .  $MM,I.,ONMZO$ ..............M.Z .D$. ~ ..................................M
..........................M.8M.ZI?N+ONMM$ ::.MOMOMO  +,M:7MO............. , O,..~. M .....................  ...........M
......................... .....8M:Z,+=MMMNI .+DI 8?Z.~, :+M.......ZZZ7M?=+,. . ~...D  .................................M
......... ................ ....+$O~MMMMM.:MM87.:.D?  == ,=Z .............,....7~.. N~~+M888? .. ..    .. ........... ..M
.......................... ..~ ?I$7N+?  ....8M$ . I ?..D8=$M ............7  8 I~ =M+DIM=..... ...  .    .~++OZZO    ...M
.........................Z O$..Z7$MM8Z ....DM,:DZZ.  ,~=OD7  . ......... $. D 7MN8N=8NMNZMD   .. . ......... ..........M
.........................Z..  .MO~OOD .....M:7MN.M$MD$: $D?  . ..... .   $. IM$ZDOO?N8MDI: NDN . . ......    ........ .M
.........................N.+  .87OOOD .....+MM=7M 8M,7M:   ........ ..  .$ =M7877MI:7,M..8O ~?+ ....... ...............M
.........................8..  ,8M.I8..........$Z :MM?Z.M? ...............D 8DM ?++..$NM8ZN=7M$O........................M
.................... 8. .$,ZZ. Z. I ....  $.:D...~MM,.MI. . ..........  :$ $M...8... N7==NM~$M7........................M
....  ... ...........,N,, ....8...,O Z..~MMZNMMM.D..NN:=~..M ..........8.$.DM  ....... :MM87?7M  ....... ........... ..M
....................M.  .... D...=7 ~ Z...  +. 7?I.:    Z 7  :.......... $ $ ,7MN$...,8. NM MN$. ......................M
...................I ........~... Z.D?.I. ..?M..:MM ..... ,N ?........ :.$.O....,  $MM  .D,OD , .................. ....M
..................$....... . ~?.. .$ ,.88....~= =M$M.....  ~$,..... , .. $ ?.. $. ..NDN.  O?N ,  . .....       .  ..  .M
....... . ..... .7 .............$. M .+. D~.. +$.8:8......   .+. 8...ONMN$N..., 8D$.... N8.MMZD .......................M
................? ..  ...... .OD .,~.=M .+ $.7..D  ....?....I==.N  ~DND.. O?.... ..... 8MMM 7M $ ......................M
...............   ..  ...... .$ .. ,N.M ZD ? I... M.....  ....MM  MDOM~,:MD7. . ?, ...~DI  . MZ D......................M
............. .D....?....... .Z ...=:O . =.~::...:=.... ~,...?O .M.MMI7,8?.D..IN.. ..M7$I~OMZ7M$ :.....................M
............    ....?.....  ..   ....M ..O:.Z....?..... ~D....=M?8,.~I?7..  Z   .  $88MM7=Z~MMDDI  ....................M
....... . ..?.M.....? ..... ..+M ....8 ..ZM.=...NZ....  ? ... N D,Z .~MN:   ..:,,.  ..  ...?7? .M.. ...................M
...... .... .,.....  +.... ...? I...., . =DM.. :, ..  D ~... N~N. IO? D=O$=: =7+,:,Z+==~7D$O+,87DM.Z........ ..........M
..    .  . :.? .....:.+... O....:+8ZNZZZ$ZMOOO.OZOZZMO?O+....8O+$  $O?M,.+Z  .=7,...Z=Z:+~IZIN7$.I.M...................M
......... N.D .......=DMMMNO.... 778IMMM$D=MN8M..ZN~MZM ~ .. ?O N . ~DMO7? .  ..      .. ..M$7:.?NMZ. . ..    .....  ..M
.........? I......... ,.~I .....  Z,7$O$$MM=.7~........:=.... 8 IZ$ . ,?7INM$?DD8=ZOD++,7D:M  +D:$M.,  .           ....M
........ OZ  ......... MM.......... $~?  8::M...........$.7 N :IN::Z:M  ?. ....N,DOZ+=::I=O$?$NZ.=M.D.. .     .     . .M
.........8...... 8. .  M,............I N7ZID:.......... :$ .....IO.7MMM........O ,:.:.. I+ N7$=. =~.N...              .M
.  ......7........ ..NIM..............Z.ID ?..........  ZM O..   I. =D  , ....  ~Z77 .  ... 7 .$~. 7..                .M
.........:......  . ~+: .............. ,.DM ............ M.=. ...M+OM.  .   .... .N.. ..... .M~O .. ....              .M
..........= .....  =. DN...............?.DM............ .O M. . ..M,..,+. . ... .,:   . ... 7M   ..,...               .M
......... O.......... 8N............... ,,.............. 7?.:   ..:M  .. .  .... ~, ..  .... =   =, ....              .M
...........: ........ 8M ...............$ :.........  . .O8.. .. OIM? ......  .  Z?.....  . . ,:7...  .               .M
........... +........ D...................N ........    .=Z  .= ,+$. ... ..      ZO  ..      ~Z....     . ..        . .M
.............I ...... D .................7D............  =Z ...7M+8,.~..... ... .+. ... ...  .M.... ... ..... . ..  ...M
..............~?......D...................D...............$ ..7Z=D...~...........+ D .........M.........              .M
................D.....D...................D.........  ... M .$Z..$N.....  .   ...+ D  .   .., M.  .   ..              .M
...................NM.O...................M ............  M .  MN.O , 8 .........+ M .......$ Z..........           . .M
.....................:,...................M.........    . + .Z.M.M  +  .  .     .= 7. .     7 , . .                   .M
.......................D ..............,..:...........D .   .Z .M   =.... ..... .$.~  ..... M?... .....       .       .M
.~MDMMMMM8DDDNDNDDNNDNDD... I......... N..~............  .:~:MMM... ....... ...   .M .. ...+.MMMM+MMNO:MMMD:MM. . ... .M
.................. $ ..=?...D..........N............   . Z 8  = .... ~..  . .......N .... .MMOOOO8888O888OOOOO88OD8N, .M
................ :... :.,,..:.........., :.......... N..,.M, ZMI.... ~..$ .........D  ... .? ...? .,....          D   .M
Z .=7..O .IO.+~ =Z ~O.OZ,M . ..........N : . +......,:.7=. 77 O = .  O..$ . ... ...= ..I. O.+$I8.N+ ..+M  .MN ..M8.  $.M
,M  NZ ~D..M. DI :?.=D M~.M..+.........N : ,  ......8.8O8...ID M..Z. ~. :.......  =    + .M. ,M?.  NO  .ON . ON   OM .IM
.=M. O..~8..+  +  ,=.=N.N .7 . ........: :., ?..... =N..OD...I +.N  ~?MMM?,.......8.  :,NMDM. =,.~ . $~ .:$$  .8~.  8M.M
. $=..$..O=..7  Z .ZM.7N,M,:. $ ..........  .~.....N?M8  IZ .~I.?.OM.OMMMII.7$$7MMMM7$II$7. O$.  NO . 7+O. =M.  .7. ..NM
O  ?  :M. M  +N :8 .OZ.$M$M:..?  ~$$$$DI?D+???MZ$$==.$D, .7,  I$. .,O~~ $..... ~$Z:7.  M+ ...O8 . ~.+  .8Z   7M   :$. .M
8 .,N..N7..7,.N+ $7..7  M.Z$Z$7$7$$$I$$$8MN?: IMD$=$IM$..=?..  D...$M .. :  .....,I.. .O. O .MM.. .M,I .=   . ~ ..  . .M
+8. N7. 8...=.,M..M..~N.8==8..,.........+ .D .....M.=N        . ..  : .N  . ..  . :   .  8.  .    . . ~,              .M
.......................... D =. ........I ..$ ......,=Z.. ... . ..   N~,. . .. .  O  .,8.. ?. ... . .  ..     .     . .M
.........................=. ~............... :......  , . ...~..   ...+I  .   . Z:,7ZM,7.., . .. ,.$..                .M
........................: , $................ .......=  ..  $,....? . M.D?ZDONO ?~     +:.. ...I .. ... .O..          .M
..................... 7... O  ............. = ..... Z+,.. .?? .. ,...,:,N, ... . ,:...  .8M888MNMN~DNO=~=~~=~,,.. .  ..M
 7..Z.O8,88888OOD8M8++M~?O~O ...........  D,O.   .IM~..N ............ :N+....... M7 .. ?N8 ..............   .       . .M
............................., ........ .:D..M$,DM7M,.. ..   . .... .  M+. .   ..=:,.:M.?O+ ..   . ....  ..  ... .    .M
............................=.$M~.....77=.M~...O~. .N .~,..........  77MO  78M7NDMD M$  8~M8M8MO$$7IZDMZDZI~DDMII     .M
.. .. IIIIIIIINON8MMZMMNZ777?Z~..Z=MMIDI..N+.. 7.....:,+MMMIOZII7OMMM$M7 7M ...   M7:.M7.,..  ... .....               .M
... . NDNNDNMM,M+I,,,,,,,, NMO ..D. . M...DMN.. .......M. .. .. ..... ..Z.MI  7M.NMMM. N.8  . .. .. ....              .M
..........................  7 I  .......8.8II ..... ?~?O    . .          Z8 .~$~=.,MD,Z..       . .           .       .M
............................$. .......O  .:$7$ .8 .N+7+.           .    ., .88O8,.7        .           .              .M
..........................M.8M......  .+I7..8$=MMM+ZM~. ..  ....... ..  ....    ..  ....... ..  .......               .M
..........................  8.M   7:.ID.8.N.... ?:..  ... ... ..  ... ... ..  ... ... ..  ... ... ..  ... ... .     . .M
..............................D7NM+M+D: ,= . :.. ............ ........... ........... ........... ......  ..          .M
................................   :Z:.................   ... . ...   ... . ...   ... . ...   ... . ...               .M
......................................................... ... ....... ... ....... ... ....... ... .......     .     . .M
......................................................        . ..        . ..        . ..        . ..                .M
""")

page64_art = ("""

  .. .......................................................................................................................................
 ...........................................................................................................................................
 ........................................................................................... ....................... ... ..........   ....  
 ........................................................................................  ............  ............... ..... ....  . .....
 ...........................................................................................................................................
 .......... ..............  ................................................................................................................
 ...........................................................................................................................................
 ........  ....... ... ................................................=== .................................................................
 ..........   ..  ... ... ...... .. ............................  .N? :    . N8  ...........................................................
 .......       ...        .. ... ... . . . .......      ........+7.DNM. ..=,=OD:O ...........   .. .........................................
 ....... ................... ...... M7M MM8.  ................ M.IO=O~~? .. ?D: $.= ........ OMIMMN= .......................................
 ....... ............  ........... MZOIMM:OMM  .. ...........~7 N+ 8  8I   .IDZ8=O D.......,NMMMIMMOM= .....................................
 ....... .........................MMMM  M8DMM$,..............?.7+$?8  IM,.N7:7+77MM=7.... ZMM8NMMM7MMMZ.....................................
 ........  .   .  ...  .. ..  ...MMMD .. 8O.MM:.. ..........M..?M~ND. O?$+:,,:,++N=.M,...I$MM+ . M .MN?, ...................................
 ..............................N,MDM .... 7..M............ ,N,7:??.O$Z$?8  D8~D..=.+I ...DMM$....   N$M ........NNNN?  .....................
 ........      . :MMMMDD,... .M$NM?M $M  =M$.MDD8O... ..... M= .. ..I:7?~N~DDO:   . .~...OZN. .D..D$..M.......MMD=MZ8DM~....................
 ....... ..... NIM?MMMMMMM... ~8,$=D. .M.,. .~8MZ8N. .....  NZ.........=+NDD .......~M:M+=NZ7.DN, MN:..N7O..,MNMMMMMMMIM, ..................
 ....... ..   MMNMMMMMM$OMM .D=,  NN .MM$+M=.MIM,,.O.... . DM.  .  .....$.7. .......$M=8..=M....8.+.. ? =.I.MMMM MMM..MMI. . ...............
............ I.7MZD  ZMOOIN8:~N .8 :MM.8M$.OMIN ..8=,.... D.  .$.+$?   $?NM7.. . .+$. M .D ,.  ZM8MZ.$. .~=.NM  . $8~. MMMI7O .. . .. ......
 ........... M+N..... ...$MDMM., .D ?7 .87 M.:  , ?  ....:+M .. , .. .88M8MMM:. .7MMM=:I.:..8...DO...MZ  ~. 8O ,M  .=O $M$.  OI8.8== M .....
 ....... ..M,MM:.  . . .  OM+ ==,,..MM=MMM M N NMMM.Z ...8:...8  MMM,87... ,  ..M   ...M.D,MM 8O.+.7D.M.....M. :MM .MN..DM. 7MO.... . D8 ...
 .......I,M  7? ,OM.,MMI..O7M,.,M.,8 . M MMZ Z?,  .., .?. ~.,.  ZMM,,O ?..  .:M,.+  ..:. :7:  . MMNM.78..8.Z=. ..Z I, ..:I: MN ...... ==M...
 ...... MO . I.,. M,.+. ..MI.~8,=,.:M? ZZMIM.? MM       M D+...MMM8MMM M..,. MMMMM$. $+.D. ......MM$Z...~ ,N Z.. ?M7=...M..~M. ...... DDM,..
 ......8, $. ZI: ZMM?MD..Z  II .?M...I.8 M+. I=.:.... ~  Z.M M+.+MMMI8?+...M ?ZMMM$D$ .7... I.7   ?~Z$ $...?.8 .?DZ+?M ,I?:+M ..I..7 I7IMM. 
 ....  8.    .M,7:IN7?.~ =:M ....+ .. :.$M  M?,? ~ ...= ..=+.+.....OM  +... .:7... ...~I... ,. Z  7..?O..M. ?.M.. .... N,?:MM, +I=.N~7: NOM7
 .....M ...?+..M.. :Z  7II= .. .Z.. .   NM+,...  ~   .8 . + .........O.+... NI ...... 8 . . ~...   , ,=  .~=. .O  ,..=D7N~M8MO ~=$.7 =DO ~Z 
 .... ,I ... ~O NM.  :OMM:... :M:   .  .ZNMD....D N  .... ++.... .. 7  ?..,. :.  .....8 .?8 M ?   ..  +...   ?M$M$$$DI: ,.I.O.:.MM,.DM=  NM.
 ....M,+M:  . .,8.NM,.:M... =M8  7M.  M... N...  $ D  .  .7M ..    . +M7? MM7D....  ..M=...M:8 .   ...+:$ .O..  .+,M :...?NN~ .. .. ....,=.?
 ...D7,. Z=,O= Z.OZMMMD. ~O? ... O8: ?..   ........7,M .I .Z...  ...D . .....~ ..... 87.:  Z8  ... ....Z,$~DN    ..M.: ...DO:M ..ZODO .OO+=.
 .  ~,...   Z :~=,Z~OM .D..N+ ... ..N...,.D........ = :8.,.IN...  .7 .   N .. D? ..+.MD.. D8...... .....O 8.N .....M,: . I:~7MM .MDD8N~?M=$N
 ..DO ....... +,$Z.~7.+,.D   ......N?.M.............. $ .88OMO...~M8.  ..  ..~O$Z.I O88D,+?........... 7.$.=8... .MMMM .. +:N?MM..8?D.:~DO$ 
 ..,Z......... ..O..M8. O ... ..    .OO..8?:...  .......=. ?$.+ =8 .?8.~  =?,.O~?  O.$MM.   ....  .. ,:.I, O....  ~M.,IM... +7MMD+.M8NMMDI  
  7.,....=......  OMM .. .... ZZ ..,.$?M,.~ ............ .....7M $.. 78 +?. N,.~,O8Z?M: ... ....  .=...I  :+. ..  O..  .Z=Z+.~ Z+MMMIMM? :D 
 .O. ...,~ .......:=N ........ N .....7MM8.7+  .  ........... ~ 8. ...?.   .= ...,.8I...... .....   +O7. .M .... Z~........+D, .D=8MMM IO=? 
.,  ............  ~=: ...... . 8 .. ..NN..I:  ,8 ..  .... .....:  D... 78D?..... M+ .D  ... . :7..M  MI,M N:.... Z  .    ... =O. DMMM:Z.8...
 8...... .........~M:........... ... M 7..I. M,    7,  ......... I 7  .... ... .M ,. .  .  Z .MZ. I+ . : .~,.....N  . .~8.....=7, MM7 $. ...
8 ......$.. ......~?:......... .,..,, ,...     ,DN....:IN.  ....  D.?. ...  ..~. Z. ....8 .N,  M, .......D.Z.... +......N.......~M M  ......
~.......$.. .. ...~~M  .. .. . ., , 7  .   . .  8$.. =MDO   N.. .  $.8?. =.8=8. +.... ,.M. Z  ........... 7.N ..I......,........ ?$N .......
 ...... =.........~=N......... ., 7,....  .......   :I7...  II 7 .. ~ M:.?8 D  = ....7.   . ....  ........ .:...M...... ,....... .NM........
 ......  ..... ...NMM............7 ...................  . $$.  Z=Z..+ +MZ+?I: 7 .==Z..  ... .  .  .~.  ...   Z..7.  ... N....... . N? ......
 .  ...~..........8M~. .. .. . .........  .....  .........  .=+. ?:I.= NMMIO.=. +,:..... ....  .  .., .... ..Z..7...... N....... . MI ......
 ......Z..........DM::... .....O............ :....M................D$,.:MZ8   =,:,....  ....... M .7.........M.. ...... N.......  ~7?:......
 ......=........ .,=MO...... ..MD.......  ..   .. ~.............. :..$+.ODD..DM. .......... ....I..I.........+ M ...... N....... IOZ?~......
 .  ..:  ...  ....:=8M ........O,......... ...D..~.  ...............I78+MND.:M8 +.  ............M 8...   .....7D .......N........INOMM......
  ... M....    . ZD8N= .. .....8 .......  . ..D  Z.. ............   .~~MMZMNM,M. .....  ... ....M= .......... 8D .  ...,.........7Z~MM......
 ...... .........MM,:~........,~.............. D  I  ........  ...,O:~8:MIMMM,N$.... ... ... ...D. ...........=D ......D ........ ::IZ......
 ............. . =NI:. .......D. .............., : .......  ........ ~ 7M=8M~8$......... .. ...+ .....     ... 8 .  ...D........77~=?~......
 ............. ..+D+:O........,$ ...........  D = ...... ....  . ..+DMM?MDMN.MZ............ ...+,......    ... =..  ..., ...... =$::?+......
 ...... ...... . =88ZO$.. ...8:.... ....  . ..D M .   .. .......    .MN MMMN D........  .......,D.............  $...............,N.~?8......
 ................=M=+O$.....?.: ............. : M............... ....8 ?MMMM?~8...  ........... 7O ...... ......I ..... Z......Z7=I,88......
 .  ............  $=~O$.... .:.............. O ,, ............. .  . .7DNMDMM?8......   .....  .M:.... ......   .M. ... 7..... ?8IO?DI .....
 ..............   7I=O ..  +I............. . = ? . ................ 7~?IMMDN.D8.................I Z ............  I.... N...... O7D+$  .....
 ............... O:ZZM....+.............  .. M N  ....... .. ...... IOD:MMND O8  ....... ....... OI .. ..........? N... N...  . =7Z8,~:.....
 ....... .........:,ZD...7. ............  .. =.7...  ........... .. =ZMZM~8NMDM...  ............ M ....  ....... ..7NI:,......  Z=Z?~:N  ...
 .................??=7.. I....  .....  ......~.N ..  ... ....  ....$. IM.=8MDZ~. .  .............=.?.. .......... MMM .8N......I~NO==D: ....
 ...........   .  8O=...?.....  .   ......   M N.     .. ....... $,7. ?? =+N=:D. .......... .  ...7M.......... ,MN...:M=:, ....M=?Z,I8, ....
 .................:=N ..$....................O :................ .M.IMNZM,?,+.M7..  ....... .  .  D7.........=:. .  .  .=M:....7+7$.IZ......
 ...................  . $...................,   .............  ...N I$NNN$,.M:M7..  .... .. .  .  M$..   .  M  ........... M  =. 7 ,$ ,.....
 ......................?  ...    . ..... . . N. ................ ==7+= ZM$,.MM=I: ...... .. .  ...?7  ....?..... Z.  ..O.. 7:DM.,=.,?.. ....
 ...............  .... 8 .....7778:.......$ ..:. ............  . Z .7?8Z7D?NDIM7O   . .. .. .  .  I.,  .=,    87.+$I... M..D.,+ :~ +=.:~....
 ..................... M :MMMM......M:. .O.+  8  ............... ?=..88M:O=M,M+7Z=.  ............. ,..~...  NM.....M....N..M  7+~ .:= . ....
 .................... ~NN?.. :....  ..,,?..=:ZD  .....  .....  .8?8M.:~M 8=+~+Z$,: =.........  ... ?...8~~ND8888I,,N ...,..M..O?............
 ...........  ..  .88M. M...D.   7.D.  . ,?M ,D   .  ... ....  ..:D7=DM?.=88MD+?II......... .   .. ?  ...+ :.      I8 ..,. M..ZN............
 .................Z ,. D ..I...... .ZZI ....M................ ..I,.Z+8+NM,7$Z$=O.M= .............. ?8 . M  ....... +N  .D. 8 .~+............
 ............... ?.:7.?...+= ..I7II77777MMM. D........... ..  D$I 77878+7D=IN88I.+$,.    .........IM 7  =  ...   ..~~..I. D  8M.............
 ...............:=.M.= ..: ...D.,$. ZZZZZO .M: ............. IO.~M I7?~ZM.$?,=:7+7?8....... ....  ? , .:=..... +++7O ..Z.+: MM. ............
 ............... ,:N =,  7  ..8 ............ M   ..     ... D ,8=I.7D.7,D=88,:Z7.:Z+,..........   $.8,.:= .I,ID  7.I..,..$ = = .............
 ...........  .....MM ? ..M ..=~ ...   ......N.  ......... $.... ......Z .~,D~N. +? $...... ...... ..$  MMMZ ... .M  8?MD?+..M .............
 ...............  ...M.$.  7 ..ODNNNNMMMDZ ..Z.   ......... .....  .....  .... ...................7...M   N  .....,?O  ...... ..............
    ...  ...   ... ..O  M. .+ . .~.....$ ,N..M.   ... ..       ..  ..........  ..............  ...= ...N  .7IM 8..   ...... Z .....  .......
 ....  ....... ......,Z?$~.. DMM....... . .:.................  .....  . .. .......  ....... .  .   ....  M, N. I$...........................
 ....................    ........... ?IOZZ: ................ ....  .....  .... ...  ..  .....  .  .... ... ~N? D7...........................
 .  .... ...........................$I. ......... .............. ..... .................... ....  ......... ...M......................... ..
  ............ .  ... .   ...........7 .  . ...... .. .. .  .... ...... .....................  ....... ........  ..................... .....
 ................. .............................. .....................................................  ...................................
 ..................... ........................  .........  ..........................  .....  ....... ................  ..........   ......
 ....... ..... ......  ...  ............  .........  ............  ........... ...  ..  .............. ... .................................
 .....................................................................................  ....................................................
 ...........  .............................................. ......................................................................  ..  ...
 .  .... ...   ... ... .. .. ...........  .....   ........   ...    ...    ..    .  ..  ... .  .  ....     ..... .  .... ..........  .......
""")

page66_art = ("""


 ........  .  .........................................................................................................            ...   . M
....   .....   ..........................................................................................................     ..     .     M
........ ...  ..  .  ..................................................................................................              ..   .M
..  ...................................................................................................................        .       ..  M
....... ...........  .....   ...............................   ..  .   .  ...  .. ..  ..   ..  .   .  ...  .. ..  ..   ..              ..  M
..................   ....... ...............................   . ..    .   ..       . ..   . ...   .   ..       . ..     .....     ....  . M
............  ..     .... ..................................   . ZN+   .  .       ..       ....    .  .       ..       . ..    .     ..    M
..  ...  ...  ..     ..      ............................... . ,$N.:M.        .   ...           ..        .   ...             .          . M
..  .... .........   ..  .    .............................. .Z +:+:.=..     . ..   .      .             . ..   .       .       ..    .    M
..   ..  ............ .  ...  ............................  OM~ .   ...7 .                                             ..          ..    . M
....... ....         .       ............................ :7  ,N+  . . ~O.   .      .           ....     .      .          .  ..  ...    ..M
........ .. ..       .   .    ...........................Z,  ........    ,:         .                           .                    .     M
.... ..  ...  ..              ..........................:~ :~~~~ ,:.     :~I.                                           .     ..  .  ....  M
................      .      ........................ +  ...M..  :. .     :.7.                                         . ...... ......   . M
................       ..... .....,. $=777 ........ + .    $IMMMDO? .  .... . ~.. .. ...   ....        ... .. .. ...   . ......... ........M
.......    .  ..     . ,7,... ............$~.......,....= .=         .7 :. .I$ZI.  .                                       .  ..  .  . ..  M
.....  . .....       . .,.    ...... 7. :N+:.:.,,I.M... .:::$ Z.   O=Z . $$Z  $ZD,. ....               .   ..              .  ..  ...  ..  M
.....  . .. .. I $. ZNO+ .   .......... ... ....MO=~+. ..ZI,,,..,,  ZOZ$+.      $=I=   .                 =.       ..   .   .          .  . M
..  ...  .. ....            . ..II77=?~..... .$ ..   ..=I$..        .$.~.?~.+=$7$$$M ....            I,..I.                                M
.   .... ...... ..   .      ............    =.  .......?,++++++.....:=+?.8 ..M ..  DZ~ .....7$:........ZZZ$..  .Z=.+=   .  .....  ........ M
 .          ... ~~+~NOO8OO,.   ~,    .,.:~:~ .. .....,O,:......,.    7        ,8,+  . =    .$Z..                  ......   . .     ..      M
..   ..     .  .. ... ..  ..   N.+D$=  +,OZOOO.~...... D ...   ..      ..  .~     ..   ?+?7$MMM8.   ~===MM=.........   ....       ... .....M
 .  ...  ...   ...            .. .... IM    . ......$MM . ..     . .  . ......  .MMMIMM7MMMMMMMMMMM8MM.. ~ .. . . .  .  .  .   .  ... .  . M
..  ... ....... O,NNNODNNNNDZ.,,,ZN.N=.... .......  ,N8NO:..D. M,.~NMMMN....N7$.. ...NNN.MM8MMMMMMMDN,, .:..=D+.,M7 ..Z?$,,7MM+.: . ...  . M
.......  .............  .  .,?Z??$= I     ........ +++MMMI,++ ++,+++::ZM..+.. Z~.. ..   ..MDMMMMMMZO,.+M$$M N$++MZI: ~7I,.~I?I= ,:   ..... M
.......  ..... ..., Z+?7. ?M$$:~I$7..  .+.. ...  ...D,$.$ $ZM   .DI. 7M7   .  . .  ~ ?...Z::MMDMMMND  .OMO.. :+++:?8+M+Z=~ +$Z ++++++:     M
..   ....  ....  ~ ,,$:+D,,..8:ID+,.::,..   ..8...8DD.:88NNNN:,.   .... . .... ..   ,.  .=,I ,8MMMO8O~=MD78 O IM,:,,=.:.ODN   .......   D  M
 .  .  ....DMM+:~:N8.  ..  . ..8..N8? .  :+ ..     ,. ..............I. ,.   . .. ... ,..~MN 88D8, .DDMO8 . ,::.~I::   . .     .          :.M
.O. ..=.=... OOOOOOOZZOOOOMM88MMMM8?OI+=$... .....MM8MMMM+Z7MM8+========M=7=M=$==O=8==N=NMM==~==DM=M?M~  . . =.+ =8.   ..  ....  : ....... M
.. ...~::7ND?+?+7.~..       ..?7777I=7I7M...I??+IIII~,.=IIIIIM77.= D$. .=I~III.I.O~O~.N.M,=.$MI+NMDN+,,II::+ .~IMZ:.= I~.:?.:I.   .,.  ..  M
.......... ..... ..~.. + .    ,,,, .......,.,I ,Z:,Z==~$8.:$MN=NM..   . ?8?I M...7.+ ?D,=.I:ZM:.  .Z.. ..     Z:ZI, ,  .? =:8==.,.., ..... M
..  .   .  .....      .  .  ...   .+. .  . ... : :+.7,,N,,~               .D.              .~.                =. N==?D:.. .            ..  M
..  ...  ......      .         :?=$~~=.~+.. ................       ... .+I: ,       .   .     . .                    ......................M
........ ...... .. .......   ...............................   ..=?IIII7$,~=  .     . ...   . . . . .. .. .     . ..                  .  . M
........ .........   ..  .   ...................................... . ..   .. .  ........... ..    ... .. .  ..............   ....   ..... M
.    ... .......              ..............................                                                                              .M
 .       ..    .             ...............................                                                           .........  ........ M
............... .......................................................................................................................... M
.......................................................................................................................................... M
.......................................................................................................................................... M
.......................................................................................................................................... M
.......................................................................................................................................... M
............... ...... .. ....   ......... .......   ......................................................................................M
                                                                                                                             

""")

page71_art = ("""
. ..... . .   . ...,...ZOM~~=: ...  ...O8NDMMMM===~=I D~==~~=~~~~~~~~~~~~~~====MO88..~===~=~MM88OO..... ..+M. .. ..~=O$.. . ...............M
. ZZ$$MM??,   ..$$$$MM7?+... .......     ...........:D ...........................  .Z=..... ....:??MMO$Z7 .  .I??NM$$$. .  +?ZI...........M
 ?D77$?.OI..  .    ...   ......................... =~I I............................8M~ ?..............  ..  ... .77$MIII..I7OI.. .........M
. .  :.. .........................................?.M. $............................~D=.?........................... ..    ?OZN=.. ........M
.    8D.........  ................................7 $.,. ...........................Z?= I.................................?8~    +O........M
. ~ +M.8 ...................................... . ==8.Z .............................:M.I................................ .8D 7............M
..I O , ............................ .. . .  =?7$. I.   ..................=..     . ..O Z .. . .......................... .=D M............M
.:.DZ  .................. .. :~: .=? ...... ... ~=+ ONNNNZNNNM?+++++++++++D+8==++==.  $,.......,.$++=,  .. .. .............~8.N............M
 :~D   ..   .... .Z,,:. .  .,~~DDZZMMMMMMD88888==:,......... ., .   ...   . .,,ZD888ZNDNM++O88ZZDDZ:~~... ,:O=Z~,...   ....~+,: ...........M
O.+ ......   ,:8OZ.?++=8ODD=~~,...  ......................  :::?8:           ............  ....~~~=ZDOZ88~++~88I:, . ,~~OZ..+I ............M
,O NZON++M88N+==. ... . ..  .. +ZNNMNMNMNZO,,,........ .ZD= ..N..,  ..   8.,. ....==7=N$$$$,,,,,.... ,,  . ... ==+M$N?ID$Z?,.?~=?,.........M
ZM?+  .. ..,$$$7..........$MM?=+ ,. . N.  $. .. .M+Z:Z   7?.....$,......:.~? .......+8... .I$$7   .:8+. .=.......... .   .:+M$M7M$? +$.....M
  ~=8O8:7   +O~:O:~.. :O8..:8..7.=...:O...N.:....N... ..::  .~:  8I::::~ 7 ~ ,.......Z...... .O.....7.. :,=7:.............. .. .~,8O+N+. ..M
      =.... . +.7..,.....,..,.O, ,+ Z  ...,8 .. ,..?Z..+Z ,$88N=.,:M:O.~..Z7N~~MNMMN8MNMMZZ88888,,,,O7.. Z.,. =N+.............,,ZO, . .=~Z,M
.. .. .M=,.8..+ =. . =... . ...DM=8NDMNZZ8+D.. ~?.?$..OMO$..D:?.?I:O$8   ~~I~ .=DZDO.$D.,Z OZI M$$?O=.7= ,. ... . =NO,,..,7,? M..O$+. =Z~  M
  ..:$$MM??MMMN: 7+.7~ ..DMI~:,$D,.DD8N MM ,IDIM$MM8D$.8$M .8~I..I=.D$   +$D ? =?,$$.Z. +M.N+$.OI=~Z: $MZ?  ,.$~Z.:.:8 .7.~ .~M=. .....Z~.?M
7$DM MN=? .NMD:8 OMMI?NI..::~~.N7,. I8O $?.,$D.:NMI=8D   I  M:, +I8 D8.. .$7.. I7I?I Z..$$ +I?.M$:+.: ?N+N.MM~.$ ...I...MO .,. ,.N ... ..IDM
.,IN O.?I .ZM==8 ?I 87  .,,,~: ?7: .II: 7$ ..? ,=M:,87  .D?:N,:..$DON= .. I7.. NO,8.,$..D$.= ..M7?$ ~..N=:.ZI$..M== O...I~ ..?=O.Z ....M=..M
.:NM +.,? .MM::D  . 7+ .,,:..  7Z, .  ~ 7,.... ,=M,.$$  .O+:~+,.. I:NZ ..$?~ . M~.+.,M..78.:~  N?Z$.:. ,:,. M7. +: =MMDMMDND~? I+M 7Z?8MM..M
..N  .M:I .D:,.D... M: .,..8~ .7$N ...:.$+....:I=M?.OI  .8N.~+=.... D$..   ,.. M+:.: ?..N8.ZN. M:,,,O..D:,..NI. $:.=.=,,7+,~+I =?M $:I,,...M
. 7 ..NI . 8:.,Z....+Z.....: .,I?,....~.M8 ..I,+~D ,=I  .O8::+,.... D$ ....  . :$~.=.+..N,~7N..DI8 IO..~,~. =?..I,:,.$: 7+.,:: ~+M M=7.....M
...  ..M...O :+ ... D7 ...M  +:?$, ...: IZ .D?~=. .I+:. ..::   .. . .= .., ....M=,.O +O.D,$. ..D ..ZO.8.~M......$ ~. 8..?+  :..=+8.I+$~....M
.   ..,M...O,Z:.....$7. ,.Z...~?,, .. .. . MD,~7.N?,=:+ .O, . D.. .:Z, .= ,... 8,:.O.?O.+ $ ...D...+8 Z:.: .  ..7  ~ D..?=....D=? .IO7$....M
.     N$., MD,::....7D. .,$ .,+,.N .   . ..DODM..N:7= =..:=,..= ...+OZ  ..Z... N,.:D.IZ,..M....O...+:  ~...... ,7 ~ .+.,D+ .$.N$I . O?~....M
..  .  ? , NZ :D  ..$7  ,O?..DI.,D...~O : .~7?M..N I8.= .:,:..+....=+N.. 8?... :..=.  8+D.M .......I~..Z... =: $D O  =.$.+ .:,N7=  7~?.....M
..  , .?.. N  :+....7+ ..:$ .MI $D  .?D.I..=8?M..N+ ....., :..DM. .,,M..,=~.....   ? . 8D.M. ,..  ~?~..?I .?:=.~Z.8. .+=++ ...M7=  O:: ....M
.   .$ ?...$  :.  ..=+ ..7$..I ~IN   +I ~..87?...M?. ... , :. IM  .::8..., ... 7?..I...IO Z .+ . Z.Z:..?8. O78 .7 , . OI7+....M88 ~7$.I....M
.   .$,7 ,...~7 ....=+~.,M$  ~.+$D  .?I,  .DZ$ ..N~: ....~7N  $7... I~... ?...+.8+I  . $:.M..,~ .I.7Z..$ .. O ..? ,   ?NO?..I.,?? ?$?.,....M
.....O,: ,$ N~D.  . +?M .$~: ,: =.   .+I....O?...N+,.... ~.M  +$...7N ....?..I .=: .,  IZ ?..I~ .I ,~. I .   ...  , ..IN7+ .:. :? ?+Z:~....M
.   .7:=,,Z MI~  .D ~ 8  $ M..?.~.  +8I$....7I...N+.=... $?N I7...=8D....?,.. ......?=.8O.?.I=~ .= 7~...+?.?..... ,.: .7=+..,I,?+.?7. 7....M
.   ?ZI7 M$ ,+:  .$..7N.8. +.  . .. .?8 ....:I ..M:,I..= .7: ?: . 7ZI8I.. ? +.......$Z.87.+. ?O..I.+,.. .8....... , . .I:+..,..Z. ?8 $Z....M
.    .:..MO .:, .7$.+?Z.8  .:..O ..  ,,.7,.M+$ .. , +$,... D.?+. 8,  . . ?7. := : $O:..$I N.,:: ...?. .. Z I ....      :Z+.. .,O.  ?.8$....M
......Z..D?. ~:8..$..+~.8:...?,+....:Z..?,. $M ...,?=Z,, ... MD,... :, .. Z. ,=MOD~:,  II,Z..?:    +.....8 ............87=... N...,? +.....M
.  .   ..  ..~Z. +...+ .8O.. IO,....ZZ. 7N, :?...:.7MI , .....8 . ... ..  $..Z.D. MM= OMI.M M?$  ,I  ..  O.I ........  ZM. .......M .7 .  .M
..,,.... ..  ~+.  I. . .,,..:,Z, ...MZ.,.+N=MN .. ,,O? ?~ ..... .... ....+.  $ZNM8.NMNMM?N.=.,,  =.M,+   : .......... .,M..... ...$. ?...,.M
. ~.   ...Z. :+.I..$ ..,   ,:I?. ...DZ :........   ,,? ?M~::,..N...., ...$D   NM.Z....... .. 7DZ.D?+.? ~ ~.... . ... .:=M.......... O+.. ..M
.. . .... + . ~:....: .  , . ...,..I.$.  .OMZ. $  D?8? ?,.?:...7....  ...=M..=ON$Z8 .....  ..D=8$,M+.?.O==. .$,+  ..    :.......... D  Z7 .M
. IM   ..  ...  ...   ...,...   .+.. ... .,+, . .  OO?   OMI.+I +:.....~8O ..ODN7M  ...+. .. .  I.?I.. =,D  : 88=....... ...........  +$? .M
..~ ,  .I .  .Z....  .....:NM7 .................... ~?., MD:  ....?,:+. ~:. ~?MN.D  ....I .... :...NM ..?,..8 M$ ....+~ ..........+.... Z..M
.  .....   ..$.D..  .OMZ 8.:M$.............   ,M ....?...8M....7.~7$:Z,.... N88 =Z......  ...+..  . .$ =+Z..I ,=....~.,~N. .,.....~...: ...M
. =M   ....O    .. ..I8D ?.:M+$~8M......+?$.D~?O~. I.  .:D8 ... .O~INZ.M8 ~I~+8. : ..........+:   .~,?.:,:. ... .M8DD ,~8I8. +?O....,? ....M
. NM? ........ .  ... 7$N7.OZ~ :Z7 ...I$.M8?8+MO=. =I~   +.......O.ID$ N8.?OO$M7D.I. . =.7 ... ....+ ?+Z:,..... I?Z8N.:~OZZ ..II= ?7??.....M
..IN?=........~ +..  8:.. M:....$, .. NM~?  ,.,77 ..,~:??:... .OI =ZN$ :D .IM$N 8 ..Z. .$..  ...  .Z ZIIM8 .. DDD$DZ8+~OMZ$ . 7?+.ZO=M ....M
. O+IM8   .... , .,D  .?~  ,,....:  ..ZM:Z  ....Z. .8.=?~. ..  .. NI8=,D7. +MMM 8..........=  .  ... $8M8,   $?.?OONNO+..,  .IM8I.?7M?.....M
. 8MIO,$,N ....  :, 7D.,  D$+Z,,M .,.?I:.. .  ..:.?..  I..N...D. :N:  ~~: ~?.MD:M.. ..... ..N. :.. ,.I:M==Z ~7=...=.DM.~....:?~ .:87,.. . =M
. MNNM:7. ..:8..D8NN:,=.~. ,,..., . =IN,. :,.,..$  I,.+ =,  .7,$:8:D~:D8, .I.$= + ... NM8.Z,.  ...7 .I:::8N8M,,....+8 ..,. .,. .. . ...8. .M
. +.NOM7IO8M~.. . ... M8OO .. .,N...  :=.+$.....=. .  Z.  .8=ON  8M~. ......7$M ~ ...,....   .+8   . ..:~~.+.    . ~M8Z. ...~ . .. .. .. M.M
. =~MDO.. .....    7 .: . +..$O~I : $7~$ +M ~. ,= $.  .~D8 O..N.  ..7 ..   ..7,,~... .O  .   ..   .. $  :. I . .8::.... .,D8:......  .$~+D.M
. ..   .   ....D. .... ......,D.. , ..8$I ?.=.. ...,N..++8 ,O   $. .. ... .., N~ ... .  ...,.........?  .,.  ....  ......? ...~.... ..N,$~.M
.      . ..7....   ..$ ....... .  7..  ,.N78:. O M+,DI D+: O:  $7.. ......+ O NM= .. $.........:....$...... . ........,    . .N,..,+. DD~,.M
.   . . . ..O. D .  7O  ~ ...... .$ .N.M?..8Z,.,.O?.=$ .., M Z ?$?,.,=M.. Z?..ZD . ...... ... ..I . ......... ..... .........M8~=.DI $+~8..M
,,ZMMM$MMM$$ 7 MM,:. $8.........   .. . I, $ M.,.IZM?O... .N$+.? $~.  ...$ M  Z.. ?.+..... ..   :. ?D Z......? ~?M.... . . .:M?M.    ~.?$..M
       .  ~I.I D,?O~ ?........=.~ +? ..7. 7.$.M ?.7$D~+.=?, D..M.. : .     =+.   + 7 ........ Z .,M?N. ......=  ? 7:.. $.. .8.M??..  ~.....M
       . ..NMD:.Z,.   .,ZD...=..7  , .. ?.? 7 OO , ?NZ8:~.$...$$..:.8... ..  +,Z..N... .......:=Z7OM8.~..  .. O.MZ,O. .$=...ZI.. .7........M
       ,NMD:MO.. 7 ......,...:8=   ,.... ~.?$+,.,N. D$8.:..8...I..7$ ,~ $..I.8..M.D .. ..   =I..=D~ .I+. .....=.....  D.:... , ..... :.~ ..M
..  .MI =,  ..? ... I....... =78 7MO.  ~~ ..D $~7MMI.O  .... .. .. ..~.D. . .:..M.~ . ....M.. ..  . I. I?. 7..........   . .....  ...   .? M
7.  .  ..  , ...    . ........ I.?~O .... ..N M,~M Z  :..........+ .. ,.  $.I . DZ ..... :8...........,. ,.?I=.... ?.   ., ..... .~~ ......M
.+  .  .:.=..  ....... .....:,=8 N O~?.I...I..N+=Z?. ........ ...8 ....~.~ . .. .$  ....I=7 .............,.=,.....:Z ......$..=: .=  ......M
..$.   I .......  ..... .$,.D.M?.D.O.I ~IO~ 7.M88. N .,~ ...  N..M .,,.,.+7 ?....+Z.,D.MI.+.M......... ....,O.... .....  ... . .  ...,:.,:.M
...:  .$.8:. ... .....Z.,8? . D7.$$O:,:,78$N~~NO8O:., ........D..M ...D  8?  ....MM8$~NNI Z? ..............Z8............... 7  , . O..D=:.M
..  .$ 7.....=MMNMZ,..7~?.=.. ,7 .M=.+N.$. .+=?Z,M +N.........N..O. . .. .$D.... D..MMI$D,?O........ .... . N ...............?.... ...N:O8 M
.... ? ........$~M+ .$. =.~:87  D,., .  ... =?MN:N?7.~OZ.,., ...$ OM?.. I  7...MMZMM8MDMM$OD$. ..... $ . ..  ....+, .......I....   ..?D.O,.M
..... ?....:..+.=O~, ?I =.~+?~IOMIII$III7IMZMMM$~MZOM78MMMNI7777~.. ....  : +.      ....    .  7 ............... . ........?.....7,..?+M...M
.... ......... M ~??.?8. +?~~OM+?+M7MZZ..?+++?MMMMMM+MMMMMNOZ$ZZZNMZZZ 7.: ....$.ZZZZZZDZMMMMM..+ ........Z.  ..$...:  ........~ +7..I:....M
....:.. ......+.... 7+ +,+..,....MM,ZN?+:.    ....    . .......  MO $8MMM?++?+++++++7+7+?+O$. O  I........... ...Z.. . ..... .$,ZM$+  . I=?M
........  :.M+,.I.  ++I,. ..  .O$.O.Z..7MMI?IIII:.. .         7MII+MI8,.O.8$$~. .,N. .    .  ..7 .D........   ..~., .. ....   .Z+ ..+   ..IM
........... .+:....?+. ... .I~I $ MZI.NMMMMMMM?IZMMMM$$$$MMMI??.D:878 7O:~$?8?$. .,?MD$$$$$$$O :Z .+........ ...  I..=.....,.. =,??: .Z .. M
..OOO..I.  . .. .: :.ZD..++.~+87M:M8 Z 7IO   .MM=  =~OOOOO  O=O= N:7 7?~7DO=O.+Z,O=MM.D7=M +=78 D~  ,....  .......  $..  O, ~. +..=+.......M
..... .?.... . .. +.7,.8 : :.7.. NI.+MM$MDM+NDN8=N7NZ..   .,8M:.8: M8ZMN,M.I.7D8=O8M?:.DMMMMM~:..N..Z......... =D . ....D.  :D. ,  . ..M. .M
....., N... .  ..I +.,..~8.....NIDI.8,,::,,~,,~D~N.,DI::,NDD,::ND~MMMM+DZOD,.8:.,D$.8I~D.:,  ...7ND..$ ..... ..... M ?D8.+?O..,...   .. $ .M
.....: ? .. ... .~:.?.,,.M$N DM7.D O~:..~~~~~~~:N8,.8:8Z~.~OO7.,,=ZDOMMMMD:O8=,,,:?O,7..~NM=NI.  .,=..~ .. .I.....~,M$D8? O ....,..? ....  M
.....,..=..~.., 7,$  .. 7MZMM+M M.?=+MM=.=NMMMMO.N .=.==. ..ZZMMMMMMNMDMZNMZMMMZZ$ . ?.+= ~$.O .= $ ~..... .:...Z.+O .D,7, .... +M.+ . ... M
..... O I....O.D,.I..+::O=$:~N.7N ?ZDMOM...MNN,.. 7 ,?.:M~=:NMM8=DM=M:+?$$.$O=$$:. ,$D?,?~ $.I.Z $ ?~..8. .::  ?:D,Z88O:::::.  .. . :.=....M
..... .~.Z. :.M. ,.$ 7.,ON :~$,7.D..  NDI . :D .8  ,8N:8N8MM~+~8:.OMDM:D,MDN.  ~OZ.=,. 7..? M..Z$.I ~$,NM . .~ ?I.~O:~77.. O~.N,,~I.:.Z. .8M
 . .,ZZ?: 7 ,8.  =. D ., + .= ?7.  ..=O?M ~.? =. OI:OM.7N7D.~=.:D,Z8NMD7,.7O.Z~. ?. ?.O8+N.+  7:?, 8,.=..O ..+.??  I .+. .D.=+= O.$..+.$.. M
.. .?ZM7$ZD$N.+ ...$~= ..,M7.I8.M ZI7DIDOIM77+,DI OZ:Z7MMD 8. ,~ID88DM?I. ? IO~.?NI ?+D:M .,+M:878:.,+O  ?M..7   ... ...O?~$   =  7..?...,.M
... .  . . ..   ..M?.+.$7$IN 7:?.IM~ZO8+7IM,,O .I? I$.$MI:~:=D..OOO.NZ:OI. O. M N,   7,8O:+ M?~ IO$OO$8...MM$~. .... =...OZ.,  I   ..=. ...M
.........M ....7 ,=. M=NOD$ :M $...=:778+M:~~ +~.+.~7: M=::.D=.?7D.O,MO: .~ ~ .DM. Z. . D,Z? 7M: 7?I=: M.=O+=Z=... I+.. I .7  M.~O+= $..=..M
...............~,, ?7 $=DM..~.8 ... ~D888,ND,N.,8.,Z.MZM. ,?. Z?7.ZD MN:=. I....$.M..+.+: $. :O8==:+D+ DM. 7MM :.  ...$O,  ,+$..+,:. ?.....M
................+:.....~M8.NZ, . M$  .:.I$?,:. , NM?.7O$~O:::7., 87 ,MM8, .7=  :..M.N  .. ,.M=D~  MN=M: O:..OI ,. ... =.?,? 8N .....~......M
.............  D.Z. ..MM8 ?M.M..Z~=OD.=ZI. = ,...:IM~Z,MO:,.M.,$..I.~MM=M..I= N. . , $+. ..= 7D8M,.+,M8 .~ .=. $MM8. M ~.$ O:I      . .....M
..............+. .$8.  +Z.M,~...MD..:,MM..$..D . Z7I8??I.=  .=~ ,8 8N M8M~ .8N.O..~.:Z = . .$ ~:?..NDD~, 8$~8$M.....?.8:I.?:D.N.O .+ ..  ..M
.....? .....  O ,.7. +.,,,Z.Z.. 7M...?:7, .~Z . ,.7, I, =~.=. ..7.,8N MM ~+  NZ. = M~:? .M.+  =:ID  =M.N ~? ..M .. ~O ...MZ~D,,8..7....D  .M
...........=.   I..O ......D ...  ..~.D  =?.~ N.8  7 .$7O:M .?. ., M8Z~~M~O.. ZN  D. ?~?. M...  7. .8$N~N.=$..OMMMMMM .  +M.:?.... .. +....M
...........,. O .. . ..... Z~NNNNNNND+=. Z?8,...MD.IZ N.8Z .., D M..O?,,$.M?   N8..N .+7,  MO.8+.ZM.DMM,O. ID,. NNMNN. M7.MD.$.. D...+.....M
.....,... ,+    ...........: .~  ~~8 7:..Z?O....N.?$$.. M:  ~  .I.7 M.:NI~ +..  ZZ  D. I M  OM .7.?.=MMMMZ=$ +M ??NZD+8M=M.~O,,..M .:......M
:.........$O.. ................$MMMM  .8.7 .~...ZNO7 ?~M=Z..= N M ?.M 8~ 8Z7.  ..:.  $ ?.,O .I+. II+DM~. N: MN~$=MZMM$+MMN7M .M. M. ~......M
. ?  ..~ N:   ...............8:.=7.O ..M.,$D~~M.N?7.D8,Z :..M ?.. ..D.I.D,: ?=.  O~..D: ?  Z.:~M =?Z,$MD$M M,$$7OZMMMMMNM$???O?. .  ~..  ..M
...., N.8..+  .+......... ..?..+ 7Z8     ?~.7O..I7~==$$ =,..Z+ ? + +8?,.~ ZM  I.I .I+.M M....7I.?  O,$ ,::.IN7:M8$$7$. ....  . 8. . ~7.....M
,....+N.........:.........   I ...?,=  =D.$.:8MM N= =M=$O :.ZM.M O.88Z = 7? . .M ~8.D .77M..Z ,=?,$M8$O.,,?M+O$M .$ .. . +N    O=M.:7 .....M
..... I  ............. O .=.: ++.N=ZM..  8.::=?:Z?.7NO+~. :.ZZ $.? 8+=.D ~? DI N$O8 O  M  ? .. I Z=MO$$..~~Z?$DD.N ,MI++   .... =.M:.I  ...M
...... ....................I..  : :+N8..=.O.?.I 8.8 M . ~: :ZZ.7.O.88.,...= .$..,:M +Z $~,?  O.M M?+,M . D8M?IO.O ~: .. .....  . .Z~. .  ..M
.......=..................?  ... .D,,~D  ~ .I.+O,,.M~7Z.=:.MMM.M.. 8O M...M+ ?. M?8.=M 7MM?=.~:D.ZM+,? Z, =ZMZ=Z.D, . ? .  M:......M  .....M
........7............., = ~......  ?,.=8$ .I..O:N,M 8.=?=D.DNM,I...8N.:,..+..?..$ZDMIM 7DM?N .D8IZO.8   ,+ $8+M$: ...78=$7$MN.......:,.....M
........ .....O .......7,. ,:. +...= ?.=??. :? 8:,M7,7Z D8.,+?D? ..,D.DM..+. M.. MODZM 7IM=+. ZDIZZ.~ ... ,.=~ $M. .NOMD,DNMIM:O.....M.....M
.....::D7   ..........: ..7 .?..N~. MMNN ,.N...+= .$+?+7M:..++N  ...8 ,~. .  M...M..+Z.,IN.Z .:DIO ?.  .......NNI.MZ8 N8I77M,NN Z....$ ....M
..........O  .......=7.I ....  N...M8O: .Z$.M   .Z.,.=N$.D, .O,.M.. :.,.$ .I M ..Z.MZM .. I+. :MIN.,.:.... ...=.=NI?OI,8I=?OIMN~.....$ ....M
............Z .... =.=+ + .. ? = ,8ZZ+ .I ?.D$+Z$.M . =I8DM.8ON$$.. $ ,.?..I M.. 8:.=MN 7NZ ..OD7NM .......II.~.  DIM +,D: 8+7MM  ...M.....M
.............Z...D,+. :+ ~. . 8 ,8OM,$~+M,.~,.~:$N$?N., .:: ~NM? .  N. ,.8 I M , DD,NM~ ?MO,. DD7MN......  .OI.   8O,.D.I+.M~7MDZ ...+.....M
...........:..7,? ? + ~,.N:,~$.:N:,M+:?DMM .:: .~MD..O.8~,.Z.+:,.M. 8 .,.~ I M :.8D ZM D ,+D.$:8I=?....,.,  .7. . OO 7 .:?$88NM8O .  ?.....M
..............  .. =. NI.. :.:  +Z$MM.,7DNM . +.,.? =.+M.~ M MN..O .8.., ~.I O.N.8  .$.. M?=..D:Z. ......  + M....~~7$ 7+$7.$,.+  ..~ .....M
...........,. .~8= ? ~  O  8 ....MO  7.,8? O$.I?.M.7=.+7:  :.MD7I.~.DI O...I:I=, Z  : =.IDZ ..N:Z~.~.....$. :?:..... Z$?7?=8M+I.... M......M
................ ..7 .D.Z?8... .8.?.... +O:N,8 ,? ?.+.+7=,~.Z8N Z.Z.D$.O..$ MZ7, 8...I=  .M I.8MI ....=.  .M 7 ? ... $N+Z$?D~7  ... 8......M
................?=. + .,O?Z .$   ........,..:D.+ O 7~ =~OD,.MNZ M.O D..O..?.Z.$, :..I8MO.$.OM:8M  ... ..~Z?~. ,.:......O. .........~  .....M
.....................Z8DD: .:........... = .:..~D.$? ?=.87..MID.M 7 8  O ~NDM.Z,~  .DM7..=Z..ZZ    ~~N=. ..7... 7.. ...............7 ......M
................ ..  ?:+:O~............  I ..$~.$=,, ?=$,. DN N,D.7 8 ,D.DN.M=M:8..MND.$.=+,DODMI.....$+ .. :,.7,~Z................M ......M
................. .7$,ZD8 ...........  O .?. I+ .N$$8M+$..N:O$NMM=7 8.., M: 8.MM.=O=OZ $,:M. ?.:  .... .....~ ,$.$ .D:. ...........7.......M
.....................7O7~.......... .$....=O==.,=..D DNZN~M ?~N$M=7.N ..?8: Z7$M?+: 7 M?N 7:. ,O. .....I .  ,Z.,+...~.~O, :.........~   ...M
......................D:...........$. .,8  ~.,DOD~M Z?Z O8. Z+,,$=M M.,.$:,7.M8=N~.D +8D.~7+..$D..........Z: ,= . .... ..$,........ ,O+8?..M
..................... =  ........... 8?=8D??88MIZ~~=.?Z=~~M,$N,?$DI..M8~ 88N~Z+M~ ~ O.O:  : D,~..:,,ZO+: ?.,  ... ... ....,~  ....?~ .$.,M M
.....................I.......... ,DI=,: ., D=.. ...:~7 78.D.,~NO$M,D M,~. 8I:~.MNN$+.M  ...  +MO$$.:ZM :?Z$. ..............M....O~ .$.N+$ .M
....................8 ...... $$I$+: .    . .......... ZI$:??D:, .M$$$M+.M~?M$$DZ~.$$OM?$MM$MIZMM7Z~:,$.:,,.8I...............~.7, .7+N+, ...M
...................  =ID7.I7  . .. .....................N .7.+I =O. ,ON,~ =..       .   7:  ..I7? 7DZ$N. ...~8..............IZ  ?I+I.. ....M
............  ..MO   ~8, ................................. OZ .?. +O$..N. ..........................OD+..Z8M=+=.  .  ...... : .II+ ........M
......... ..:M+DD............................................. ...........................................   8DDMM8:,D=....O.Z,+, .........M
........  =Z7:........................................................................................................II~. ,N I ...........M
........M = ........................................................................................................... ?$.M:=.............M
..... .I,, ............................................................................................................... ?:..............M
......, ?...................................................................................................................O$N............M
....+,  ?....................................................................................................................:: ,D.........M
...: ......................................................................................................................... $ .? .......M
..Z. ..O ...................................................................................................................... N .........M
.I... .+........... ............................................................................................................ ,.. ......M
?.... D............+ ............  .................. ............................................................................ Z ......M
.... . .......... +................................................................................................................ =......M
.....=...........:.........................................................................................................................M
...IO........... N ........................................................................................................................M
. O............. =Z+OOOOM?=. ................................................................................... ..           ... .........M
.  ........N... ?  ....  .DN~,.DN .....................................................................   ~NDD~:NMMDDDDD88888+DDDM7 .......M
...........=...8. ...........  ..8M. M~ ........................................................ ,IN~,8N     . .    ............ .. .......M
......... ....D ..................  ..DZ =M ...............................................OM   MO    .  ..................................M
......... .  8............................,N,,D   ............................... ..  N?DM, ...............................................M
......... .+.: ................. ... ..... .  N:,M ...  ..........................:,N...........  .....   ...... ..........................M



""")

page72_art = ("""


. .....  .  . ..  ....  . .                      .                .        .                           .                
 . .................................  ..  . .    .  ... . ..               .           .    .          .        ..    ..
....... ..  .  .  ....    .                      .       .                                             .                
.. .... ..  . ..  ....  . ..... .   . .     ..   .  ..  .     . ...  .    ..   .                       ..    .          
....... ................. .   ..             .     .:             .                                    .                
 . .  . ..  . .... ...... .   .,             .   . .       ..        .     .                           .    ..          
.. ...... ... ..   ...... .                 .    .   ,  .            .     .                           .                
....... ..... ........  ..  .......... .   .  .. ..           .                                 .                       
   .... ..  ..........  . .                      .                   .     .                           .     .          
............. ..  ....   .               .       . ...            .  .   ,..           .        .      .     .          
........ ....  .   . .                           . .    .     .   .  .     .       .                   .     .          
.. ......   .  .   ...          ..=,               .    .                       .~.                                     
....... ..  .  .  .. .  .         ...         .. .      .        .        =.                           .                
  ..... ..  . ..   . .  ..    .   ..        .    . ...     .  ,            .                           .                
..........   ............ ..          .     , :... O    .      =. .   :. .                                              
 . ...... ....     . .    .            ....   ,$ :D..M. . 7       . ,    . .    ..,.                                    
.   .....   ....  ....  ...                      . =..:, .  I     .I .I..  .  .                                         
..........  . ..  ....  . .   .                  .  O, ...7 .Z .  I..  8,.  ..,.                                        
. ...... .  . ........... ...:=+.            ,~, +ZO,: .=    . I..... +.=   . . . ...                  .     .          
   ..... ..................     .8..   ... +=~,. .?OOON8~      .   IMDNMM7IO=======~ . .  OZOO==     :.    .   .        
....... .     ..  ....  . .      ~:. .. ..:      ...?::    O... .I~ZO=: .  .   .            :.         .     .          
....,:8N8 .  .=DD,........ .. :: . .     .   . , .. . 7++   $..,. .  .   ,.     .,DDI:..DN              .               
M: ..   ..    .  ,  ..N: .M, .MMM = D                O.=...    . .M  .  ...  :MM+. .                   .                
.. ...7 ..  . ......Z .=.  .   ..... O..ZZ?OO. . .+..~.=      Z:. . ,  $. O:..+              . .$== .. ....  .          
......  ..  ...   :?ND8.,,:,ID,~,.DN.,NN.    ..   . I.,.D   . .,. O$ .,.    .,,.  .. .. 7I 88N=. ..,DN..:.,:M,. .. ..   
$ ..........:D~. .  7:..  .       =. .+N .       . .I ?,= M=7  . .   I         ... O . ,,   8D.,.. :.NO... .  I= .  .:MM
..,.  7Z,.? .. .   . .        OZ. =OZ8..=..ZZ.   ..,.I.$ +?.,., . . . .7.   ..,.~         .       O=~     $O+. .      . 
  .~ +....  . ..  ....., ::   ..,    ..     ,~    ,.   ~,.I.  O?. :      , Z .    ..      $        ...~O7    .~Z:       
....... .....  ?   ..~:,      .   ..    O .        ..   + =. , :?.. .+    ..         +    $            .  ..            
..........,.  ..~..  . ....    .    D7  . ,.     . ...    ..=.==.,.~. .       , . ...     I.  ..      +O. ..~~~ .,88D~~ 
.....  .  .=. ..   . .  .,~.    ~.  ...,.I.      .  ,  ,      ,.  .:,.$O=  ...=8 .        I.    .M,.=O.. .   . ..:$,.   
....... .    ...   . .   :Z ... ...,, = =.       $      .     . .. ..M..  .    .+...7   ..  ,.  ,+  .. .           . :  
.  ....  .  . ..  ....  . O~?.+N, . .Z.         +.?   ...          .    .  ....=.+,    M.?...    .    :      .       .  
 ..:.    .  .  .  ..    O +. +: M    .~. , .    .: = ,.    .I..     .:.= 8+.  .OD ..  ..  .     .      .                
. . . ..8 .   ..  ,7.8.:,.:,D$, .... 7.?..  . ...,..... .   ., .,.    :.~MMDM~MN7D $.. Z ,= ...,       .                
   .... .    .7$+?... ...  77..     ,I. 7=                     .. , 7Z?:MM+MMIMDM?O.7  ~.8:.. .+ :.    .                
..  ... .   .  .  ..,$.. D    ..OZ   ,I~+.=.     . .,.            ,  . ,DM=I$~D=8M8~$..=...$ . .~      .     .          
....... ..  . . ...,:... ...   = :Z. :,  :       .  ..            .    DD$?$,NZM$MO.:. O..$. O               .          
.......  .  .  ,$. . .    ~     . ..   ,=M~.  .........  .   ..:  .   +  MMM?MMM7+  . 7,..,.    ~.    .. .              
   .... . .....:OO, .,$..8.:...8.      .  . .   +7NMM?MM::     +   ZMM, :, :8..,D.~:D8. .,,. ,  . .7.   .    .          
   .... .?  ......... ?Z  $ ..   ~?  .=,.  . $==MZMM$8MM8.  ~::+. .8MM8M.7MMM8MMMDM~$M8M  ....~Z, .?..  .               
............. .......   $ . I.   ,.7N,.7 M..$.DMMMMNMMMMNM ..Z. . +,MMMMOMM?,,7+M~OMMNNNM.    M. .+I                    
..............     ..=. ?? ::: N,.~ D. 7.77.7 ZMMMMMMM?+IM .?8  ~MMMM~$.OD7MM$OM:ZZZO$M8MMM ..... . .. .   .+ .         
. ..... ..  . ........O.I. . I.,8. , ,..O? I?8:MMZM8MMZMNM :$D~+:ZM8MOM,?$8:MNONND=DM~MNMMMM. ON=~:, . . . .78    .     
. ..... ..  ........+.:... ,  ,8OO.?....?$=. Z=+MMMMMMN?$ .O,~O?MMDMMOMD8N:DM:7$,INIMM=MMM7M8==:~N8.O.   :   .          
.  .... ..  . ..  ...  +.,,    .I ..  , ...7D,..8OMMMMMMM .O.:M$ZDIOMMM:N?$$M 7+DD$7M MMM8DMM.,::$8~ . .    .           
.. .... ..  . . .....$= ,:,       .I:..,. . I..8NMMMMMMNDM~::~NDN?D7DMDNI7MN8,77:MN8MMMMMNMMD,,?.  ..  . :              
.. .... ...87......~+8 =  =,..       O. O, .N,D?MO NI87.. ,7N=:NO7DMMMM:77M+=O$87M7M$MM8MM8M~ 7=+ .  ,$.     .      .   
....... .8  :Z..  ,87 :, D. ....~.....~ . .?,D:DM=MM$MM+~.$I$?MIMMIMM8D:Z,MMD8.D:O?MMM8MMMMM, $$, ~ .=. ,               
.. .... , ,8.  ,. $,N , .~ ..?., . 7. =  ,M7O:.8N .,NM$.  ,:Z.N. I,=.:?MNMN$N,N.N8NOMM~ ,. .Z=.7O   ,.  .$= .=,D,...    
.......  7..,$ ..O 8.  .M...M..O.  ?~..$.: 7~,.MMMINNM$ZOD7,~DM?= $+ $M =:ZZMM7ON888DMM. I.,. . ., D     ....   .Z?     
 .  ... .   ?. ..M  . D 7  ~I..D   I,... ? .MMD8MM..?MM..,7M,M $.7.+ MMN.7MMMM?Z +8M.MM 7.,8Z=    +7.?8  8~:   ... .  . 
... .+$=..I7..?.  ~. ~I8 . ,  .:O .~,::.8O ~MMMMMO++MN$=I=Z7INN:=. =:?MMNIN$NMI8$MMMDMM 8$ .= +.. ~ 7.,~ ..II~.Z8I  ,,. 
..  $O,7.,  . 7 , .  $=:...D  ::Z ., :.I:.:7NN$~+$IO$ZIZZDDN :~,?. ,MMMDM77?M8MNOMZM7M887O. ~ .?O.,ND,..IO. . DMD,,O~.,Z
...?~~7?. .. $.O ...I I?  I$  =.8,. ..ZI $..~87?..    :,,, ,~I?$=.+:MMMZ$8OM7IODMMMMMMMMO~ 7 . ~?  O.~ =~.,?   $~ I?..==
 ,=Z~+,+.?7::,,? .. ==.. =~$  ~:N..~,ZI =..I: =DIO88IO8=+OIN=7$ ..=,MMMOMO$N?MMZ+DMI8MMM7I +~....?Z .,Z:.:   I:..~~+.$Z 
. ...    .I.Z:8,..,I,O..,:,..,7.:~:,I?,,  ,$+ .+... .  . .  ~O,,,..:8$MMN:M+M8ODDD8DDMMM7,.~:.:.78?. . .I,ZZ..,, . .    
:.~ ~?8  ~.~,.O Z  . $~.I.$:..8+~$8Z.  ?~I    +O8IMO?=,.$,7~=.   . ..+M?MM$ZM~~IM8~MMMM$?..    +8?. :..~ :N+I,.87.Z=..  
   .I,.. 7 ,:.$.O DZ :... .     . ... +? +8NI :N .... .  . .?.OI.IO 8,+MMIMZ:NNDMMMO7MMMNI.~. . . .?  . IO8=  I:.+:.=NN 
   ....    . : ~$  ..  . . .+:.:=I~~,ODI~+.+: M~, ?O.7+O8$+M~ ZI.== $7ODMMMMM?MMMMMMMMN7Z==+ = 8..?~ ==. .    ~ ? : I.  
   .......  ..  .. Z...ZMNO .7,.,MMNMMNMMM,I..M+.   .  .  MM.. .   .:, DMMMIDMMNMMMMMMM . . .  .. M7NMM$I,:DZ?.  .      
............I~+II. ~7.,,=$+:O7.. . .,I7I...  .$~77O7?=7D7..Z: I ...,78:MMMM8M$MMMNZM7IM?I~,.?.,D..Z~?777I . ....I7II,   
... +.=?.I~~8..=$=,=ZO.,.. . . $:. .  . .    .Z  .    .    8,.  ? .....NMZMMMMMMMMMNNMMZ+~.$ .=~.,$78~..D..Z . ,        
......,.:I.=$D,Z:  .    .   .,:~.  , .,O8D~7,:~  .  ..     O+ .,.,N78~=MMMNMMMMMMM=87M~.      .,  .,  .,  Z=:?I.,Z$Z,~, 
....... ... . .... ~   ...=$+. .?7 I$I,:M. 7,::   8.,+?8$. ~N,$$~.:?? ZMMMMMM+8MMMMM8M: + I.$7 =.     +=.$:,.=~ .?7     
. ..... ...:. ..$Z,...... .  7,:O?~+:D,.~..7.+.  . .?:I   ....,,I... .:Z$ON+:MMMMNMI=M::~,Z.~. DZ=.    ..   .   . .     
.. ............ =  = .  . . .~.:,I7.,?  ,. I,M   . .D?D~.   $7 ?7..I ~:8MMM++MMMMMOMMM8+.I~.+,.              .      .   
.. ....  .  . ...  .   M. =87  . .. .:M8N  N?~   .  DMZ:.   8D I+ ..M,,=8M MM8MMDM=MMMZ=...          . .            .   
....... .............. ..  . ..   , .= .,.8M.~     .$8$     .O..$.. D7, MMMNM~MMMM+MMM........,. , ... .?N          .   
 .........  ............. . ..  ..         . .   . M.. ~..   MO8 ... ~~+8M M+,NMMD8DNM=$?7 .:I~.ZN,=    . ,:. .         
.. .... ..  . ...........             ..  .  .     N   N     M,$.... .  MMMMM $MMMMMMMM.I., 8+.? ...   . .              
....... ..  .  .......  ...   ...      .  . ?.   ..N7DON     ~I..  =I.,$D$M$MM8M$ZMI8MNI =..7 ...  .  ... .....   ... ..
........      .......... ........... .IO87. D..... N...= ....Z +..Z?.=ZONMM+D+ZMM7NM+MM.................................
.......     . ........   . .....  .. .......$.... .$...N ....D .........N::M7MMM8MMMMMZ.................................
........      ................ .................... ...?................=ZZDZZMZMD~77+,.................................
.......       .......... . ....           . . ..  . ..  ........... ....   .+MD888=,8. ......... .. ..... ..............
........    . ......................... ....................................,.... 88....................................
........      ....................  . .   . . ..   ... ..................................... ...........................
........      ......................... ................................................................................
.......       ..............  ... ...  .      ..        .......... ...... ..    .... . .....    ... .. .. ..............
...... .      ..  . ....                                 .....       ...   .     ...             .     .    .   ........

""")


page77_art = ("""

 .  ........................        .. .  .   ..  . ... .    . .  . .   . ..   . .     .  .  ...    .... .   .. .. ...  
 .  ..   ....  .......... ......  .........  .... ..... ......................................... ..  ....... ..  ......
..  ...  .... ..........................................................................................................
..  ...   ...  ........... ................ .... ......   NOZOOZZN=.....................................................
..................... ............................... $:....... . ..,Z: .......................... .....................
................................................... D~..7? .....  .Z. .=+...............................................
...............................     .. ..  $I777777..~=?............ I 7.N..............................................
..........................  ..$MM?O?D,8? 7 :8NZ7 ~..~.=................I D.7............................................
.......................,~NI~Z.+,+:?.7:7$.+Z~~~DO8.~,.: .................+ .IM8D8NN8N:,  ................................
.................. :NM.,Z8..Z+~$=~I:8 ?:~I,,?=MO~.Z.N=, ..................:.:N:N:: D=~,78M$~  ..........................
 ................$+.:+Z=+O:.?7.+7D,D~:7 Z~,OI$MI ZZ +N?+$. . ............. .ID8.,,~+D==::O=7 MDZ. ......................
............... DM$: ,$$M=:ZIZ+=8,8==Z=7$?I?O,$+$M8=,$N+~,$OZ............. :NO=MZM? Z?:Z:I?.+==Z,+O? ...................
...............7.....$7MMMMNIIDM7MMMON$I$~8, +?DI8I . 8ZMI??...7$7$$$$$..=IMZ$8ZI .$MD8I=$+O$.Z= N:+7,N=................
...... ...... .IOOO~+...Z:...====MMM=.... =O,M=..+ .OI:~.  MO  M ..IM+= .O$..=:MO~==M8=MO=O=+Z=.Z+IZ=.OD+7.......... ...
............ I $======~~=======++NMM...,D=N~.. O, .=7+~ ,,N.NZZMOZ88,N8NND:?Z?,N~+MO~?7.,=+MMMDON+NN+==,,,M. ....... .  
.......... M.. M7.... . ...,$$$?IM? MM+M.. ....7N ?7Z. . .:M...M .?INI+   = IO..$,I7IM? ..MMI8M$77$$$$ 7$$$D ...........
.......... ~ 7 ID.D~:  .,  :DZD:.~8D:7DM~... ....ZN,..:=.ID+,:.~     :Z..D..~D$.D~....DMD:Z+?$DOZDOZO8DDD8O8..Z,........
..............~.$M:I,M~ .,~DI,~~ZZ~8?=8D?78DMDZ=M,......:ZO..: ?..OZ.~O$ :.. $$8..... =IDM8$88M:8$ZN~~::,,?Z , $........
...............  D88,,,+M,$N= $+. ZN?.I+=$I.D7Z,.ZOM8ZZ 78  ...D......M$..  ...MMZMM7Z?+$:$?I$=?Z  ?MZ, .8Z.~. .........
................ MON7DM$ ..,NOM~Z~.Z ?=$I,8:,?7,.~Z~+~I88M?$7+7MD8NM?78+I~I.:$=.$87.IN.??+~O ?$.?NZ,??NMMZZ. ~ .........
................ :?M$.+. :$I. .. $MMIO:.?.$I:.$I.=I,.,.  ~?OZ8DN?,,.. ?OII, ,77.:$:.7~+8 8.D=+7. $$D77 ?MM. ............
.........................=78..=MO.  ...==OMOOM8,~D,~+7O?Z$=I7.M87,NIDN$ .=OZ~.+=.Z=.$+.N,I O.8OM~.Z?OMMDZM..............
....  ......................   ..   ,=NZ88:.. .. . ~DDNNZ88DD~MMOD?7~:+DZ:?DM,+O:8N8ZN8D~=  ..:8D=:.~~DNN ..............
................................. .,I$$..  .  ???I777+  .  .        .......     .     ,77O?I.  ..7......................
........................................  .  I.7M7I   ...   .7I?I.N..      ..... ... ....:?=I   ........................
....  ..........................................  ...  .....~=8DMN...... .. ==:Z$I,, ..... .............................
....  ............................  .................... .....M?? ......................................................
......................................................... ....DNM ......................................................
..............................................................7?I ......................................................
........................................................................................................................
....................................................  ......................  ..........................................
 ............................. .........................................................................................
........................................................................................................................
......................................... .  ....=============.. . . ...................................................
....................................  :MOZ.. ..................  . ..~ZM===.............................................
.............................. ... ~+   .............................. .  . .?8$:...................... ................
................................. ?............................................... =Z. .................................
...................................................................................... +  ..............................
..................................8 ................................................... =...............................
....................................7D.  .............................................. , ..............................
...................................... +M?, . ..........................................O ..............................
..........................................  .I7MM7................................. ID..................................
................................................ .. .=ZOOMMM========~. ====+MDOZ ..  ...................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
............... ........ ...............................................................................................
""")

page86_art = ("""

.......................................................................................................................M
.......................................................................................................................M
.......................................................................................................................M
.......................................................................................................................M
............ . ... .. .................................................................................................M
......... .............................................................................................................M
....... . .. ...   .     ............. ..... .     . ..     .  . ....  .. .............................................M
....... ..  ...................Z ....8 =DDDDDDDD ....................... .8=.=,,..    ... .............................M
... ....    ..................N.?MMMMD7M777I$$I78MMMMMNII7II7IIIII     . .........  ....    =77MD,.....................M
..........  ..................,... ,M................... ....   .. ...... ..     ....========NINNN7,......  ...........M
.. .....    ..................,$....I.............. ......  .  ...  .....  ...... ..... ......  .. ::......... .... . .M
.......   .................... $..:  ............................. ................................:.~ ...  ........  .M
...... ..   ...................$ .=  ...............  ............ ........ ........... ...........O  ,................M
........  .................. ..O..=.................  ....................................... .....Z......  ...........M
....... ..  .................~.I..I  ..............................................................D...................M
......... .................. O.?. I.................... ....... .......... ... ...  ...............N  ....  ...........M
............................  .?.. . ...............  ....=NZZMMMMOMD+.. . ...... .... .   ........N  .................M
.  .  ...................... ..... ................ ....ZMMMMMZMMDDMMMMMI ........  . ..... .......N.  ...  .. ..... ..M
..    ....  ................  .... ...............    .NMMIDMMMMMMDMIM8MIO .  .   ..      ...   ...8 . ...  ... .. . ..M
.................................. ............... .  ~MN?MMMMDMMMMDMD=MMM. ......  ... ........ ..Z.  ...  ......  ...M
 .    ....................... .... .................. 8MMM,~MMMMMMMMMMMMNMM.  ....  . . ... .......:... ............ ..M
.. ........................ = .... ............... . MMMMD.   N MNM .7 MMMM ... ..  . ..... ..  ...:   ...  ... ...  ..M
............................= .... ...............  .MZMM,    ...: ..=..8M,.     .  ... .. .. .....:.. ...  ....... ...M
............................7 .... =..............   MM?=..8O=.. .. Z ..MMM...  .   .      ..   ...:   ........ ... ...M
....  ......................8.....M..................MDN.:~~. .. , .:. ..MN... ...  ...   ...... . :......   .. .......M
......... ....................,..  ...............  .MN.:M$?7M  .=$+=MMI8M7    ..          .. .... Z   ...   ..... ....M
..............................  .  ..................MD,. .M$ . .7MMM.. MZ ..........  ...... .. .~$ , ...   .. ... ...M
....  ... ..................... . ................   MM NI. . . ..    :DD=                        ~,   ...  ..  .. ....M
..  ......  ..................,..Z ................ .M8=D,N,.? ..=.OMI?.DM .... ..... ..... ......=, +. ..   .. ....  .M
....  ....  ................ .,.,.................  .DM:8=D .  .....?...~+ .     .      ...  .... +.   ...   .  ... ...M
... ........................ .,  ..~................ 7MO.~.~  .OIZ. .,IMNM...........  .  ........=. . ...  ... ... ...M
. .......................... .,....................   .Z   : .,.~:.,?M ZMD ....   .. .      .     = ......  ......... .M
.   ..........................,... :..............    D$,..7O, ,,,MDD,N8OO  ..      .  .   .    . +.   ...  ......   ..M
............................ O, .. . ...............  .,8:. Z?,$Z=Z Z.7O.7 .....  ... . ..   .....= ,. ............. ..M
..  ... .....................7, ..:................    : Z8, =.ODO N...N:=NO. O..   .       . ..  =    ...  ...........M
....  .......................+, .. ...............M :~MM7.7N:  =M.8 .$I D:7MM.I+8.  . .    ...... =..  ..... ..........M
......... ...................?,... .............8O M$MDI = ,?Z,.II.7I.7 .Z:D+$ZO$8..        .   . =.. ...... .....  ...M
. ..  .. ................... ,,.,..,.......... D, , ~M.  $,,,.. .$I IM.8. DO. ,77$= .  .  ...   ..+. . ...  ..  .......M
... .........................~. ..............~O...MMM  ..7. =::..I..?.,~ :N M$ ~$~+O.. .. . .   .M ,. ..... .. ..  ...M
.. .......  ................ O  .. . .........M8..7=MM ....:..M=..I.:~ D   M.II?.==+MN O,  ...  ..O  ......... ... ....M
..........  ................ 8  .. ..........II,. .?MM.  . ~O.Z :+.: +  I   O:$+O?,:N+,. M ..   ..O.   ...  ...........M
....  ........................, .. ........ N7~ .~IMMM .   .,~...+=? .   O  .+7+: .:M,. I 8       O.    ..   .  ...  ..M
........ ....................Z ............M.M  Z .MM78       ...$  ..    M M .MM$M..M.N?M.I      :.   ...   ......  ..M
....  ...................... O .......... 8$D. .=8$NMNM..       ..  ..  . $O.M. 8.::ODON?,$ =.    O N....... .  .......M
..  ......  .................=  .. O.....M. .. =O,MDM$MMM ..  ~...   ...  NM.7..,...,Z+O O7. ,    8    ...  ... .......M
.  .  ... .................. , ?...O....+O8,. ?.+.IMMO88M~MD...~.. =..8MDM.N 8.  ?.. ,OM:,Z  $..  8,   ...  ... ... ...M
... .... ......................+...... 8=7... :?. MMOI?,Z~DMMN$=..778MNMMM.~. . . :~,.. ..:7$.8 . =.   ...  ...........M
......... ....................... .?. I . ... 7  ?MM:7=:~MMMMMMM .MMMMMDN+D  ..    $O.O   .M= ~ .   .. ...  ....... ...M
. .........................7 ..:..~..N :+ I... . .OM:$:8$O$7M$MOMMM:7NZM$=IOI .8O=..., ...  ~$M.., Z  ....  ...... ....M
....  ......................,7.,...IZ ...8~.. , .,?~MMMMMOZ+NMMMMMMDMMMMM NZD .?::,..~7N?.. N=M. ~:Z   ..   ..  ..  . .M
.   .... ....................:.M ...+=  :8 . ,, ?+MMMMMMM:MMMM?M$MMMN8MMM+ 7N    +.,, ,.,M. ,I= .~O..7....   . ... . ..M
.........   ...................? . 7Z,. :, .. ...ODOMM?$D7MNMN?MMMMNMNMM8+:Z:: . .  ~.~~,.Z .M  .~=.   ...  ...........M
.............................. ?..7.. I..O.... .$.M7M.=MMMMM=, ..  ..  ..O O7... $,.,. ,Z,?MZ   .Z+$   .....   ........M
 ....... ..................... ? .I+I.O.,Z......+7MM ? ....... .....  ... ,?=.   :   ,,..7$8~ ...Z+Z......  ...........M
..........  ...................?.,. ..Z ........~D$I . . ... .    .  .  ..?:.Z. .   ..,M,., .....Z~Z     ...   ...    .M
..............................,7.$?8   .......  8M7.  M   ..  . ... ..  .=..Z8,?  . ~OOO+.M . ...8OZ.I8................M
.      .. ....................:$ Z~+ ..... ....~ZZ,....~.   .        ....I. .. .7.... :NZ+      .N+... :..  ... ... ...M
..  .... ..................... NMM., ... 8..., ,,7M.  .Z .  .   .. ...  . ~    .. .DMMMM .    .. O=.  ...,  ...........M
.........   ..................,MM?O. .  ,...$. 7:O$....~. ... ..  . .   :.: ... ..  ...   ....  .,,...... .............M
....  ....  ..................,D.I,...:8.  N..,~N,+   .Z :  ..  ... ....:. D....  ... .     .   .,..   ..... .. .. . ..M
.. ...........................,=D?...8I  .O.. N.,I.    =.=   ...      ...+.MD.  ..  .      ...  .,.....................M
 . ...........................I.?Z..I+:. ,Z .7=,8..   N:: .... ~..  ....   MM+ ..      .  .. .  .:..  ....  ...... ....M
.. ...........................,?D ~Z8M..D..:,~:D .  .MM $.   .....  .... .:MMM. ..  .   ... .    :................ ....M
...............................ON=O$I  ?:DIM ?~.... ,MM +.  ............. MZOMM ....... .........:,........... ... ....M
...............................,N$NM,M,:.NOZ= .... NMM8:.................ZNMM8M,.................:=....................M
............................  .  =$IZ. ~?~D  ......NDDMN,............. 8~D+M7MM7 ....  .......... =.  ............  ...M
............................+. ..  $  .  . ........M7M:DM............Z M7 I~IM?$$................ ,....................M
.......................... 8...... ...............MIMZ87D~M ......:. :MNMZN~N?IZM................  ..   ...............M
........................... ...... ..............7~OMM7MMDNNM7 .  =MO$:N?OD8? M+: ..............=.+.......   ..........M
..........................+,~ .... ..............7= :MN8+88NM7M?M:M~IZ NNONM =$..$..............=...   ................M
............................:...OM.7 ............?.I MMM??=~8NZ7D:O:?D8MDMMI..?=.$  ............=.........  .. .  ... .M
..........................., N  .$ .............O+ 8.=MNNOD8+:Z$Z O+D+MM$O:=: $+.M..............M =......... ..........M
............................$~ ? .? I ..........M .,,,DDM+MMD$ 7.8 N?+M+D .O? .M M..............M.=....................M
............................ ,,?.O +............:7, ~  :88D$M~D?O+I?MMMD8. 8?$ M.M..............8 =....................M
............................,.N? .DN............$.D M  ?.8MMNN:NMOM:MM~MO .:? II.Z..............8  ....................M
..........................  ,.:?.. M.......... M? , N,=Z~?MMDMMMND$D78=8O .O..$I.$  ............8 8...   ...  ..   ....M
............................. ,?...M.........  MI...N7+ ~?~8NDMMZ87NI,,8.Z....:?.$+ID=..........8 O....................M
..............................,?.. M...........M7.. ,IZ.=$:OMNM?I7.:I.,, ,~...$N7+,N~,N ........8 8.   ................M
..............................,?.. M.......... M8 ..8$N. +,8NMM ZN.$+:8 ..8...ZO$=?$~+8.........O O..,.. ...  ..  .....M
...............................?..7$.........  M.$..8NZ 8:,:ZIM.7N ~I8:...,. .7 ?78,,8 .........8 .=. ... .............M
..............................,I..7$ ..........M,II... :,:88$$: ~,.OI:~...,. .~?=:8~$=.......... .7....................M
..............................:?. 7$.......... M8.. . .:,~. $N    .I=... :,....M$$.D,$............I...... ........... .M
........................+ ....,+...$ ...........Z. .N .: +8 .? ., ..,. , +=. M ZN.D 8 D ........=~ ...... .............M
...................... =......Z?. .$ . ........:8...:  =,+==N?.$7 .D:....,, .=ZZ:Z,Z~Z.D ....... Z ....................M
....................... ......,?. .Z..........7:M. .M,.~.+ ...Z=  M,.....=   DN$:.+.N.N~= ...... Z.....................M
......................+........? ............ 8.M,.:: .~:O+DN ?+  ..I ..+I.. 7M=+Z:7:+ +? ...... Z.... ................M
...............................+I.............? M ..M .~:M7IN.::..I.8 ..7+.:IZ .7:?:7+I.Z. ..... ,..  ...... ..........M
...............................?.... ........ . M..,~ ~~~D. M. .... . ..DM:.IM N.N.Z.M M.:.......  ............ .......M
...............................+.... ........ ..$   ~.DI=8=DM..,..,Z 8 .=~.:7I.,7.=+=O=O~:,......,.....................M
...................... .....~..?.  .......... . ....= 8.+D ~M. ...  ...O$ . ?D.IZ D7+,+8=OM......+.....................M
.. .  ................$.....:..... M.........    7=?.  =:Z+ N .... ... 8: ..$7$D =~~=.=Z:M.:.. $.,..............  .....M
....  ................M..... .,...7+ ........  ..I8.7.D7.DN D.8...=...... ..?,$8 ?I~Z.77:$:O.. $.:.... ................M
.......................? .  .., .?I .......... .,77...D :DNN8 . ..,,... ....$.NMM+:?,8 :D.:ND..M.. .  ......... .......M
.................. ... .......~?,............ ..I$7,..O,,D: :....?  ..... ,...?,N:O.$O~~8D$D,..N.~ ... ..   ...........M
............... :====, : , =++M~............. ?.87  .:D.?M~  ?.. $........: .. I.OI?ZZ.N~Z... .M=====+=$MMMM===M== ....M
............................................. =.M=.: .DZ::+IZM  ... ......O7:.~8$ I:M?ZN ... ...  Z$ = ....+ .+...+....M
.. .  .......................................NM.M+.+. DZ: .~IM:...:..=....8+:, $$$8 I+DO.....     ..  .................M
............................................ NN.$?,  .M$. N..MM...I:7~..,. +I?..MDO$+~8 ............   ..... ........ .M
.............................................M8.$MM...MI .$IM8IM  . 7M.... ?$8O. I+? MZ ......  ....  ....  .. ...... .M
.............................................$?M +.  .MI,::. MM+:~ ,+?: ..... ~+.8??+$ .............   ................M
............................................~+?M .  ..:: :~.DMDZDMD 7,, ......+..::+8,.................. ..............M
.. .........................................N+,M.::,..ZO:~:~M$O?ZZ. :.,: .....  . $$I .................................M
............................................D:?M. N...:8+8? ,8MZ7M: IN O=......+...DN...............  ...... ..........M
............................................D,+M.=O   .NI?+. IMM=MI D,,N::.. ... . ~+..... . ... ...  ... .............M
............................   .............8$O .=O. 7 8NIN.M7+DMMM 8.7.,:NM8N. =. =M ..... .... ...  ....  ...... ....M
................................ ...........ZN8 .$$....DONN..?MZMNMZ7 = ?Z:Z$.7? MO ~..... .........   ................M
............................................NMD..,N...:O:8 N8MMN M7,. .N 7:..,I..MON~.................   .  ......... .M
.............................. .............DDI~ZN7 .. ::Z D7:~ONZ~.,DZ+..~,.~:..++7N..... ............................M
............................................~.=IZM.=...:II OII.=MDON~$8,,  $Z$I...~Z?...............  .................M
..............................................O.$ ~~.+$=:,?$,O$778 $II$ D+  ..~.. =Z................... .... ..........M
.............................................M,=.:M7.7~~=.NMZ~OMNMNOM,D.~,+.,+..  N . ..........  ..   ...  .. .  .....M
............................... ............. D~78OM~.M7 .OD: ==MN:8N:+M~.,+..  M7 : ................... ..... ... ....M
...............................................+..MI:~.. ~~NNNM$$88.. ONM=+NNZ....N............................... ....M
................................................M7 =,.,+,7M$$MI87Z= ..8Z7$,:M..M$ D....................................M
................................................Z.N=MOMMNM$MMDM$MI....?O7=. O.8OO=.... .............  ........ ... .. .M
................................................ Z=$ $ZZD=MO:7Z$8...:~O=ODI?MMDZ.......................................M
..................................................OI D ......M+=. . +O.O+~,8N7 ........................................M
................................................. OZD..~7.~  MM .......................................................M
.................................................. ~,8 D.~,+ M+........................................................M
.......................... ..... ................. ... ~MMM .I...... ............ ..................  ............. ...M

""")

page91_art = ("""

        ....  .................. . M., Z ......  .. . .......................    .... M=.. ..........................  ....................M
.   ... ..............   . ..  .. .?.. =:+ ~MMMMMMM.7 ...~,. .  ........ .   . 8MMMMMM7Z I     ... ...  ...................................M
 ...............D:.   ,, ~  :,:,=?NN+ .    ,,+MMMMMMMMMMM=:::::::::,:,:MM?:::::::::7. ,MMDDDDDND~ . ...  ..................................M
. .......... ..... D ~.   ,Z$Z=........   ..   ..  ....... ........ . M..,I==++=~ $ZZZO .... . ...   ,+++++=++IMOI.ZZOZZZ7.................M
 ............ .   .~  ... .......... ...   .........    ..  ..........~.......................................... I   . ...................M
 ....................Z.I= D ..........................................~ ........................................7  ........................M
 .................... ,I Z=,.......................  .................~........................................M...........................M
 ........77III77777 ....7 ,=?7...... ............. ...................~ ..................................... M  ..........................M
 ....... .,..,..=Z$:IM87?+???NZZ$$$$$$$D+?DM+++++++++++++++=..........~...$Z$Z+++++++=....................+ ,N ............................M
.................. .~7, O ....................... DD  ,,ZOZNN~~~~=++=,.+88OO8OZZZZZNNNNNINNNNNNZ7=~:I,?,:...~, ..   .     .  ..............M
....................$.?~ $.......................7.8I:.........,,::OZZ8:,:,..  .. . ~~~~~~~~~=OZZZZZZD8M=++:Z.. ......  ~~~~Z:.............M
.....................,.~7.= ......................D.+=.......................    ,.I=. ,=: ...................   .+++++ZZ. ,. .............M
...................... 7.$$ .......................~~8D ....................... .:IZ +........................ ... ..M.=:D. ...............M
....................... ~.I+,I .................... .8DD ...................... I,I I ......................?7$:.. ?I8$.M?I, ..............M
..... ZZZ,,7ZZZZ,,,,,,,     ~,=NN$$$,,,, ...     . ...~N .................. O..+.?,I  Z .......... .,~Z7~ .:ZONN.. ..  . ~Z.   ............M
..... ...... . ,III???I??IIMN7MMMO7IIII?NMI777$......., MMMMMM77~..77777$.... I +DZ~... ........7I. .,7ZI  7?N777777$~ .N?.................M
.... O =.. . ...    .   ..+ ?.  ..... .  . O8......   7$$$$$$$$$MMMZMMN,ONMMMMM,..$$$MMM8?????: ?MZ+ ..  .D: ........ :?M .................M
...... =MMM8,   ~~7,.N.    ..DM~8. .........DD=. ................     8O... . .... .    ...,M:Z~~DM8:~7MDM...........ZN..8N=M8N,...........M
.....? ... :,D8:,,DI $M$.........?N$N , ... .N.  .....................~.............  .D,M  +D=.....  M$M.,8....... $+ :...................M
..... =  M. . ......N +N.~  .   ...$?NMZMMMO..?.  ...   ... .   .... .8........... .:.7M$$ I    ...MM.M?..MM ... O7+ M,....................M
 ...... ?,I.. .......I.~,,MD8. .  .Z$:? ,,8O,,.,NNNNI   . :,,,: $NNO 8= .. ..    :8,8M,  ,+..N?:DNN. . ... ......$ IIMMN ...   ............M
........ O.D,D........?,:    ==D8ZO.$:?... N.  . . ...  ~M8..  .===8MMO ...   ...:N$, ..MMM=  .  .N... ..  .  .. I.M M.. . .==+N. . .......M
........ ..+ MO. .   .  IO  .   . O?7,7......D.   ..   ..~.NM  ..    .    . MM=.I,. N8 ...  ....NMMMMMMMMMMMMMMMMMM=..... ...   ... .......M
..... N.NZ$,,D8... ,.+ND,.NN ...... ?~M.......+M.     ... 7 Z O ..... ,,:N7.. =O.O,.,  .I :::..... ,: ,:+IMMM=:,,,,,,,  . .,.8MMNNN   .....M
 . ,.ZZ~ ....8=:=~?OOOMMZ.$8....... ID+~, ....$.:$~Z....... $8............~  IO,OZMMMO...D.DZ  .........=M .................+,    .........M
$I:.. .. ... .D,I77. ..   ,OI ......? =7I+:..7Z7. Z7M .... ?.I .......,?..==IIZI?7D..III8877I.=7........=I..................+..............M
 7=,........ ?~M$.... .,7~~....7Z+..?:=$.IM..=8Z7  ?.N.......78........  .:MDOMOM$MMMMM?M8$8MN?? .N :MM~=I. ....:$$$$$Z$$$$=I .............M
..~O8  .==+=MOZ==NN$====8NMMM?+?+==..N= .$+.MZ~ 8:... DNNNNNN?8NNNN==== ,D. ~MM........OZ.......MMN?+++++M?+++++MNN:NNNNM++==++OZZ+........M
...88OM.8=  :  . =$.. .M .... :::IDN~ZD8=+  M  ..,NI,O=D..:......ZZZZZI:$.:8.M ,=.ZZZZ8=,O 7~~~.7.8+~. +......... +?M 7.......... .........M
.,:$ OD ....D+ .  .7~N.M..=...     M.. ....,O.~....MMI,$$.8 ....... .  7Z$?MD?...,??????+...8O$+:NM,MZ.,  ....... I7$$.........:.?+........M
~:..?NO:?MM7===~:?==MMO8M++8MMNNM$D+7=~~++$OOIZ?:. O$O.D88.O ..... :,..,.N7=.:,,.,? ......,,Z...$O+7.~:O~ .   . . ?M$  .     . I? .........M
..+8....D........ ....== 8:+ONDDD8ZZ8N7.8NZM:8O78:Z8....8OZ ,  ...D   N+: $      ,N ..    ,I ..D,..IN,~?:.$::::   .87.  DDDD.~8 ...........M
.=7.    ..    ..8,....~?.8=+ ....... M . N. O8.,,M8 O... NID =....  :?==ZMDMM=+?+?,,,$O$OZI.=M:,,OZ$,. +N+==+ZDZZ$Z$ZZZ$:$OM?D8= ..........M
~N??.~$77NM??II?~???8. +MMIMMMMMD77M.8$M,.$I.7D..  $,Z....=ZMMMMMMMM.. =$,+?.M .. ...=. . . .7+,.    :. MM,..8.......  .M,=I . ...I........M
$N...  .. M~ .     .8   M $7M?M =7DM IMM$N .. =..I8.8.. II?. 7 ... MI? +  .:.M.7I?I8 M +7D7 8 .8 .??I.7I$7 .$:.........MM?Z..... ~.........M
.D ......  .........O....::.. M  ..::: . 7~=MZ=O$ .. .MI, DO I ...$:. D OOO=+ZO..+MOOZZMOOOID$.=OO.  ...=?~ M ........ 7=D.==.8.,~ ........M
.8MMM7.   ..?..MMMMN M7..MM$77:N7778:MI$ZD,. M....Z...$?D. M.8O ..Z...,.....~7 .M:.... .$...+. ... M...~.MMM+MMMMMMMMMMDMZMI?8. ...........M
... .?O........$. ........: :......Z ...D . . . I?D?$, Z,. 8=8= .I, ++7$$????O+IOI?I???N~ ?M???IZM?I$I...M?.........$. ~:...I .  ,~........M
8===I=:M====   .. ... ... ,I+  . ..?. ~D..MD=$ =....Z..==. M+DOOM: . ....N...7 ....+,....M M  7     :D:.=M?....... .M. ?.  M+MMM8. ........M
N:.......D.    :DDN.8I ..~DDMMM:,,MMM8 O. ....7. ::8 M.. MDNZ :  N 8M::::8   7$~.  N.   .M N:+=M:DD... ~ 7~:~::::::?NMM~MD..  ,Z  .........M
M... ..  D7 ........D ....=?....=I $.... . .N=M$M.. 7M   D$~O.Z  : .. .N.:NDM.~NNM ..    $$M .  N.. .MM7.$.  O    .M .M. .....D?.  ........M
,,.DMINM. ,MMMNO.. .. . ..D? ...~.~..,?.,  .  .,8 ...~:+.M7.M.ZI. ..   N. ....= .M....   $$I NMMN+  . 7..$O..O....   $MM ... ,=MM8.........M
.....M..  .  .$:~~~,:8O~?8MMM8888MN.:. .M ......8=8~~=, .:Z.M M Z .,, .~=~N=I~=$8OOOOO8.O=IZ.:  ...  O,=:Z8 ZO...... .$D .8~8~. ...........M
.D$$$... ...  Z........7. M?.:+  8O....= .?IMII.:  .....IN8MZMMM$... .~ ..  +.$  .... 7.+  7 N I$7I8~  M =: OD.I,.=$7MM??7D.... $+8,.......M
....   ,,:MNNNO....... .. D. ~7 .,MN D,N~,~. .. + ...NNIN.M N.M?N 7 .,,,?MN  ,,MND,$NNMNDMNM.,N8   ... ,.M,,,,,,, 7O.$,. ~M  .,+,D.........M
.O....... I   ..=~ I,MM=~~===~===ZD ?. .  :... ? ZZ7,...~ MM. M M.M ....?..   ~  M ..      I   .   OMM . ZO.......D. Z...~ .8~8:. ....8....M
....?I?ZM:M....    M .... M:.... IZ.M   IN:D~7....Z+ .$MMZMM7MMMM$O.,IIZ    ..=~.M .$$ .$$.~ ID.M7: .: +MM.    .  8. M.?7:D,.N.  O.D=  ....M
.....    .. . ?$???O+    .N   .. O.Z=I?7... Z   +D.+Z?MDMMMMMMZMM?MOM~...7.O$8M???7MOM?7MMM8$:+...M?MM78DM????????7I?$MZ....,7+?~M...7... .M
N==.~  .  . N ...,,,.O87OOMZM,,,D8$.. $.. .,O:+8M7. .MNZN=MDMMMOMM8MM?:  .M .M.. .  8....?+  +NNMMOD .,~MMI,,:D,++MNO.... .~~.N. ~+.IDO....M
  ~=ZZN ++:::  .. ........=?N...~7 . .7:DMN7.   +Z ~NMMMONMMMMMN8MMO8NMMI:DDDM:8OZZ8M:.:~,?I8=?,:==MDDDMMOM..,N:.. .I    ,Z~: ..7+7O?,.7: .M
.....  .. ..,,, =+~N87,,,.~,O,,,:MOO$8~  .D.=8~,O~:MNDMM:NMMM=MMNMMO7MMMOO7:DN$~Z8~7+8M+$MM$+?N:$Z,,+OZZNM8  :D . .=ID=?$IN  .ZDZ:D,,,,D...M
 ~=  ..?....    = . .,,,OOMI,,IMOD. $....=~,Z,?7..OM??M$M.MMMOMM8DM7MMNMMM$=$= Z .,,,,,,,,,?Z~.,... ...7IM===ZM~=+==MMN,:~M 8Z~Z.=:,: .....M
.:DZO::=::ZZ=:::? ........~...+D $ .?Z?88 . ..+OZ~MNM7=MNMMMMNMMMDMMMMMMND::= .:. ....?=II. .  .,:::I OZO7.  .  Z ..N.. 7=MD+=:8NDOD?Z.....M
....    .MI.. =~ND8=+8ZZOO=+++=MMMZZ  ..M..,OMD$DO8DOMMDNMMMMDMMMMMNMMMDMI.~8$.?ZZ~MNN8ZZN+:DZ:ZDIZDDNDMMM .........M.=:MM? OIN$ZZZZIZ$$?ZZM
.?M?8OMDMN8.......+  ..  8. D.  ~8....?NMMNZMZO??++IMOMMN$OMMMMZMMMMMMMMM. .???NMMMN$?8 . ~,,?NI...,I??M$M8. ..... MMZIZ.7MND$??~++.. .....M
...,7~?Z=,=:D:7$O$MMMIIIIM. 88.,IMMM~:?INO?   87NOZ$MNMMMMMMMMMMMMMMMMMM.M7 :.,? I.: .  . . .,.. ..78IIIIMM7Z7III?IZO:~M7N$$M$MM7M8:$~~?  .M
 .... ........,ZZOZZOMM8O ZMNN7~.+,=$M.O8O8.,++:+MMMMI?OMMMMMMMMMMOMM=MM.N.=N7~M M,=.MI.?.?:. ~7.8..:.7=.MM+$MND?+D,N~ZMMOMMOMONMODONMZOM=.M
O~~~~~~~~~~~=~~~I++M~ =8MMM~,8+87..+I +...O7N:.$M7OMM:,MMDMMMMMMMMMMDMNZ.N .    DD=?,$I.I:.I:,:D8~~=~~~~,~:~ .~ ~7?7=,I87,I~O. .  . .  ....M
....... .   , +~.I.7.$.:~~7 . ..  .   =. ?..ZD+=?I,M N   DMMMMMMMMMM::~..,II .  .....8~.I=+8.7+.??:+77 :DO      ........      . ..... .....M
O,++=.  .  .. .. ....  .. ..:N:7? I,=$.ON~:.I+?Z??8 ..? .    ~MMMMMMDDDM  D:+. ...... +OOOZZZZ?O?. .....  .    . ......... ...  ..... .$O7.M
...............           ...   ...  .  . ...  .:$ ...~MMMDM7MMMMMMIMMMMO. ?+Z~N~~8:,O : ..: O: O~ I$.7O.Z:,OD+=$.?I.7 N8+~:~  ,..,........M
..  Z7.$..7  , +...  .,.. O :=..+.+.M= O =~,7$?M=..~MMM..    7MNMMM~..:=M8 ..M. .  .       ... . .. ... ..    . .~,D.+.    ~ $ .DNI,M$=MMM M
....    M:N N ~M O .~.Z.I O.,Z D= ~ 7~I  ..,..MM  Z.7MMND~?~=7MMMMMMDZ8=?:MM8 8............... .  . .........     ..   .....  ..  ..  .....M
.....  .   . . .. . ..., .. ,:. ..  .$ M8.+8O8O..D..?$OO88DODMMMZMZMDMZOZNMMD?D.D7,+Z 7  8.?.    . 7 D..~ +,I,  ,~  ......... ...... ......M
............  ........ ..........  . . .7 :I7N. MM. ~IM:.   .  ZMM8M.....=+Z8 7:.+MNZ7M$N$$D$Z?:MI+$ Z.?Z=$.D.Z.8::7.?= ...... .  .  ......M
....... ......................... ?$~,. .::O? .8MD=..7N...+IOI=~MMM= .. ... ?==MM ,M:$8?I~.= 7 :~,I,=~ ~.~,,.,I.I,,I ~I....  .D: 8. I=.. .,M
....... ....  ................  ...  .. ~= 8  DZ+,I..MM7??,~87OIMMMM8MZ=I=..M?MM?.Z.D. 8DODOD8=8~?O,Z~=O~$.D~+~?$.:O ,~  Z,8~,Z+,8 ,ZI.. ..M
.............   ... ...  .  . :::O==DM8DMDD. N+DZIN:.IMD7$=::+MM8MM$?NIO~:M8M~$M$....M +?.8.I,:?.+  ... ...   . 7   .   +.,D ..............M
...........O?:? $.$ :+= ~:+ D $.N $ O ~.7=: ?M8. DOI?D:?..  .. .MM?:I77DMNMMMMDMM ... N7II?,  =..........~  =+.=I..........................M
.....    ....8.$.,,+,?~~::=+= I., ,?,:7.O= I  M~  8$DN  ... ....MM........ ?MZM:= ....7.  .. .. ............ .. .=...  .....,...... .......M
.............. ,.8 . D.=.~.? ,.:.+.$,.IZD D . $MM.,MZDOZ~,,ZN$ ?N~I~,~OIDZD.MMM O: . D$.77.,D==Z   ........ ..... I.I 8$.Z.O+~D.ID.++I.....M
................... ...  ..? 7.7.~ ,.,?$.. ....MMINMN+OI:.,Z8,~:M=7:.I=Z$8$M$$,.D+NND$?::D:,8:... ...  ......... ..:::,.,... .:,,...:,,,,,:M
.................................   :.,7. .....+.7MNM~  ..~.:. .:I+.:=~:~77M++++ .+.   . . .. ..............................  . ...  .     M
.......  ..   ..................::::::~=......87=~$DM ...  ......  .. . ..,M...  ..........................  ..............................M
 ...... ....  .........    .  ...   .,.8....=~=:,,  MDO7~:Z$= 8D,~+~$$,..OIM~:=:,.    .  . .  ..        . .. .... .........................M
...........  ~.. ..+ ?.D+,D.N O,=8,7D7:D:NNNO ~D.:$DMND?.+7Z :$=?,$N7.:=ODOMO+ ?+,7 7.O O O+=$,?8 +O.Z I.:.IZ.Z.$,:.= +. ?  . .............M
....... ...  =.?7,D=?~~I+,I~7.7,+8.=7.~N.::=8.=8: ,:MMI+,.OI IZ8=,ZD7?,I=88M7=:?,.,:I.I 7 I Z?.,I.,:.7 7 7?.+.7.?7=+7.77:7:7,$M7. .........M
........ .. ...::,~ $:.7 Z.7.IZ.ID.+$?=7?=:?Z .DIZ~:D .. ........... .  . .DN~.D.$.8,I7,? D:~$ ,I.$I N.7,+=.8I7?..I Z8 7 ?..  .............M
........... ..........  .... I...D ??= +7~.7=.,7$D8$O8 8D. ~7: ??O:,,8O=:,D$O ~=.7 7..,. .....  .. . ..  .  .   ...........................M
 ....  .... ..........  ,  .. .: ..   .. ,...   . .87NOO ZIN.,$IN~:~ZZ=?.,?M= ~= ,...    . ..:..7.. . .....................................M
.....   ...   ....... .=I,: D,,.................... 7O8,,,7~+,.$$:.+8 , .=?78.,         ..  .. ............................................M
.    . . ...  . ...... 7I7++.....   ..    ..       .7 ....   .. .   .   ... D=========, .....:..I =........................................M
 ...............,.Z, .. IO,+8~,.$............. ?=7,:M8~ ,............,,?,:7IMNN8.:Z.:Z,.? 7. Z Z.D~.M  O M:,+: ,~ .........................M
....,7 $7 7Z.N,.? Z.OI ...    . .. .  ..D.Z,.D?.8MMNMM:?8M.OM..7$:,~DO,+?,MM87NZ,~8 ,8.,+.7 .8 Z,~,.I .$.MO.M:.=...........................M
..........,  M 8D.   .....+ .D+~$ 8 .8 ?:?N~ =D?,7?8:Z MD::8N.,IM:.?D8O  ~,:.I?N.+O =Z :. O ,:.N $, 7.,7 ~$................................M
.....  ....   ..................   . . . ... ..    ,8.  ..  . ~?.   ...    ZM= D+,+,.7  ?.Z. $ . ?D.~, ....................................M
....................................  ==... .  . .=,O.MOD8~I+~.. ,IDOONM$D.MN~,$I,,+:. ?~ I:  7+  .,  .....................................M
.......  .. ........................ . I.~=:,$D?:+.MD  ...=O88MZZZZ=IZO, ..7.  . .. .....   ....... .,. .   ++,O~,~.,. .I..................M
..  .       ...............................:$,.7?Z8D..... .  ++~  ........:~........ .... +=....=+7 I,~D ~I N$:.7$~  . ....................M
.....       ................................+NZ?DMM, ......................D87 , ,.... I:~I 8..,,$+ $? 8:~N.  ..  .........................M
............  .............................     7Z8M........................OZ.=.$:~N .... ......7   .  ...................................M
...........   ..................... .., : :. ,:O,II, .......................8 ~:+D=,$+.+? .................  ..............................M
.... ......   ............:DZ:. Z :?,Z.$ 8.=I,N:8M~. .....................7$D.+Z.=:,8..7+,7.= .............................................M
.......  .. .................:~~.+.   I.,I.8=+8 ~D ~ ......          .....$MZ.,:,IZ,7 .7~.++.?..I..........................................M
.....  .... ..   .  ... ..... ~ +8 . ,. +..D~I7.?7:~ ... I.,I8MMMII,..... $??8.I,?7,D$=+8 .. I?:+.+Z+......................................M
........   ., $~ ~:I,~O$,+$, ,?,.I I.:OZ8~+M~~7,~~+= ..........7+,...... :?.  ~~~~~~..,.  ...  .  .........................................M
.............. .. ~D :I.:+D... .D+~I.:I~,.O~.Z. .?=O...........D., ..... 88..  .. . ....  .... ............  ..............................M
........ .. ......   :..=$, ,...=.N O:7.D+III,?.?OM, ..........M ...... ~.$...... . .....    ..............................................M
.....    ..   .........   ..................   .. O ...........MM...... $M  .. ............................................................M
.....   ...   ..............................,:?D~ Z.7 .........M?......: MZ:7~ OO..8+    ......... ..Z...?.................................M
..  ... ....  ..... ZM.=,:8.:Z7:.N?.+D:~N.~D7,7I: +N...........N ......N.8N.$I 8O,,O,.?=.N7.$, ............................................M
.................................I .?D +==DDI..N.INM.8.........7...... $INN....$I  .:.N. ++.=8, OZ,,D~,=+. . ..............................M
........ .. ............................... ..... .:...........7 ..... .M.............M=,?NI.~DO,M:..O..NN.=D.  ...........................M
.......     ................  .......:,,..$8.= .... 7 ....  ...7 .....D,?......  .  .:?  ?+,.:$,.ON..O ...........  .......................M
.......  .. ......   .,M.N=M~ 7 ..,   .   ..... ... M ....  ...M .....DM7O+  ,., O:=D ?D7.. ........  .....  .....  .......................M
.....    ...   :.O.,::I.:D.N.8$::I.?.:.. .  : .,, ..7..........M+... $ N:ND Z.:,78:.O .....................................................M
..  .    .+.?..Z.$ :Z=+?.. ..................$~.N.,N ~.........I+.....,, += ..    .........................................................M
 .... 77$ 7 I ,I I:O........................... :. O ~....  ... M.....?=O:+8 = ,=.. ..  ..........................  .......................M
 ....==Z: I.,~ 7=,7.Z=,............................Z.~..........8...~~MD7.I:IZ O.:+.7. O,..................................................M
.........~I.,$~,.:?,=.N8:. .........,.,,.,O,7:.?:.8 .~......... 7...+.MOM~MN8M.8:~=.7:.7DZ.................................................M
.......  ... + : I.=$7ZNOMI~N,.,.I.7=.7+,,?.8,.O,=M.. .........7M ..8 M7M787N7IM~N$77:=?  . ...............................................M
........................ :+.7,?,7D.O$?+OZOOO??.+?:N............7$.. O M=,. . . .  .........................................................M
.....  .....  ...........  .  . , .7.8..:=O+,=?.DDM............77 ..Z.DD7:7$,N:=DZ.. . .  . .   ...........................................M
..  .  . .. ........... .O8~:     . :::.~:8NDNO8DNM............7.:..,.NNNONODOOODDD~~. ~,.,  . :...........................................M
....... ... ...........  ......................  .M............:.: . 88....................................................................M
 ...........................................~,ZD.8O............D.: . ON   ...  ............................................................M
.......  ...  ................................~.7+M............O : ..:$:+NZ=.....   .......................................................M
.....    ....................,++.: ........+===M8M7............Z.N .:=OO.=7O~..............................................................M
 ...........  ......................... :=I.O.M.+O=............~ N .O8MM8$77,77~8$~DM== ~..................................................M
........... ........................+?~8,~ ??7ZINM=. ..........8 N .,MI   .   ...  . .   ..................................................M
........    ...............................$.7~~7DM............O N ??M++.N:=+.,8~,M..~ . . ................................................M
...........................................    ..$M............7.N  M:O7,N~ +:~ZO $~,7D?7..................................................M
....... ... ......................................M............7.MMMO ,..8N.ZI,.$,MO ..~$. ................  ..............................M
.....  . .........................................O............7 =M?~:. .   ..=N..  .. .7 .................................................M
.....    ..   ............................ . .?,$ N,..........~ MMMMMMN=?,=?~  ...O7~.. ...............   =..... ..........................M
.....      .  ............. ...:.:ZI :N, $.7::..:.Z~I ....  . .,N8$DO8.:7:,..... .....  ..................:+.~. Z,.=.. ....................M
.......  ...  .....    ,?.O.,=,.8.Z I,I$ D.M.8DMM$ODM~ ........ ?N.,NZ, 7~.7 $$ .    D.,.. .................,$:.~~,D  I+...................M
........ .............. ., +~ZO.8Z$=Z$:I.?~7 ,~=MMMNOMM=MMMM==$D,+,.Z , +Z I.,7.O.=,~..O.$.7.+I 7.. ... .?~ .?$ D :8 ID +..................M
....... .....................   ....7.~+, .D..:~DO.I8?8..? .  :I~N II.N7:, $ ~? I.I?,+ I.7 7.,.,O?MD7I=? .7.:,7.I.~:.,M ...................M
.........................................., . ZZZZZOMMMMI++MMMM 8?~8.~D +..Z~ 7.I..I . 7 7:+.$$=,+ ?Z  .7.7D.$.:D Z .......................M
.....  .... .........................................D=+8MNM8NN.8:8O~DM,N. ..... ....:  .........  ...?7 .,................................M
..  .    ..   ....................... .. ..   .......O~7~:N :.N.. ?,,Z.,I.7....  ,O,.D 7.?N.?Z..Z .........................................M
.......  ..   ....................................... =?,$II N+.  ~.7~,M,7$. ....     . .  ................................................M
........ ...  ........................................D:.Z?~.N, ...~=,,+,,N................................................................M
....... .............................................:8$O.?,,N.7.  D~ $= ZD.D .............................................................M
.....   ........................................... ..=N, 8 O?:D .. ~=8.:$.78.. : ,= 7 ..,.     ...........................................M
.....  .....  ..................................... +I.D,+=.7.=7....:77~~:.::..  .....       . .  .=.......  ..............................M
 ........  .  ..................................... 8?,=.?7 I.+I ..  7I.I7.7,~.............................................................M
..  ...  ..   ......................................$.,= N O,.D~ D ..D .=. 7,. ............................................................M
 .  .         ......................................+,I ? ~Z Z~ D,..+I. 8.$I ~I  .   .   ..     ...      .   .   .  .......................M
""")

page92_art = ("""

.......................................   ........ .. ..    ................................................................................
.................................................. ...  . ..................................................................................
.................................   .     . ...... ...  .    ...............................................................................
................................... ....... .....  ..    .   MM .................................................................. ...   ...
................................ ....  ........... ...      ND.M ...........................................................................
................................... ...   . .. ... .......M.M,.~D,................................................................ .........
................................ .. .  .  . ..     ..   ?Z.=  . =NO.........................................................................
................................ ......   . ..        .8M Z7......OM. ..................... ... ......................................    ..
................................... .   .......  . . OZ??MN??+787 .OMI ............. ...... ...................................... ...   ...
...................................................,O~ : ..  . ......,N ....................................................................
..................................................NI    ... .   ......IN, ..................................................................
............................................... .+ 8?. :D. ..,...     ..,N .................................................................
......................+..?~7$$$$MMMM?+........,?. ++.=7$$$$$$$ .  ........8.................................................................
................ 7~ .. .............D~ ......+,.. .N  +~ .  .... ~,.7...~~~~8  .............................................................
.................  ............O. ,ON======+MOM .  .,=7MMMD ...$$Z.. ZZZZZZZ$M.  ....Z.=+~.~===,..+=........................................
.............8NMM,.............. ...  .   MMM$M, ,   N     ....,MMMMMMMM+M MMMN+. ..  ... ..   ... .,..,Z............... ...................
....................    .,=~MM==,...   .ZZ ..I....~NM............MMMMMZO8OOMMDMMO   ..... ... ....~N8O.... . .... .... .....................
...................,...................7:: ....  .ZD7   .. .   .     8..,D7 ...OMM~:,....NMN  D......MO:::,:.:+MND.. D  ....................
..........  ..:~~....  .  ....      .N.........7=~~M.      $.  .   .... :MMMMMM.. =+.... M,~~........................  .....................
...ZOO.8=.          ,.:~.MZ==M:+Z7DO+.D,..........:,.O88OOOO8..... .M . 8+~~~~~~~===D~O=MMMMMM  .. ...... ..................................
..............MOMM=:,==?MDZ .  DMNM   .+O$ ...... ~.........MMMMMM..+8O..:OOO~ . .   ZDMMMMMMMMODMOZ8:,I$   ~7..............................
....................... .,, ....?,.,$$ZZ......   O$............ 7,,,+=    ..  .  .  D:+NMMMMM8..,,.~,,,,IZZZMMM?NMNNMMNZO$ZO~.+I ...........
.......  .  ......... .. .  ...M +.+++.:........+ :...    ..    IZMM .  ..  ......=..8,:MMMMMMMMM ~OD~.?8M7I$+?MZ~=7DD ~OI=.~?OZZ~,... .....
...............I.?,7D$ZZ7+77=Z. .+.  .. ....   ++++++.    .....,.?M?.++ =?+?=...7..M MMMMMMMMMMMMMMNM+?M$.IM, . ?MNNM+8MMO$,+$ .............
.......,,,IZ=:ONM.=7NMDD?Z~~$...7 $7..$...?   .?.,,. .,8 .  =  +NMMM: .++++~++++,+.. . N:MZMMMM8$M+?NIMZ?M: ZDMZ=...,. .  =   ........,8  ..
.. ...  .~I7?+O$M+:..$IMZMM.~ZZN$...::+++=. ~+M+.=++MMMMMM~ .... .. . ...... . . .    8=M?.NM?~=,+.,7M.:.+=.++MMM$MM7~Z~7.:,,+=.I........Z  
..,OOZZMMDMD7+~.........?O ,,Z: . ... .  .=..$+====+=...========D.....======I=D:..,,,+M8 ,8.OO8=++MMI.=M+ IO~ZNM7~======,.=....~+ ..........
N=.... .O8888888ZMMMIMNMMMMM888MNOO88888888OODMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMM?MMM8~MMN8MM8MO8I8O88O888MM888888O8O88888OO88 88.OO .
:++?~DNMND7?,.....,. ...888O88888O8O .~~~~~~~~~.~~~~~~~+MM8M=88MM...,=~~~7IM8N,D.M,MDM ..$8MMMMMMMMMMMDO88.?+N8~ .8M.$O:DM.MD:7=?:NM~~,.~:..
.,.. . =:,7MZ=D8,=.~   ?~~~~.~.....~~~  I: MZ,M?=NMO~N?+=+MD$...... M:MO.M8.O.M O+:O ?,DO??+~~ ..,..........I .~M~.  .  .  D, ,. .  ........
.............. .  ...........:~.......    :D,IDM 88.MN . .. ........ ..$ .  ..  ....      . ...N........:, 7.NNN?,~O$ZZZ.?Z ................
.............. ........ ++ONDND7?,,.,. .. .  . . ...  .............. OM= ~===~ ................ ...... .  .: . . ....  ..  .................
.............. .............................................................................................................................
............................................................................................................................................
............................................................................................................................................
........... ................................................................................................................................
............................................................................................................................................
............................................................................................................................................
............................................................................................................................................
............................................................................................................................................
............................................................................................................................................
..  .... .. ..    .  . ...... ...... .......  ...........................................  .................................  ..  ..........
""")


page95_art = ("""
...................................................................... ....................................  .......        ..  ..          
..................................................... .. ............................................................    ..    ...    .     
........................................... ...... I+?Z.... .....  ...:  ... ,:, ... . ............ . ... ..  ..  ...                       
............................. ,~O .:.,OIZ=78O$O....   ... ~NNZ,NN N8?:N,~DNNNN::O 7.Z$8MNO...  ....  ,7O$,~8OON8.  .D. ..      ...          
....................... .=.$$=87$~=~:7MI$~M8N ,  :.... .OM~. :+M= MO ND.?$ .~I,~$ 7 87Z==DZO,,8.:$..... .====~=M?+.:7ID.I.8: ,. ............
................  .  ..$:~?Z?Z,7.=:MMO  . ... .  . .~OZO?+~~.  ..   .?8$..... .=,  ,.    =8I7O  =+...............8:=:7=...I$~:+IZ...........
............... ..... =.I?$Z ... .  ...:~I$8D . .. =... . ..+..... ... ....M+++8ZZZZZZ$ZI..  .+++=.. DO?........... ZD?=:I7?77.Z  ..........
................   ..: ?II...........I+, 8   ......MII,IMZ ZN+=8DN~? D .....DDND+~.ZM$Z7 D ,:NM~:ZZM .?O.$..+.D:I7.,   8M~DO$D8?, .O.=,.....
.....................I.  . =I7ZM:: .. ..III...IMMN$8Z::8~.D8I~$MDZ .. .....   . , ~II7$~IIO:I7I::?MM  ... .., 8.+O 77:O+,+ ..NI=ZI7,=$D? ...
............... .. .=~.I7?$$I8: =MNMMMMI$IO:+~D?MOOOI .  I....?       . . ...    .. ......... $:$M,+M ?DN=  . . ..... +.,IN?..ZZ~Z$. .   ...
.................. ~~,OZ.?$.. DI~=+MDD,..,. .. . . .?.,7N$:  ...$I.,IMI.:++,+=OD= ,.., ......   .  IZ  8.DN,8MD=  . . I8,   .....+MOI::.  ..
..................,.D=+I....N$,+=.  ,D8:N=$. ,:.Z 8D=..ZM.. ... D=.$7.,:,?I~+:Z?:??=ZI.I,:  ..D=+: ... ..?O,DD.8N,?MMM OO==87$..... 7N+~::  
....... ... .. .   OI~  8M:~DI. .M? ..DO=O.=D. M..N7. ..    . .   =77N .. ,... I~O?:O$=I..DZ~ .. ..... +.   ?O==D 7MNDO.,=?=$ODII. .. ,O$=..
.........  ... . ...   7Z+  ..  I?,? :. ++?.    ..   Z+++, .7  ??+++  . . .. ..  +Z+=   +OD?$ ?Z=..7$=.,. ... .+7D?~?O.,I7$Z$..7?= :.. $7Z: 
.............. . ..,IMN .~=?    .   .   =MII7. 7MM7~    . ,7... , . M.=8 OD.Z, DO ~I .+7.  . :MM? ..  :M.:N:, . .. ~ :  .... ,+  . ~=Z  . ..
....... . . :Z8DN=:,~7O7=:  ....  ..+M..?N=   ZDO+  .O+DMDN8~.7..D.?Z.+O.8= D..+~.=?=~:Z I~.:NI.. ~$M+. .:N7~.? ....  O.Z$:N~..=?. =7I......
.......+,.I7=NZD==8,O+... ..=$DZDZ. ~Z:..I.7+,=D~NNDNN87$8DMM,..ID.77,I: D.8=? 7~,+IN ~,:Z7.,Z+,IMDDO..N, ==== ... +    O?:Z?:M..O,,IO= O...
....... DODMN? .,OIO, = .7$~$+~:M.7. .7  =D$7O7.M~: ,7M= .   : ...  ...   =MO.II,,~?, D~,O=.:D7:+?=. .+.  + 7$ 7MI~  ... ?,IO,$=:$M. O7.$+..
..............=O7+N~:. I=:.7.~~+.::.. .:.OO8$$...++.  ... .. O++MZM8$,+8?..$ :M.... .. . . . ,..... =.7?.OD.$D D.+?.8I+..  I$,$Z=?M~ .+,OD.,
....    .. ....... ..DZI I=IM=. ....$NMMMM.... ~.~::,.. ,+ .: DD~?:D?,IN=~  .........7Z~~=7D?... . .... .=$?~8.D,?O,?8,DDO8 ..$8ZZN87. .$8N~
...::.~D.,MD.  . NN88 .,ZON8,.. :,,:+$D: ..,O ~~NO: .7INZD.I.:8 ,  ,? ,, ., ......,: . ,=~,:. 8::=OI:.. ...D?,,O?:?O:+.+8+=OZ .,$.?,+O~.. Z8
. ,:+D,,=?O~.. .:OO88,~M~. . ID~$M8?$,M...?N?DDN$8DNO8ZO,....:NN+I,.OOMMMO= .$$......Z 8,N:MI~ ..,..  .+=OO    ?D.:: I+,=8,=ZN$.....Z7:MD...
.. .,..88....=O.  ...... .7 :8?DMN....,7OZ7ZD+,7I:.... ~$$:.7~~: ?M$OZ=?.++?,O778D..Z ..   ?....O.O.N..,?. .   ..  .+OII:=$7~D:O:.....:$,?D.
.... I   .. :......   +$DDMZ. ...   ?8II$.I .... .?$8MDZ.I8~,$=. IM$7I:..+OZZO .......=O?.. ....  ..++~,8.N,77 N ....   ,$M?,7NZ=8:....I,I$ 
......... I, .. ~,,=+.=7.  .....$$$, . .. .:MND.D88M+.:.$=:,D.+,,DMN8D., 7..M8+,O?.MMD8? 8,~?DM~.....  . ,ON:M:,7.+ ..?~:,O,M,ZNO,~N.  ... .
.......M. . ...::?N,M8ZM.. $?..Z8M8NM... M7O =~MMZM$=, ZM~ . .=MN . ...... .. . . I==.~I.... =.=.M+M.....=  ..M M. ......,N8..  ..$M.M......
...., . ..~I ZZDO:+?MZ  ..I:$. .:.$Z,.MD$ =~O8ON8=,.$I8 .  :O8=  ..,7 .............  .,   7 :.= N.IZNMM+:. ..~   .  ...7.= ..+I:~$  .OMM,...
. ..   DM$.7D  :=,M.:N?MMM+ ,. .,M:NNI.  M?ONZD,:,Z? .. $.:ND.,M+,.$$: ......... .. :+..........M.$7 7.8Z OMM,N D7 ........M.N8,=? D.+:..D..
.ZM,:8N~.?M  M7MM+ ........M .D..+~N$.8I$~MN ... . MN= Z$=N ~8$,,, . .  ..    .   ......... D ......=I M..DZ OM. $ .M...... .,O.M+ O.M:,D ..
 +.MD~.:Z7=M .  .. ....D,. MI?,++:88MNN. .MM: ,MOZ~? ,?Z:....... ..:$D.IM,$.Z.NN~M  ..Z?...NMO ...+ . .  ..N :M.$?.. +M  ...... M ,D.N:,MO .
.Z8. OMO~  ..., .. ..D..=Z?O$I=Z8O, ....:,.......  .~ ... ..8O=.,,O+,Z+, ,$ 8.~7~:I.8OD? Z,.=~+N8.  8..  ~O..~N.$I, .. .?O, ..... ~::OO,.~  
., 77= ....... ..  .. DIZ8$~$O$ID .?Z$....=:I+IMO...D~.I~ I? 88 .~I  ..~ :. N: ~:+8,D+,M =+ D.M.M.8M:  . .. IZIM7... .. +=77D  .....~=IN8M8.
 77.........Z?I.:~:  ~=7,  $.N,O.~=:.7: .. O:O$.. ?M?$.. .. .   ..........,. . .  7.I=IM.~.,?  :Z.D:,O7.....+ MDM=...?O. Z?.8I M: ... D :$N.
  .......IN? Z7ODO: ~,.,I$8?,,+=OO8$DDM:+..==OZ,.   ........... ....... ZI8OMMM+8+:..7...Z= .~ Z,7D,O +D,8........?7= ?I.?:,Z+.?8M:.....,.,.
......MO=,:$D7 .  88O8$Z,8,,I7N,:?~D87. .:.   .......,,.,,=7Z=~:+?::?$I,  ::DN88Z=.Z:~ ,:8$~DO~. ,?,O.D~?OM....8.. .  , .Z ,78~~M$?ND.......
.. .D7 ,Z8:.  ..N+,~::D.. :Z8+,?ZI. .~....= ... ??, DD~7++8ON?=?::Z77, .. ...  ..$$M?~?+. .,.I..Z?..++Z.O=IM. .. ....    ~.$O$   +OZ7D=.....
.... 7O.....=Z7.,IZD8...~. ..~DO .8=+.:I?N.NMI7N~~,IO7=8O, ..  ..,,,.. N... =Z+ 8~ Z,=:+?  D,...+,,NOZ==.I: .,... $:.~: .......Z. .=8O8+  ..
........  ~M$ ?DO7:...8. .:8,..OZ~~~788N$~7.OO:D:DO. .... ZD $. :: .. ,....  ..I=.,~ I:?,~M:.8:, ...~7,:88..,D..,. .,?8:,. ...:. ,O. :O8O...
....... ,=O.~8?D~ ....  8,  .O~~,~8Z?7,..?7.,N...... .,$N+++ZO7:DMN..  . .... .7~.~.:I,D.++.87 ,.:=O. . :$I,.:.=8?,ZO~..,I:........... 8NO. 
..... .O8DOMD=........:~.~7=.:?O8~:.~..MM?.......,$MOMD$OD7MINM..   . . ...  ..IN.II   ~.8.?~ M.8~ZO7,.  ..: .:D8+,MDN+,.~7. 7Z+.. ...:I7DZ 
.....M,::O. ...... ..? ~ ++Z7O:.. ?DZ  ..+8 . ..+77Z$$8N.77.I?.  ..I7,OO++~ =~,=. , $8, . .. ? .?.. .$OZO ....   +N+ .8,.  ...:I+??  . ,Z7M.
...~M O.  ......D= .O. 7N77?: : . .  Z$:,+ ODOO+ ~:7=,Z ..:8::D,?=  . 7~ ++ ~=.IO~D+78M..~,..... ...7N.  .:D~ .. :...~...O+   .7 IO=, . .IM,
.OZ. ..........,. N,.D+I=?7 I..  +N.?NMII. :NZ,..:. ........      .    .  . ..        .. ~.:..DM:,  .  ::MMMD .M: ..  . .8+ .N~.  $:?=......
.  ........Z=...N~.:=,.=Z... ..O +Z:?ZN8... .. ,+  .....~ZO8D8OM$MMMI,I7.. $. .  .  .?= + ~ 8.N ...ZZM~?Z$+:MID=..ZM?. ..:M+?~ ZN+ ~7OZ ....
.........    .Z. .,$=8.. .$=..,,87Z,. .....$Z= . .,DON+DN8MOOMO        .  7. ~Z,:: :,:,?~. O+ M,D. .. .. .. $8:.I,. . Z8?    ,$,~7.~.  8~,..
..........  D.. OMD... I7 .:NZ+MZ.   .     :.N:.8DMMMD...:MNDDM= .....MMM     O$8=$+..=$O$. Z$~.I.$MDINN, .... M  . ,..~~.M: .+.+.+ON..=8...
.........$,. $M8. .... .+NZ.$,.... .,7. ... :M~,ZDM,  NZIZ~.=Z:M ..  M?,~M,MMN      ....,Z+:  NMM8 M8.+M.+: . ....,N   ... DM, ...?:IM .....
.........  IN=....... 8=. .. ..8NO~~O7NI,:.IMM+ . . .     :...7.=+~M$. ,~..=$~=~+MM88.. D:  .D . ..,~D,MZM 8Z:O.D . .8+  $   DM ..N,I7......
..........O= .  ,MZ$7  ..... .    ZIMO?=M+..  .. $N++ :~$ $7,.. ....... .Z...   .:~DOI:~7D$MI ..8.+MM+..M..7$=~?~~?~?,+N. . +8=O: . 8.:N ...
........$.....8,=?M....  .  ?MI... . .. ...,..~.ND ~$DM.~M~~.., .$ZIDIZ.M~I.:: +O=:. .., O~.7MM... ..$DO~NN+. $$ 8.D O N.87+.8~~OM~ ..:ND...
..... =... ,8$MMMO.~~?. I?=?I~.........: =7.:D=ZO,. .O8:  ...++,OZ=77?MM,+,=N..IDN7O8,     .,= 7.M:O?~   .,.O,  .?,87.=~,I:D.O7.~=.$$ ..D,..
....:.D  MN?Z?8...:.+:O::I. ... :=~::D:.,:,..,..DON?:MDDI..+ .+D7?87DNMMN:::88NI: ,, .~$O8:= . ..N.+,D:~M?   ?. .... .IDZ?8=N~ ..... $...Z  
..   ... =I7M..:NOD?88. .... =$OOO.  .D~:=?   ...,..8N?  .. . ,? ~+:8NZ  .   7M?$M  . :..,.+7O . . + D Z OI$D  ...$$ =.. ZD.$?= ... Z.O. ...
..... .OOO  .II :.D,. ..., $D8DOMO8~.?DM$~.....O8=?.7ZDI,ZO$~+~~7IMI? ,I  ... .$O7I8Z,.IDO,:,ZDN7+  : .,.O.$ 8,MM~... 7,MZ :M+$ND:. .~8D ...
..... D8... .7+ ,....  ?7.?:7+. ..  ,I. .,:O~:8,O,,7,  ....  .7O.ZN$INI .. .....8N7  .  ...  ...,..   . :....7 8.7D:N  .8I+,. MI:Z?...:~N...
..... M ........ ..O78+D=.  ....ON8O,...........,.....  . .. ..=I7,?D I    ..  .. MMO?7O ....., .   .., ,~...   =~7:I=. ...:N:. =ZDM  :=ND  
................~:,,,,,. .  ............... . .. ....... .. ..D$IZMZ.$. ..    .  . Z8~= M~M,...  MM+? .    .......=.,.MZ ..  +OD.. MZ: +DN..
........................................... . ... .......  =II~,:: .~..........  .  . I~7 ........ ~   .: . .  + O+I8.D 7M$... IZ....D? .DD 
..................,???????......  ..........$~I. Z$+ 8MMMMMM ZZMO$M.7..          .....OM, .  ??+=.. ..  . .          .  ID,MMM =O:$,.?? .. .
...........  .  ............ ==..== . =+   ... . .....?O? Z:.:DNZZ ? ................ ~.N8.  , . = .O?   ...  .... ......  .   ?I.ID7 .. ...
.....................  ,, ..     .:::::::~:::. . .,.  :,7~I$Z=:,I ................... .+D8$......  . .. ............,,,,, .....  ?I..D$.....
..........?~ +?,.... ,?+.. ......    .. .. .  .. .... .M$.~M::$M:., ..     ..    ....   .$MM+    ...   , .. . . .   ....7$7$$$$  . .8  .....
.........      ..  ...  .... ...... ..:OOO8O ,...  ,.~8.M7~.,,,M ,............... ..  .. .I,+M . ... ...,...,... .OOO.O~.8,.  .....  .......
..:::. .. .:Z.N.:,,..,........   .  .. .  ....  ,  .DM.Z$+ZNM$N .O......  .....   ....  ...ZNM~:I DDD .,DO  .::=ODNI 8.,O.OD.:Z.IDO ........
.......... ........ ..... . .:~ ~~. ~. ,.=. $O88...Z8=D,:.:I:8,.~. .......... .  .... ......:IO8D...   . ~ .    7.,. .   .. .,$..... .......
..... $ZZD$Z. .  ...  ..   +: =++,.. MMMM+++?MM++,8~Z,.ID8Z$N,..=..........   .............  .MONM M+ +M$.  .ON$.       + .... .      ......
+ . I+  .   .~II.IN?I$ ?IIMM7.:M7?I?IMMMZIMMMDM7MDIMNZD~ ~,?7..I.  ...................  .....  Z?:+MMM.MIII. ,.7II.. I . ..  ., ..    . ....
. ...=MOM? Z,7D88M8,8MM$=MMM+OO.,8DMMDMMDO=8MMMMM8D,:87O+7$Z............  ....  ...............~7Z77MMM+MOMM8MMMMMMZ~ :=~   ==MMN  =..  .~..
M~. .DMMMNNMOM. DM+8,~,NMMMMMMMM8MMMM,.N ..  ,  .=MMNZ ,?MD.  .,MMNNMMNMDM~.~~87D87Z.$,. NIN~.8 .8MI~MMNNMD. . NMI .Z.MMM++MIM8MMIM+7 .M:8..
.  D,+:..?:MMM$:D MDDNN7$$+Z.D+MM .8 $MMN. ,MMMMMZ.. ,MMMMI,:D$ ,MND7:MMMDN.?MMMMMIMM?,$M=7MNMMMI=MMNMMMM8DMDM.NNDM:.  MNN:D,, : .NDNN,8. ..
=.M .O887. , :~?88MMMMMZM8MM7MMMMMMMO~DZMM8888M,M:8NM?MMMMMMMNN8DM...,8MD88MMMMMMDN8~MM8O8888MMM. +M. ~DN ,7NMM+I$MMMMMD8DDM88 =~M7MMM8+MMM8
 .M..  .. .    .  .    . ..?MMNMMMMN?N~MMMMMMMNMMMMMMMMM    ,..,M?MMMM.MDMNMM. NM..O+MZMMM$MMZ MI~MM~MM8?MMMDO.,MMMMM+MMMND8$DMMMMM~..    M:
.....,M::.. .D NMM:.... ...NM. .     ,:,MMMMMMNND  N??O:,:,:DN+DMMMMM::MMM?,MDM$N87MMMMM:=MMMMMMMNMMNMMMNMMMNMMMMMM:::::..  ... .....:.,: ..
.....   ..MZ.7. ......: . .. .   ~8N:.....M=8O8O8=... ...=~~DD~~Z~~~M~=~~  ...  ....=. ..... N..8M8.. ?.8MMM.~OM8. .8NM88 Z..Z8?OD~OMM~..OM8
..:ZO+D?. .Z$8?$ZI  ..,+.:M:  Z7OZ . ........  . . . ...  .....++~,...:++ =+. .+$M+ .?++ ?ZMD~+7ZZ8+. .$O$ZZ  .$DZZ+..Z . ,ZDOZ+............
..................M$.......   ... .?MI7=  .I$7...$M7DIZ. 7,87I7M...7MI 7I .7.+................  . .  .8?. ..... ............  ,~..8 .7M.....
Z~ ,DI . ~7=O$.........++M ...8..   ...... ............ ........ .. := .=.~+ .. .. ,.. .=....  ..,.:7=++OZN7..+NO ..........,,     .. ......
.... .... ........... .  ...:...,: ::: ...8DDO+8~+N~~ ~~. ~~...... .  ,  .  .  . :,  .   .~8:,::. .. .   .  ......  .=Z8D~+=:~~,. . .~... ..
..............................................    .... . ..    ..  ... ...... ....D:..:,.,: ....  . .....:D8:$:. ..  ... .  . ... ~~   .  : 
.......................=~= ..?Z=,,~.N8O,OOO=,,?= .  ......~+$:$$O,,O. .,, .....,,  .,.. ,. ....?I.++$ ...  ..,+=ZZ= , .++ ..=N~. =..:, . ...
..:D8,88Z88O. .O88=..  .. .......  . ....... .O$. ~8ODDZO:~ .  ..,8..888D::DDD8O:........:D:....... =,.::.........   .   . .. ..    .. . ...
........... ....... ..=M$+D8O8D=88OOOO.. .,.   . ...  :,  . ,...:., ,Z, :    .      ... .. .. ..  ..   ..,Z,ZN 7  ,OM,,~. . NZ,,ZNO$OO8,,...
........ .,Z. ..  ......................... .. ,+.. .......... ....  . ... .... $M??MM$+????=... $8ZN.:. .. .  . . ..... .. ................
.......  ....:77  .............    ......................+ .IM7IMMM77...IOZ?MM,.. ...   ? ....I . .... ...I ..~,.7I :.. ...............?.   
.....................  : ...  ?8.OMMMN....  .=M=.  .. .  ..............   .............    . ...  ........  =O8+=ZM+O~ ..  =O.===?.. 7... .,
........... ..:DM:D.. . .N .  ............ ..... ..   DD  .. ....  IM  ,.......  ......? DI.~DDD ,Z:MI.~... .... ....... .. ................
..   .. ... .  .........,   ,.....,.N78................ IM=..~?... . . .  . .8MMMM$.. . ........... ....... .    .. .......  .  .  .........
""")

page96_art = ("""


................................................ D8MMMMMMMMMZMMMMD:DD.., ...............................................
................................. ..... .......~MMMMMMMM7:MNMDIMMMMMMM8DMDDDDDD~........................................
........................... ..... ..... .. ..,MMMM7+8MIM8O?M8$OMMMMZMM+MMM=M8$M7 ,8.....................................
.......................... .   .. ..   .  ..MMMMMMMMM.:IMM+ZM:? MMM$MMNMM+M$MM    ..$ ..................................
........ ..................         .   ..NMMMMMO,.MMM7.MMNOMMMMMM~8M7MD8N7M~DMMM8=MZ7:..... ...........................
.............. ...........      .        ?MMIMMMM7N$MOM$8MMMMM?ZMM$MZMMN?MM~MM.7~~+  D8Z.. .............................
..........................      . .. .MMDNMMMMZMMMMMM,:MM?MMIM=MN=MM.MMMMM~MMM8$MO=8..  D. .............................
..........................      .. =D:.8ZM8MMMNMMMNMMMM$MMM78D~MMMM.8N+OM$ZMNIMMM~. .... :,.............................
....... ..  ...................,DI:$$~=DMMMO~MN,NMMMOMM$7NMMMO~MMD~7MMDMIDD7DMMMMD......: .,. ......... ................
.........    ............. . ~M7O....:..MMMMMZ=MM~M7NMMD7MDMM:~MMM MMMMMMM,MMNMNMM.DM::II+8N...... .....................
......... .. ...............M  .. ..  ..MM:MM8M,D MMOMDMMMM:M~.MM::MMMM~$DMMMMMMMMMDO:?$+NO$7 ..........................
......  ..................~=OO... .. .. MMMDIMMNZM= MN+MMMMDMD.MM MM7=MMZ~MOMMMMMMMMZ~MDD8N$DD..........................
.......  .   .............I=:8~,~.O,,= 8D+MM$D.D=MMMMNMZMMMDMM.M8 MMMMMMMMMMMNMMMMMM~ .,:::IMM.......... ...............
....... .    ........... M$M?ZD?=~ :~:+NMMIM8MMNZ , 8MMMMMMM+M78O+MMMMMMMIMMM7OM+MD $......, MM.........................
..  ... ..   ...........M.,.M:,7MO:=,I~MMMMM +NNMMMMMMMMMMMMMMM ODMNZMM+NMM,MMMMN+M=... ... ..M ........................
.. ....  .   ......... M . I~D,OIZ:~+=7DMMMMMMM.8M?MMMIMM?MMM$M$MDMMMM7$MMMIM?MM8MM .........  ?=.......................
..................... ?,....8.I=8DZ7=$:DMMM~8MDMMI,OM8MM$MMMMMMMMMMMMMD$=?M7M?MDMZM = ...........D .....................
............. .......=M ... ,M M $D ..:Z MMMMMN, MMMM?MMMMM=MM MMNMMMMMMMMMMMMN7M=MM.=............,.....................
.................... O+O~ ..=.+.8:...... ?M=DM?MMOMMMMMMM$8~MM:MM=MMMMO8O$+~DOMMO8MMM.=...........  N ..................
....................78=:7,. ..:O7MM.,  .,.MDMMO88:DO++MMNMM MMMM8.DMN8DMMMMM=ZO?MMM+ O.=............ ?. ................
...................MD?D,7D? ...7MMMOMMM8MMMMM,DMMMMMMMDMMMM.=NM~M.NMMMMMMMMMMMM$MMMN  D7  ............Z.................
...................$8 8+OMO?8O8ZM7M7MIDMMIMMDMN,MMMMM7?IMO~~ DDMD.MMMN~I~$.8MOMM$OMM ..N+..............:................
..................  88:OZMMMZ7NZMM==:  .:OZMMMMM$MMM$MMMM NM$D. .8OMM$MMMM8MDOZMN8MZMM7ON.:.............:,+++=7MMMZ7 ...
................ I.      ...  ++ZZ   ........$NNMMM8MMMM$ ZZZZZZIMM7MMMMMMMMM8M...Z+ .. MM,8.............:..........I...
............... O~ ... . . .   ............ +,.IIMMMMMMM:........7$8MMOMOMMZMM. ..  ....+78N I........... 8 .........N..
............8DMM  ..........................  :=$NDI8M~MMN.......:~MMMMMMMMM~  ..:~ .... .8ZM$.O.......... ~......... M 
......... O~MO..8Z?..... .. ,?MMZ?MM8$$$$$$MMM:  788Z 7 .~~.....M+: ... .ZI.,~, ...........MI~ON ? .........+..........M
......... M7?. MM++:.:ZZZM=DN.. +IZZ.. =    .MD..   =....+..... .O8  ..... ?M? ............=88OONI.:.........M..........
......... .8M8 MMMM.,M.,NN:MMMN,...... ,NMMNN~. MMN+...?.:M8M. .==DM MM ...7,. N ...........I..,+8MM:.........: .......,
...........D ,:........OM=DMMM,.88=OODD=  D+M 8O8N.   ...,...DNND  NM,. .=8N=..$ ........... ....~O?N8 ........?........
..........M.................  M7 .MMZN..  .8M:7.7NM,IO,, ..........,,8I,8DN$N:. ............. ... ..~+8M ...... ,$......
........ Z ...................:7 .   . ....Z$8, ?N~OM?NMM ...8..,:,MMMO$M,   ............... Z.....INZMN ........ =.....
.......I,.....................,7.Z..........= I,:=D+$8DONO7..+87=.IZN :... ..................~Z......+,7..........  ....
......$............ ..........D8.M......... ID ..,.:~M.$.  ...................................~~.....OM............N....
......MNMMM7O8MMO====...?O88M8M7.M..........M:. . :I:  ...................................... ZI.... N............. 7...
... .8  .    .............. ..$ .$......... . +....=$ ..  ... .   . ... ....................   ,D ..,? .............8I77
....I        ............,$=?N,  M.........:+.D~O88=:,,::,    ..   ::,,... Z:$Z+.....~~OOZZ7,..D...==,.. ........... N..
.. ,.. ..    ..............M7MD  +.......,$D. = ..?O...... IZZ:~.......... .........   . ..,. .    .M...,Z,......... D..
. I ..       ............~I8$7N  O...,..$ .:MD. . .+............................................Z...Z..7MO$,...:, ~.MN..
.:....      ............$MO+N=8I,MN=I. DNM~, ...................................................=. $.. M?8$=.. M. ~.7D..
......       ......... ~,M$8D,,,+$MO,~:~:. ......................................................~MM..D. ~ZD...I ~ = ,..
......       ....... ....=IO8~.:=O ..   ........+.................................................+? O .. ID . I.M +. ..
... ..       ....................................................................................~.........M .O .,., ...
......        .................................N.................................................. .......+M  D M=, ....
......       .................................  ..................................................$.......+M..~.O.......
......       .............................................................................................$N.M.I........
......    .. ......................................................................................:......$M M..........
......       ...................................................................................... ...... .: ..........
... ...      ...........................................................................................................
......        . .....   ....  ............. ................... .......... .................. ..........................
 
""")




page98_art = ("""

...........................................................................................................................   . ...........M
...........................................................................................................................................M
...........................................................................................................................................M
...........................................................................................................................................M
...........................................................................................................................................M
........................................................................................................................... ...... ........M
......................................................... .............................................................. ..................M
.................................................. $7MI?I,...?I$7 $$$$N?I?Z....................................................... ...... .M
...................................INNN+....+N$+. . .~.D8I?MN+~   ,ZD, :$NZM=:MMMZ?,,.ZO=...++:N$M+ .~++:......................... ........M
....    .:::.. ....:::DZZ8::::ZN+,..:~DZ::... ..7NN:::IDDO:...... ::ZD::DM+::,::::::..    :I8:.  :I::7NMO==+MDDO8O::~:=8:   ....  . .  ::,:M
.. ~.M+:.,,+ZZ++.. ......... =OON.=+N.Z$M+++.....  ...... ++MNZ .. ZM====...Z... ... +OD$M8D?8OOMMZ+++,.. ......... .77ZI.I7..,.$ZM+~ .....M
.....  IZ7~. 77I? II  MI.I I$N7,. .. .+.~   .+O$ =Z$ZZ   ..IZ7.  .INZ?88$ ...... ...  7D7 . M7   . .7..7: ..... ? .. ... I ..,M . . . .. ..M
......... . $OZDM$$$~.,.......?$$.,.. .. . ..  . .............. .  . . Z+ :,..: +?.+~: +. ..$?~.OMZ8++ZZO?Z$$,$$I,$?.?O?7 7I+. . O=7D7O=?OOM
............. ..~8DM8..I$D,=~N,~N=~7DI......,.+?~,., =~, ..  . ...8. .. ,.,IZ+,ID+,DI,+DI:ZDOO,:?8~D8I,  .~Z~:..,.:Z+:Z=,I++.$D7IO,,8:7,O8ZM
............... ..,$=,.==ZONO,~?OONZ+===.====DM~,IIN=.I.D,=?I,I :, :.O$. ,..$~,:N+~N8.:8OON=~: :?  . .7?,,.7+,....   =~Z, Z.:O:.:8DDO,=O$8IM
............      .~~:8NMDZZ8?DZ:,  DN~::::.O=D~ ,:8D: .  =7 D,:ON: ZZ,+O~?+DDDD8Z8D~+?=, .. ..+.:++.   O$:8  .... ~ ,: .I8DD=.,Z.I~MDDD8D8M
.. .++++=...   ...,.,Z$=?,.I~,~$:,+$=.+8 ZO87,?I.+OM$7+=+=+=I?+ ,.,,$:..:.O .7 +.   =.=.ZN.N=+ ...  $,,.+NN~ ... =?,O.?O8+  .?Z,   .. :..  M
...........I    ?.:$+. $7M?II. MI7MM77I77,.=+.7. .    . :..  . . .   ... ,,D ?Z.N:7MZID  .   .....=.$7   ..=:....  ? .8I$~:. ?  =7MO =O? 78M
.......~.$~=+ 8Z?=N$=+?.+  =.... .=.+~.................   . .....?$D7~+,O?~??.D.?~.M ..... . :8D$ ....   ,..... ? ...?,, ....$: I+... $$?ONM
........+~,7~O++.N7, ..............................,.~:MZ==D=~I,O=.7~~,.:  Z., ...... .,+,$IDZ$ ......7.,,.. .+MO ..=M.~N $?....  ,..+.,I:DM
.....  Z7,:: .. .................................,. Z:.$.. :  . +. .  ...............        ..........M?ZM.MMMDDZ+~M8M8.+88MM.7.:?..::....M
........=I  .............. . .....................................................................777..NMMMMMM,IMM.DMMMMM77DZ,?=.N~:O~~~77 M
...............   ..   ~MM,   ........... ......................................................... IDMMMMMMMMMMMZMMMM?=M...Z M::I N7 ?MMMZM
.........   .~ ,D $I7Z ,Z,,D777MI7$INIIIIII77I ... ............................................... NMMMMMMMMMMNZMMMMM8MMMMM  D$.MIMID: I:..M
.......~ :7., =7 ++.O+?M$ ..77   .........  . ..?   $$M?ZZ?~8= + .............................. =8MZ8+MMMMMMMNMMMMMMMMN,MMN$7+ :M$$? $O.ZOZM
....... . .I= ZD8I: =... O..~=.~=.~ :................  ..=,.O+~ ,N 7.8. .,?....,..,....:..~,.8:887MMMMMMMMMMIMM7MMMMMMMMMM8 ND,D:.$:.N:.I7.M
.........,IM~,. ..:,Z?~~~...: .Z.$.8+:~: Z.+..~.O.,,.......  , ,:+OO:,+DD8~+8.$D.Z+.Z..8.I8,7Z,7N::M=NDDM,MMMMMMM.MMMMMM7MMMD.~8,:D.~N.~OI.M
......7? : .7O:................,.+,N.~ D $ O,==:O 8 O $+?I$ $.  ..  .~77M$$D..=~.8~IMI?O :~.ZN+7M$MMMMMM7,MMMM7MDMMMMM.MMMMNM:II,+I =$.....M
.......,................................... .. +.?~~ =~I~~+ 8.I ,O7.  . .,,~. ZMM.,  = ~:?.+ Z .DDZ: 7M.~MMOOIM.$M$MZO..:M,   .. . ..=O. ..M
............................................................... . ..     O7~.....=  DM:: .ZM.  .... DN.: .=MM:.. M :MM...+8 ...............M
......... .. .  ................................................................ D,,. D. .,8I,... .8D,.  M:M.  .N  : M,:DDMDDNNNDZ .  .   .M
........ ~+7~?,: D~O.=~,~,~~~Z.D 7.~ ~ . .  . . ...................................ON.M7~. ..=.?ZDMM  :~MMM~8Z..:    N .. . .... ..... ..8ZM
........... .I.N:?,=,+::$::~ D,Z.8,$ 8:+~:$.7,II78,O, . ............................. I~D,D=D8:..7$D::MMDMMD.~D~8.ZZ,::~Z.O. .:,:.,I . .. .M
............. .... +.+M....I N , :  ,~ ..,+ ~ ~ .. .  .................................    .+.+8NZO$+DMN.O ,?M$7,.+I ?:=:.Z 8:O.8 I 8 7I.Z.M
...........Z? ...+.? . =.. =   = I. , ,...? ......... +.,~,~ ++? I D.8.7.Z.I.$$:D?. ........ .77M8.OMOMM~8?O~+ 7.,O7M~.I I 8.7 = I:=,?I.N=~M
............  N::.~,~: :8~,,,~ ~.I.Z ?.D,,+.:Z7,7 +.:.D,D:::DN+:.=.~,O.D.O,Z:,M,8I,DI .. 7.I, ?Z. ,MM .:,8:Z~  O M~. =:NN:O..+.$.+ Z I,.I,+M
..............7.8.N Z N.=:,.:.,D.N.M M Z :.I7,N.M.Z.MMMMNNNNMOM:.,,..8DNMNMMMNMI:$.N+IZ,$. M.DMM,IMM........ D:N.N.M.$D,.. .MMD I~$..+ ...7M
.................?OOO~==========NOO7.===: ..................  .. . ...=NOOOMO.,OMMMM   .:$.ZNO=7M$M ............ ~.I,O:+8+$, ?:.+==O8 $I,$.M
.............. .,,.,,,:$7  8DDDD,,. .:+8,ZNZ,:... ..     .........::NND: MM,.. , 7D:......:$M+NMM~D+: , ........................ D8,.I.DNNDM
.......  .   :...  . ...I Z.,O.:=Z, .  ,= =Z:8MZ 7.?.+.OZ...=D+,$. .... NM.,?DO=+M O=~I 8? M?+DM=.Z 8D.=D,.  ........................   +?ZM
........+.7+,$?+.$O,=Z I+:Z Z.+.$$.I 8.  =~ ~M.M I=O M?=Z?,8. .Z? +:D=$$MMO7$: 8M:+I?D=IN8M7OMO M+??  .7N 7 8.7,=  . ......................M
......: . ,,.D,, .+ M.MM~:D=:.DDMI:?.N M$DMMMM,MMZ =I.D++N.N8 $   8,M?:N.NM8,~MMMIM: MM.IMMMMM$MDN?8 I:M:..D,,N.=:.O Z.O:I+. . ............M
......=.Z M.O 7 N.MMMMMM+MM.:MMMM?MMMMMM,NMMM+MM.N$:M.??MZM?,NM 8MM MMMMMMNM,~MMMM..MMI.MMMMM8MMM.MMDMM:ZMM~MNMM.D.O MMDM7.O.D.M. .  . ....M
..... .II ?7Z?? DMNMMMMMMM=DOMMMMMMMMMMMMMMMMMMZON:MMNMMMMMMM?78MMOMMMMMMMMMOMMMMOMM ,8MMDMMMMMIMZN8MMMMMMO:INDDM.MM8M MODMM=:: $.OI~=78.N.M
....8OI=ZMIZM~IMM8DZMMMMMMMMMMMMMMMOMMMMMMMMMMMZ8OIMMMMMMMMMMMM?MMDMMMZM,MMMMMMMMMIMDII7:~MMMMMMMIOMMMMMMMM7DMMMMM8IMMMNMM$MMMM7OIMID~~I 7+M
. ..  ,$MMMMMMMMMMMMMMMMMMMMMMDZ8MMMMMMMMMMMM~NZMNM~MMMMMMMMMMMMMMMMMM~=MMN?MMMMMN  7. .M ..  M$8?$MMMD88MMMM=MD=MMMMMMMMMMMMMM,.$ 7~:MO~7~M
..+$$$NMMMM8.MMMN8M7MMMMM$MM$$MMM7MMMMMZMMMM7MM  $MMMZ+MMDNMMNMMMMMMMNM$MMZ+ NMM,.O..Z$I.  ..IO?MO77.. IM..NMMMMMMMMMMMMMMMM~ 7O  I     N +M
..:MMNMMM?M7MIMMMMMMMMMMMMMMMMNMMMMMMI,MZMMMM~:,?, ~MMMMNDMMMMDMMMMMMMMNMMDMM~M+MNMM. MM.MD.  :... M..O:Z+~M   NMMMMMMMMMMMDMNM MMIZ I: . DM
. ..7MMMMMMMDMMMMMMMMMMMMMMM~MMMM=MMMM,. .=M?.$  +.M?MMMMMMM=8M MMMNMMMMNMMMMMMMDMMMMM?M7. .M .M..7M.7MMMMN . ~MMMMMMMMMMMMMMMMIM ZM $.M+,=M
.+.=Z.=,IN.MMMMMN~MN~8M . . O~ .M~D=MMIM:M IN+7D,...D .D:.ZM7M.D8M?N MN=M MM~MMM8MMMMMMM:Z, ?8888DD8MMMMMMMMMM    MMMMMMMMM$MMMZOMMMMMDMDDNM
..$...I~?  . 8 ?M~.M..M.Z7D...I..?M  M.M .7 .:.. .....,D..I.8..M 7..M, D M,MI.M I77MOD7MMMN... . .I$D7MMMMMMMMMMMMMMMMMMMMMIINMMMMMMMMMIZMOM
......M+ ~ . N  =O.    ,= ..... O.   ?.. .......... ,.. O........=:.   7.=. .. ..M:MI  MZ.?M8M8$M~$8MMMMMNMD~=MMM8DMMMO88NMMM8M$MMMMM?MN:.8M
..... ...... ,N   ....  ..8 ..Z. ..................  ..  ......,,  ,...D .......  $. .. I .M,. .8.NON7N,MN D?MMMMMMMMM+MNMNO.,MMNDNMMMM+NMMM
...........I., ....~, .~. . : .  ..................., ........  :~ ..$......... ......  M7. OMO 8.. ..+.MDDM,MDMD~M=MMMMMMM. OD ... MMMMMM7M
........ 8... ...M . O . N,  M  .......................... .  .~.  ... ..................MM M~M M M.MM. M.MMMMMMMM$DNMZ.  MMMMM. M  .?MMMMMM
............. 7  ..D, .Z,  =................+. I......... . $  ..O...... , ........... .+M8M+M M8MM+....?N:Z:DDD==7. OMM,?:,  MM,?MMM:MMMM?M
............I .. ~.,.$ . ............. .. ?.......+......+..O 8,.. ..  ? I.....   ..8D.M=$M MMMMM8........ :.7D .NO,N 8 + $MMNNMMMMMM8 Z.$DM
..........+.. ........~, ....+, .... M =DIM O. ....  Z, 8N. MMD.8   ,:.+. .. =.  ~MMMMM8O=IMMMM+N7?.==  ZO   MM.MM..,.8.. I=MMMMMMMMMMMMMMMM
..... ,,,,,,MNDDDDDDDNDDDDDDNN,,,..M?NMMMMNI.,M,.,,=NN+NNMNMOD,N~M=8.Z... , .N .NNMMMMMOMOMMMMIN  ... ,,.....MMO~8:O8,  MD:, ~MMMMMMMMMMMMNM
....... ..........  ..     Z88I. .  ~MMMMMMMM8N?   $8O8MNMMMIO$M?M8M8~O  =M88MODMNN8NMMMMM8MMM ......  8.788OMMMMMMMMM~...M87NMIMMMMMMNMMNNM
........ 7.. =:7,=I Z. :8$ .: .:. ,.,+:O ...  =$$8 .OM=MMMMMMMMMMMMMIMDMMMMMMMM$M =MM?M8+:MIN= ? . . .,,  . OMMNMMMN++D7 +NMOMMMMMMMMMMMMMMM
........+.8.Z 87.O,,Z M I.N  $ 7.?,I7?.O.,+ ...+.$  .$$M+MMMMMMMM$MMIO.,MMNNMM,M,M$$$.  .8. ~?IM$MM:Z7MMM$MN~MMMMMMM?NMMMMNMMMM8MMM$M.MMMMMM
......  .. . .   ..  , .  ??+$Z, ,.+$$.8.? ?+==:8 $I  .??ZZ+IMMMON$ZMMMMMMMMMMMMMOMMM.?:=I~~ZMIO ZM?N+,:Z$N78N:MMNMMM. MM NMMMMMMMMMMMMMMMOM
..............................    .ZMZD?.8.+~$$.N:~8,~O:~8=?.O+=ZZ?+ZZMMMMMMMMMMMMMM$ O$ $,+8MMDMMMMZ8ZZNOZ,  7..Z..   = DZ:OM.  .. ZZMM~ MM
......... ,.8.  ..$: Z.=,D.N~D?~D O.$MD8DN8I,,8MNI:MI:N:~O=7ND~++:M:::~MNNN8ODDDD:D,?,,$. :.8...:, ..............  . .. ...   . ,8I. .... ,M
........,:I,M.N.D:?O:.~8.8 I.=OM8MI~~~Z.I.., ,.,....+..O.N....................................................... . ~,~~.,. ~M88? . ,... ..M
........ =.,Z. :N M ?8 ~:+.... ....................................................................................................... OMO.M
......+.   , ....................................................................................  . ..  .   .  ...........................M
............................................................................... .  ..,,=7:ONNNNNN.=:Z.=.=. .=D..,............~ ............M
...................................................... . ..... .  ,.,OZI.=:...  .    ..  . .   ..     .,,,,:O:8IO,.,+~,. . .~. O :   ... ..M
....................................... .. ,.~,?.?~.D:.,+D=?Z=~O:.    ..................  .~$N?D~:7 8 O $.:::,~+.D.::.8.8.+,$:.I..I:8?8MNM:M
............................ :,Z,,,.8.=:D.8.=+ $.7I,I +.~NZ=DZ?................ ..+8M~N.~ $ N D $.?..7,~.O.7.7 .+ 7.,, ~.$ 8..D ? O .$.~.? M
............................ .:7 O.D Z:=D : Z.O+~8?.=.?~ +7,,$Z ........... ZI~= 8=+=~?.~  ~+ .: O 7.I $,. :,.D. + D,7 Z.+..+, =.+.D D..= 7M
...................................:.O,+=I:.I 8=:8+.O?:. MMMI...........I7  M +~,I ? +.I O 7 I.Z.==D..,.I,I.=..I 7...::.+.:?.8 7.,==+ Z $ $M
...............................    .  .  $.O~=:8D$O,,,..................=  ,+.D::=,~.~. ,7 ?.~..$:I 7 ~.:  :.=. Z 7.7 I  ? :..,.+.I I,~~,? M
.................   .......+.Z = 8,D.7~~ . ...................... ......  Z, :D $,, $,?= ,:,~.I.N... ..= .  ~.O.O. .Z..~..: I., ..,~.,.D I,M
...........=  ~. . ...       .........................$$7$Z?????.?.~... ..... ?=I .  ~:.I.$.+. ~.7 ... .: ...?,:  ~ . , ..?  +,~.$.=.~.?= .M
........ ...   ... .. .  .............. ..  8 .........................:.......... .~ ...I , ~.,. ,. .O  . ~ O . . .Z... : . $.., 7 .. ~ ~ M
........ ..   . ......... ..7$?.,I .=. .  .............................................. . :~... +.  ......   + =.., 8 Z = ::.$...=?.. . ..M
........ ...    .  ?.  . .  ...................................................................  .I .=$I . .       .  : .. :IMIM.   . .....M
............ N., .  .............................................................................. ......... .,  . ..   .., .. ............M
........ ... ,~N:, .     ... .................................................................................. ...7 . .. . ...............M
........      ..   ...,.. +  +....................................  . .  .  . ..  . ...   ..   .   ....................,. ,..  ............M
........      .    ..  .. .. ........................... .....=I+:$$7$.........   . . ..  . ..$7$$$: ?,?,. ... . .......... .I  . .........M
............... .. ... ........................    ~+8IZ    ....................... .... ~ .O.... . ~ .  .    ..Z.OI+  ..  ................M
........ .. ..     .. .      .......... ... .$ I  ..............................................  ..... 7 . ....,....   :7I7 . ............M
........ ......    .. .      .... .. +D$.  ............................................................... +........M. ... .:..,$M+ .......M
........ ..     .....    ...  :. ::  ............................................................................... ...., . ...+  .   .:..M
........      .    ..  .. :7?.. . ~..................................................................................~ ..... ,=  .   .... +M
........ ..    .     . I   ......................................................................................................  ... .. :M
........ ...  .  .. ..  .    .................................................................................................. ...?.~O..=.M
........ ..   . .7D~,,    ................................................................................................. ...M..+ .N ...,M
........    ... .. .. .   .. .................................................................................................. ....... =..M
........ .. ... .. ....      .......................................................................................... ........D.. .  ? ..M
............  ................................................................................................,........+...... .... ,.. O..M
................   ..  .. ........................................................................................I,. . ......  ..8.. .....M
........ ..   ..   .. ... ...................................................................... ?+.......  .........   ..7 ...+...........M
.................. ....   .. .................................................................... ... .... . ..............................M
........ ...   ... ...... .....................................................,Z ......... ....., ..:........~ .......,...................M
........ ...... .......   .. ..................................................  .7....M .. ............. .......   .......................M
.........  ............  .............................................,,..... ..... ..........  .: ........................................M
.........  .  . .. .. ... ...................................................+....=.......... = .. ........................................M
........   .  ..   ..     ..................................   ......... .........................  .......................................M
........ ..   ..     .   .   ...............................,...=. .... ...................................................................M
........... ... .. ....  .................................... ? ...........................................................................M
........ .....     ..        ...................... .. ::..................................................................................M
........           .. .   .. ......................,?......................................................................................M
........ .. ... .. ..    .  ................. .............................................................................................M
........ ..   .... ....      ..............................................................................................................M
                                                                                                                             
""")





page104_art = ("""

 ...........  ..     ..   ...........................................................................................   ....  ..  ...    ..M
.....................................................................................................................  .............. ... .M
.........  ........  ..  ...................................................................................................   .  .........M
.................. ........................................................................................................................M
........   .....     ...........................................................................................................  ... .....M
..  .......   .   .  ..  ..................................................................................................................M
...........................................................................................................................................M
..  .................................................................................................................... ..................M
...........................................................................................................................................M
.........  ........  ......................................................................................................................M
..  .... ..... ....  ..  ..................................................................................................................M
..................... ....  ........................................ ....................................................  ................M
.....   .  .....  ....      .................................... 7NMN7D.........................................................   ....  ..M
. .. ...... ....  ....      ...................................8NM?NI.MMMO,................................................................M
....... ..................................................... =MMZNNMM?MMNMM  .............................................................M
.    ...    .. .  .         ................................. +MN7MIMMMMM8MMM....................................... .......  .....   .  ..M
.... ...   .....  ...  ..   ................................ 8$MMM . NMMMMMM7..............................................................M
. ......    ....         .  ................................:DMMMN Z..+M~?MMM..............................................................M
.    ...........  ...     ..................................MDMZD:8M~.. .=+M+ .......................................  . ...... ...  ......M
. ......       .  .         .......................... ..  .MMNMN8DM  ,:7+$M .......................................    .  .  .... .. .   .M
..     ..   .. .  .  .      ...........................?~,,:MI8DMD.$..DMMOM.................................................... ...  ......M
.    ....   .. .  .  .   ............................ :.Z+8MM?8.=M ..$MDMMO.............................................   .......... .....M
.    ....   .. .  ...       ......................... =+ O,~IMZ?8= .,MNNDM,..$................................................. ...........M
..  .   ........  .... ..............................Z8.. MMM7=+ON. +M$N.,MD   ............................................................M
.    ....      .  ...       ........................?M $ ~ZM.?M?,M,ON.O.~ :MN :.............................................  . ...........M
       .   ... .  ... .   .........................Z+M.8.+.M=+M$OM..M.MMZ  M7,.I ...................................... ....  .........  ..M
.   .  ..   .........    .  ................... :.7:O.$$ $.MIZMD8M,. .MOZ  MNN.:................................................  .........M
.    ....   .. ....  .   .  ...................:,:=7=?MO ,O ?$M .  .ZM+~O.M.Z8N .D  ........................................... ...  ..  ..M
.              .  ...       .................. : NII $D. .  D7M....MMMI.  ,:+..M .$ .................................    ......   .....  ..M
.      .... .......  .........................Z.MZ+..M7 .,.,MDMMMMMMMM+ 7MZ=MDI.I..$  .....................................................M
.      .   ...    ...     ..................~, +=8...MI  O  M?MMM?IMMMZ.ODNND7~D. 8.$., ........................................  .   .....M
..  .      .  ..            ................Z, +~M= Z$+? 8  7.MMMMMMMM87O8M$., =O.?8.?,: ............................    ...... .. ........M
.   .       ....  .  .......................O,.+~:O DD:..:.+Z$:ZMMMM8OZOIOOMI8 ND$.MZ 8....................................................M
.      . ...                ................ . M ,N:I8:8~~.MMM ..MDMM.=M ZZMOD8MMM I:N.+ ..............................  ...  . ...........M
.      .    .. .            ................ ,8Z:,.:,$8ZM,+M$$... M~8 + ~NO=NN~MMM?+N.,.....................................  ..  .........M
. ..     .. .......... ...  ............... O8M=:I.Z $M8+MIM.$..$MI.O  ~778M M.IMM.ZM=8. ..................................................M
.      .       .            ............... ZMMM?N+?$,Z:   M.? ..MM+D.,? ZON,DI .,$M~~, .............................  . ...  ..     ......M
    ,OOOOOOOOOOOOO8MO8OOON8ONDNNN.$NMZ?M~====MMDOI=MI~O:, ..:   .MMN .  ~O8M=D....NID8           ..............  ....... ..................M
..     ..   .. .   OOOOOOOODD8.,.M?.  $8::NDDD,:=O8:M+8.,~?D?N:?...OOOO :ND: :.?,M,I .........~..:::,::::,::::,I=::::::::::::::::::::::::::M
....   . ..    .     .      . ?.M,Z .........~ IM,7Z7=:D.~  .ND+........ZD7:+~D: M.M................ ,       ~7 8+ ..:   ..................M
.      .       .            ...M.:.............+N7=. O Z ...OZ8..........7I::M...$$ ...........................~ OO..=.. ...   .       .. .M
..  . .......................+M,:               .   ..+D....O++ . ....  . M7:~...?M........................... .D..M   +.......   .........M
..    ..      .      .    ...M==........ .     . ...  .M ...M$.       .  .ZM+N... M,.           ,7777~:7II77~7777778MMZMMMMMMDMMMMMMMMMMMD M
  .    ..   .. .  ....   .   M::...................... M ...N7 ...........NZ,? ...M ...............................IM:                    .M
+I.,,$.,,I,,,,,,.Z~ZI.IZZZZZZMZZ.,,,,,,,???????????????M ...MMM?~????:??:~DN?$... $??:=,.=,.....,+++:. ,.     ,   .DM  . +++++?+++++++++:..M
=8.$+M,??+I 7$8M.MDM$ 8?OMI? 78~I,+~MM:+ 7778MMM:N.7IO8M ...?M? + ??~I?MZ7N,:I ...ZI +I?8$.??,M.I?+$M=I?=M7ZM,M7I?.M.???+M.??.O,7I.M,$7$M:$M
.. . M,,. 7.  ,M?,.$M8. .D+..7?~ .D78..= 8..O8., M7+  ZM ...?MO$= M =,+ .7D:Z~D...$?D ..OZN . IZ...8I~  ~7N..M8$..,MD  .8I?..ZO:  ~DM .+$8.M
., ~.ZMZ .8?,. ,.7 .8.. .= , Z+$? +8M..M$=. $Z Z.~IN .OM ...?$M D.8 =,~.  Z.$:M...$.....8Z= .8M ...I+ ..IM ..N :. O7D  .?: ..$ .. M... ~I,.M
..M. +N..  ., .=,. .OI   ~:  7.M..:=.  I $  :? . ~?I. D$ ...?7.+8O8 ?..  $.$::M...$..=, Z8   8I  .=.. . NI.. .,  Z8?. .O?.  88.. =Z  .Z .~~M
,....,...~N :,M. +MN  .MN..8D7 ?MMN  NM7... . . ,Z...:=7 ...?$=$+. ,M .IM.MOO,M...$..=MD...=N ..8M8  ..N...,Z.,=M+...:D.. :? .  D .. N.  .,M
.   . ..       .     .         +I      .....    ..  .. 7 ... ?Z. .........MM.,N..  $.=8                    .  . M                         .M
.7MMOZMZOOOOOOOZOOZOO OOOZZ,  . ZZOOZ~OZZZZZZOZZZZZZMM:MM . $MZ .MM8MM8...+ZZN...  8O=?    .+++++8OOOOOOZZOOZODDMOMMM?$M8OOOOOOMZOMMMMMMM7 M
......... ,~ ...  ....   .  ::: 7N......  ..   ..  .MO,DM .MMMMMNMMDMMMMM.=DIN.....$ =,...Z8DDDDO . , ~~I:NMM.M:  D8DD+ ??.:~~IM?M       . M
.      ...   ... ... .. .   . .$.M.N... .  ...  ....IO $ .MMMMMMMMMMMMMMM. 8MM ... $... ...........  . .... , M:M..........  ..   .  ......M
.   .  .       .            ...$.D =............... +O 7.NMMMMMMMMMMMMMMM$ ..M.... $... ......................M:8 ...    ...  ....   ......M
           :.7NDDD  ...  .     . M N     ... .....  ?8.,.MMMMMMMDMMM+~MMM7  MN ... $,.:8MMDNNNND    .         M~  ..               .      .M
.      .     ~~~~..~~~~~~D==~~~~MMZM~MMM8MDM8NMMMMNMMMMM8MMMMNMMMMDM=MMMMM..MM...? MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN8888D88888ONO8MNMMM
.   .  .   .   .  ..... .:  .............,..... ,.... ~.MMMMMMM?MMM:MMMMMMM +:~,.M.$......... .Z  .....................  M ..$ .  ..... 7 .M
       .    ..        .8.   ............ Z.......M ..M~$NMMMMMMMM,MM8MMMMMMMM: $N.$M .=, .....7......................   =.. .+          7..M
.... ... ............ .. .............. I .......:  D8D7MMMMMMMMMMI8MM8M87MMMD. .O$M?..8 .....N ....................... ,.....=........ 7..M
. .. ...   ... .      7  .  ...........?.........:~.  8.+. ?MMMMMM788MMMMMMMM$  ,  M$: 8 .... :........................$......8........ . .M
.   .       ..       7.     .........   .........:....~ N .$MMMMMMMMMMMMMMMM$NZDI..D:::: ....+ ...................... .  ..   O.        = .M
..     .... .. .  . :..  .  ..........Z .........:....OI.MO$MMMMOM$MMMMMZM77:$7M7$M~: O ,............................ =  .....O ...........M
.      ..   ....  ..+.    .......................~ ... ..~M?7ZNMOIMNMMM87MDN.,I8MM8:~+ 8 ............................ . ....  . ...........M
.      .       .   $..      .....................:....... M= .N8MMMMMM$D8~8+ ,:  M? +=,~ ...........................    ....  .8   ... ....M
.      .       .            .....................D.........$Z ND++.IMMM=O.O  .:  $?..,O .... .............................. ....I, ........M
.   .  .      .   D         .............................. M...  I?ZMMMM=MMD..DOID=  .......=..........................    .   : ..  . .. .M
..   ......    .  .         ..............................8.~  +=.~?MMMDMOO,O+:~,M~+.O..... ............................ ..... ~..N .......M
. ...  ....   ..            ...............................=DZI8OMD8MMMMM +..... M ? =.....=.................................. ~  .$ ......M
.              .            .............................. :.I$:,.8ODMMZMIO ,D8I:+.?.,...............................   .  .   N   ?..... .M
.      . ..    .            ..............................  .Z ...:8MM7MN7NMOO=I=,M. D......................................... ... N......M
.   ....   .....  .         ++++ +,,++,+: +=, +++++++?? . $.7.= :.=8M,MMMM~.~~.7ZMM.?=. ......... .... ..+++,++=+,7+   8=ZOZ    .  .Z......M
                   :NMZ8.MN,=.M.MN.MMM8+NNNOMM8N8MMMMM8M..+ I MONODZNM8ZMI=:. . ..$$:.7 ........N 8MDN8N$NMDNM?.=ZO7::?O..DM+MM8NM,MNN,D  .M
. ..   . ...   .   7?MOD MM,~.M MN MMMDZ$Z7:MZ.Z:MMMN8DM.8.:. =?Z .  ..7M..: .. =,7M.~, ....... N.MM78+O$$M==.I:N O7::+..7M7++ZDDDOMN$M. ..M
.................. Z?M.O.M?,= M M8.MMMDM$Z7:MZ,Z:MM$MOZM =.N ..?..  ..,?M?+M =.I8O?M,=Z........ ..DM78+M$MM==,I:=,Z7=:+. IM7+?O8NDZMN$M. ..M
..................=$+M O$M+...M MN.MDMDZ$Z7:M.,Z=MM$M$Z$,= M.? = ..::NZIMM,:NDON~N$N?+8. ...... . OM.8+M$MM==,?.D$$N?++8 7D7+?O8NDZMN7$. ..M
..................=$MMIO7M+ : I~M8ZM7MDO$Z7:D,.Z~DZ$M,O$,~...? M: I8$NMZ7 .  ....,: $D$ ........ 8ZM.=+N:NMO=,?:D$Z$I?+O :=7:?OD+=ZM.:$I...M
..................=$DMON=M.,~ Z$MNM8MMDZDZ7:NZ.ZMDI8M=OM.=. .? M=M8,....     ...?Z+D:,$,?....... 8?M.=MM..MN..Z~O MM:+,M.  8 M=D ~ M, D8 ..M
..................=7MMZNMM+,~ M$MNM+~MD$$O7,8::ZMMM$+~Z$,=. .. M.  .  778...MO8I=NMM.$~=D  ....$.8 N7 MM7 N, ..=,.M7N+?M...M...M...MNMM8 ..M
..................=$.        .=+. .  D~::~~~~~~~~~MMMMMM.=.  . M.8.=8ND?.,?NOZ~I=D7 ,7 +:?.....$.8MMMM888, ~$D88D8MDMD88.... ..  ZD88MM8 ..M
..................=M.. . .=+=+++OMMMMMMMM8++  .,~,+==.=~. . ...M+.N8O.,:+N~..   DZD.+I:?N. ....$.8+==++++? =,+:...  MMM+$O:+ZM8M++=+++OO...M
..................~M$777$$7$7.   .=77M7IMMMMMMMMMMMMI. .. . ...M7M8.  . ....ZDM..M8.O?:.?~.+...+.8I??III ...     ...M$II8II :::8N$$777ZN...M
..................=$+.MNOMM, MO?$M+MM?MM8,7M+..M+ M$.M8~, . .I M?   ..$ODOZDDZ7MMM$+~7.7? I ...+.8=~M$8M.IMN=NM~OZ.7M~+ ZM,.M.=DM:++M?$I ..M
..................:$? MD8MM,.MO?.M?DM+MM?Z7M+..M~ MZ M$I?.Z. ? M. =ON=+IZ=~Z.O .. +MZ=,Z:.D ...+.8+~7ZMM.IMN=MM~8. 7M + ZM,.M =,M:~+MI$M ..M
..................=$? MNODM,.MO?.M?NM$MD?Z7M+++M~ MZ ?DMM.Z.NN.MZDZ?~,77M?=~ ......MMN.O.7+....,.8+~7ZMM.?MNN+$:8. 7M,+ ZM: M =:M:=+:?$M...M
..................~$? MN88M. O.?.N+ZMM8+IZ7M++MM~ M. =DZM.M.?:,7?.=O8M$.8,........ $.?D ~D.Z?..+.8+~7ZZM$IMNNNN=8. 7M:+ ZI:.M =:M:=.~?$D...M
..................=$. MO DO .O,?.N+ZMNM+M=+D:+MM~ M. ~D7M.M ... :$:. ??...........$...:78 I=,~  .8:~IZZO$IZNNN?~N ,7M:+ MI,.M.=:M:=.IZ$M$..M
...................$. MO.DZ .M=? M+8MMM~M .D::MND D,.=D7M M.... O.....................:M?.? +$...8.~7,ZO$I.NN=,~M..7M:~ MI:.M.=:M:=.M8M=$..M
...................$. MZ.DZ .M=?.M.7MMM M =DO.+MD.M. =~$N.+ ...~=.....................  MZ,.+:+. 8O~7, O$+.NDDD~M =:D:, N :.M.=ZM:=.M$M~M..M
..................Z$. M..NN..M=..M.ZMMZ M ?ND 8I8 MZ.~~$M +....Z ........................ZD:7,,Z.8O~$8.O$ .NZ I~M .,D:. 8 :.M =OM:=.MDM ? .M
..................=$.I8..DM..M== M..MM,.$  8D M+D M= =~$N +....:+. .......,...............8N? I:.8O~7D.O$..ZZ..~M ,7O:+ ?.:.M.+OM:~ N$MO ..M
..................O$.7O+.DM..MM: M..MM: Z. ID  +D M+.M~$N.=....Z, ....DZZZ~ Z ........... .ONI+:M8MI7O O$ .ND.7.M .+=++ ? :.M.=ZM:N N$M8 ..M
..................+$.IO .DM .MM..M .MM: D . D ,+D8M+ZMM+M . ..~D .......II:MM,7..............8 ZZNDMDN.O$. NN ~ O   .=  ? : M  IM:?.M.M. ..M
...................$.IO .DN .MM..M .MM~ $ .88, +M8M?OMMIN ...I~......... $,D:M:  ...........I $M.8++NM.OZ .$N ..M.,I.~  ? . N. ~M:I N.M. ..M
...................$.7O.7DZ..MM..N. DMD Z..D8$N+DMM+?MNIM .M.I: ....... $ M=O+Z7...............Z.~:=7M.,M..NN.  M.,+.:  ? . Z  ~M:$.N,M. ..M
...................?.IO,ODZ8 MM..M  8MD $..$DZ,++M:??MNMNI .?  ......... NO,8,+.N ..............MM$~7N.DM:.OD...M. :.:~.?.=.Z. ~M~Z.N$M. ..M
.................. $.MO,.DZ8.MM..N$.8M8 8,.DDZ,:MM,.8?I?. ,M8=M.......:.8.8I Z.8.M  ............MM?I.Z.IM .ZN$..M.. .:~ 8 7=Z  ~M:, N$M. ..M
.................~.$O7Z=8D+8 MM..NM?8M8 M. D8$MMMMOZ.........  ....... ZM~.7I?   ..8I  .........MM:~M.+=M  ZNM..MZ...:+ I D=$~ ~M:,.D$M. ..M
.................~ ?MDO~8D.8DM7? NMI8MOZM.7D8ZMDMMDMO.................M 8 M . ........O$8......., N~MM.=M ,ON?..OZ...:+ ?.D7D=.~M:..N$M. ..M
.................: .MMO=MN.8MM=?,NMN8MNZ?.MNNMMMDMMMM~..............IM . . ........... Z8Z ......?.M$8M M .MN=?.M$  .:+~I.D7M: :M:O,M7M~ ..M
................... MOD==N DMM=?=NOZ8MMZ?.MDMZMMNMMO8D  ...........NM,Z...............  7.,+.....+,~7NO7~..MN,.:M..=.:+M?.D78+ ~M:ZZM.M8...M
...................7M7?~MM.NMM7?$NMO8MMZ?.IMMI?MDDMMZN .........D M=.Z~...............O.$.. ......~~8DM.M7+M$, :M ~7.:$NM Z7M+ :M:8MM=M8 ..M
...................7DMMOMMMMMMMMMMMMMMMMMMMMMD+=MMDMOM.  .. ,=M~M+Z+ = :..............~:.ZD ......$.DOM=I,MMMMMMMMMMMMMMMMMMMMMMMMMMMMM8 ..M
...................$MMDDDD7......DD8DN=MMMMMMZ8N=MMNMM .N$.:MMDI,8  ..$ .............. :.Z~.......  .~O= M8:?8DDD8DNM~~~::8NN+DMMMNM8D?8 ..M
...................$N8D88       ,.  .?DNNMMNDMDN~DMMI~,DMDO8.:D: ,N.7  ............... M ND ........ =+N77.N~ .Z8NN,DND,$,. . ... ,,,,?M ..M
...................MDDDD8D8DD8D8DD8D8ND8MIOM~NMIMD$NMM?MOMO~...I: =....................D. D......... .ZMZ.: ~:.~.   D:,ZD+887O8888NNMZ?....M
...................NM.8:=:+ 8I~?.N., MM+DMIIOMMDMMMMMM?O .Z...........................,.. NO..........=.M M.O M=OMN.MM, ,MD.+? ~N:8ZN ?....M
................... . .== + 8. .., , MM+ZM$+DINMMM7MZMDO .  ........... ............. 8.:.~=.......... =M,M.O M:OMZ.MM~..MD.++ ~,:OZN ?....M
............................ ....... 7N+ +MNMNMMMMDNON:.,   ......................... M 8 .Z7  ........MO,M=~:MMM7MNDN:M.M8.+. ,,.Z.N ?I ..M
...................................... .= MMM8MMM.~DZ8..~ ...........................Z. :  =  O=....... ZMMMNN~MM8?MMMZO:.. , .   ..N. ....M
........................................= ZMMMMM,87.=,............................... ,8 ? .M..........O~..   MN+MDOMD  ...........  ......M
.....................................  ..$..,M, .7 .~.................................8 .+...: .....  O. ....MM. MM.88 ....................M
................................................. 7....................................:I.D ..8.  .,MM=  .I..MIZM~.........................M
...................................................................................... I: .?....:Z: ..:$?M?DDMMN,~.O ......................M
...................................................  ....................................$.... ..D. . $$MZMZ?M.:M.   ......................M
...............................................................................................M .IMMN:M8I7M:.?7 ..........................M
....................................................................  ............................ MOM8 MM. 8.+ ...........................M
............................................................................................. .,..,M+MM:..N + .............................M

""")



page105_art = ("""


.......................... . ...... ..... ....... .  . ............... +.........   ..  ...........................     .     ..         . M
...................... I+..:O?Z:...7...:O .......8N$8MON ............. O. .... ..,..................................:.. .D?.  :~  ...ZD    M
...................... Z,..$8~, ...~ ..~M...... =8NZIN8$O~............ :+: ..  OO7................................ :=   .$=,...:. ~  8D..  M
...................... ?...,? ~ ...Z...+Z ..  .?O=+78DI8ZI  ..... .~....~.,..ZM78Z.....................   .........,I ...+:,...$. N  OO... M
.......................:Z ... O....8 ..87... . ..,,D8D7$$NM .....  $ZMN,:MND,:N7D ....................I8N .........87.  .:~:..:7+  ..$.  . M
...................... 78 ...,,....D...=$ ......  MZOD? .. ........=?:+7$I,.+:OOO...................,=IM...........~Z ...:I:..:$7O..?.:... M
...................... $8... O.....7....M+ ......,$8ON8I ............ D+.::,?~Z88 ........=N,..... =,I:. ......... OD  ..:~?  . :O  .7,  . M
...................... DD....$.....~...,D8....... .OZZZM............ .7?+$D?=7D?D8  ..... .OODMO.$O$IM............ ,:. .. D8  .$?O+..?:    M
...................... 8D ..I?.....:....7Z ......... :. ............ =OO?N$,M:O+DN7,....... $OZOMOON$. ........... ~+~. ..N8   I$?7..?:..  M
...................... ?$ .=OI, ...I...:7$................   .  ... D.OONZZM=+ .........  . 7~$$ZMZIN?.   ........ ?M. . .M8..:8DO   ?~    M
...................... +.  :8ON8...Z....I~ .............. :8ND8 ...M+ ZIMMOZO=...........,I+.~ 7IMO+DZO?N8 ........$$   . N$..?D8....8Z..  M
.......................? ....8Z? ..D... +,..... 7......  +~N~. ....   ...DDO= ............. +, 7MMIM=$IN...........: =   .8~  Z7..Z..OO    M
...................... 7O ....D ...:M.. MN..... MNN  MI.O.~............. IN,+ ........... ,,8:.?M:M$O,.  ......... .I+ ...8 ..~7..7=.ZO    M
.......................78... M= ...:Z....8...... NN,DMM~=Z. ..............M. ............. .:=:+NNOZ+............. .I?   .N     .., .7.  . M
..  ...................I?....O..O .,... ZM........Z?O8D+NN  ................................,DO+?NNM?$............ .$O   ND.         ,.  . M
..  .................. ?. .. ?.$N . O.. 7N........D$D8IZ$MOMM:.............................. 8,M.,MZ.. .............7.  .~8.    MZ.  ?     M
.......................I, ..M..7... N   IM .......,I~,,.ZI?$?=+...............DZ.............M,O....................7.  .~O.  ZNN .  ?~  . M
...................... :8 .$Z. . ..,=.. I~........,+:D?:=7$+$D ........ ......M. ............ . ...........  ..... .I.   ~M.  +I.~I. ?:  . M
...................... 78 :$+.D=.. .~. ..?..     +O7ZZZ8OI+77I?~ ......+N... I ... ...M........    .N.... .,..... .=+  ...Z, D$M+.:  $~..  M
................  .... 8D ..=.I Z.  7.. .7       DI  8I$: ?=I$I77       ?I  8? :.. ?78.  ......$...:7 . ,7.N  ... .:.: ..,I. .$+7+ . O,... M
............... ...... D8 ..$= :8   Z.. ZN.       .   .. .  ... ....... .+?O8~.,8Z7O..  .   ...:ZZ.N~.7=$~M    . . ..~   $8   ..~II =O ..  M
...................... ?Z ..~..8I . D . $M+.     .       ....   .... 7 .,OZ7$. 77I .  ..       ?7?I$I7+M=MMM$MMN$+..:=...ID .77 ?+= ~$.... M
.................. ....?~   . .?~  .7. .II.      .          ........ M$ID=+Z+,7?=    ... .. .  .:.$?D?ZMMDMMMMMMMMMM$=. .DD. .  8$= :$.    M
.......................:,,  ...7   .~...I~.      .       ...........  DZ=.+D~I=DO+$MO... ....  ,?M8DMMMMMMMMMMMIMMMMMMZ..Z8....7=7. ,~:... M
...................... IZ....  ~~...+:  ,: .   ..   . .:O ..    .    ..I:,?8$7::7Z7, .  .    .D7ZD$MDMOMMMMMMNMMM$DMMMM=.$8...?~? . ,?:... M
...................... ,87... ,Z7 .. ~ .,~.    ... .=D+$$ .. .........Z?.,8+?~ ~.   ..  ....8O==8+MMMMMMMI=NMMMMMMMOMMMM.ON  ~88. ...:...  M
.......................:Z?....,Z? . .=.  8=    I$=  ?8:O~ ..... .  ...7=.~OND7. ......   .. . .7~MMNMMMDMMMMMMMMMOMMMMMMZI7, ..~ . . ?:..  M
................  .... .,=   .N$:    = .=M~     +~,O7,+,+O,    ..  . .I ..Z$+=.  ... .   ..  .N,MMMMMMMMMMMMMMMMMMM8MMMMMMM,77N8O=~ ~M.    M
...................... .?    ++O .. .O .7= .   .=7MD~~I~Z?NI$.. .    $....MO, ...    ...       .M?MMM~MMMMMNMMMMMMMM$NOMM7MM7~=ZI~~.:7,    M
....................... +=   7..$,. ,$,.7$..   ..7$OI$+,=Z~ZND. ...... ...+?........ .  .      NMN..$ .MMMMMMMMMMMMMMMM?M?MMM:.=ZO7.DZ,..  M
.......................,8Z. DO..:7:..M .7$Z... .. N+7N7,: ~7~M:............... ..... .  .....  ~M .   .....,MMMMMMMMMMMMZDMMMN.~=NM.Z?...  M
.................. .... ?I.,, ..~8O .7..7?M   . Z8Z,$$+I7O    ...  .....  ...........=,... =Z$ ~MM ........?ZNN:MMNMMMMMMNMMMN ?=~~.8+...  M
........................~I NM.  $O+..$  $=M:M,MMM: .=.?7D?=  .......  ........    ...I+.. 7O8   N8.   ... MD ...~,NMMMMMMMMMMN ,+8 .Z? ..  M
................  ..... :+ +I  . :. +$~MMM7MMMMMMMMM:=I=+$M,.....  ..............:.~ I+MMZ?. ...=.M   ,MM.N:.8.. ..M7MMMMMMMMM  $=.,MI...  M
........................,, M7. .    ?MMZM=MMM7MMM?=7MM$..MM$ .. ....  .....    ?+=.=8I++?NIM   . MMM M. N:  N .. . MMMMMMMMMMMD MM..N?.... M
....................... 8Z ,O+NN7  DM~NMM,DMMMNMMMMMMMM  .:: .. ........  .  .  ::~88ZD8NZDM8D...,MZD? +MM$M  ...  $MMMMMMMMMMMM =M.NM ... M
.................. .....O+  .MD?M.MM.MMMIMM?=M,MMMM$8MMM ...... .   .... M.  ..  ..Z8MN=Z$M8Z= .  MMO? .,,N, ......+MMMMMMM. M,?MMM MM.  . M
....................... ~= .. .. MMMMNNMMD$MDMM:M~NMMMMMMD  .......... ID7 ....... $87?Z=DI~,... .O..D ..=.,. .... MMMMMM:+:.,.     . ..8D.M
............... ........,I   $:.ZM~MM8MMOMMMM8N MMMMI+MMMM.......  . .DO,..... ...$8=Z$7I?ZI:..   O I~    N.MZ$7..7MMMMM,:7...M??=....N7MMNM
........................?? ..Z$.MMNMMMMM8MMNIMMMM$7...MMMM....... .D:M+I  .......I7?D??D ... . $? :=.MIMNMMMMMMM NMMMM~M7.....  ...MI8..+N:M
........................DD. :M=DMMMMMM7MMMOMMMMM= .   $MM8...~? ...+O?D.......... ..7I~ ... 8.,=. . MMMMMMM7,MMMMMMMMM. ... ..  Z8D.$.,M.:MM
............... ....... +N. I?+ZMMNM8MMMM8D,~..~Z, .O87Z,    .,~Z?Z,I8:D., ... ......:. ...:NZ:8~8,.MMMN8$N. :MMMMMMM+I....  .87?+,......~:M
................  ....  =?.~:I MMMM8MMMM.O  .~.:. :?88N .   . .?~8:O$,D=ZOD8 .   ....   ...DM. ..MN7MMMM+7M8+MMMMMMMM Z ...:OO+Z ..... ....M
....................... ~I  .O MMMMM8N,N.  ..M~M+:M?MMM.  .....=O.~O+Z=O..7,: O7.... ....  D:$....88.MMMMMMMMMMMMMMM D ..?ZD,$....   . ... M
................  ... . ~= ...,,MMMD.       .IDM7. 7,.7, ,..   D+8M87OI+. .. ..:$:      ...D= .... ?.?MMMMMMMMMMMMMM..,D.D~O. . ...  . ... M
....................... .~ .I.  ON7D8  .   ....    ...7,8O~ .,8 .$+77ZIZO .... O8OI. .... I :..=. .. OMMMMMMMMMMMMMM8=+ND.    ..$ .  ..  . M
....................... =~I 7? $MMMM... ...   ...MMZ+.MMMO....... +D~ ........ =?=7O77....7$ . =... ..7MZMMMMMM8MMMMM.. ...... . O.O   ... M
............... ....... ?DI 7MMMMMMMM   ..         7N ZMMOI.......I=.. ....... +=.~D7D8DMD N M. O..   .MMMMMMMMMMMI    ..   ..   ,~.$. ... M
................  ...... MO .MMMMMMM=...D .    .$? ~7MOM~:7M$...... .......... I+,778D7. N. .:, M...  ..MMMMDMM$MMI .+............+,O.+.   M
................  ..... ~7M MMN$ON8DMO.  :O .  ...$+ MMMODI~$M,.........8:... .D+?I7IOO+ +... M + .....  MMMMMMMMM?=7  ..   ..  .. .8? =.  M
.............. ........ ~MMMM7I8 $788IM+. . DI.....7$. III.~ ,+,.......O$O .... .,MM$O8MD= ... ? I     ..+7MMMMMMMMMM.........  .....$,.:  M
........................7MMM=8D7:... ..$MM?+M8MM$, ... Z   OD77,,   . :::7: .. MM MNNMMMM? ....:.M..   ...MMMMMMMMIZ=   ... .........Z8... M
...................... ?7+    :DN   =,.   =Z ?MDO8NDDNMDDI:$N,?MI. +,.NMMMMM..M.DMMNMM7ZM.......~ ~....... NMMMMMM:+....... ..  ..... ~N ~ M
.......:+DMZ . ...... +7MN:D, . MD8~~::NM:,.=Z8D,~DD8NMMN:,7Z: :8M.?DMMMMMMMMNN?M,7O    +....... .M,. .... ~MMMMM7?$ ...... ..  ......O,=: M
.....:=MMN~Z88$MD,...M+$~Z?$N:N$OM8:,$8?.:,?8$$,,O8NONMMMO   ...+.N=MMMNMIMMOMDOMM$   .+ ...... ...Z8 ....  OMMMMN~  .. .   ..  .. ....ZZ.DM
....,:?MMZ?~... +D,IM=$...:.7??MMO~=....+=:... ....  =MM7$, .. .77.N: ..MMMMMMZ8M,.. ..O ..........?O ..... ,MMM .  .N+MZ..  .. ...  ..Z.:MM
....8MDMMM ..      I:7~ . ...MMMMIZ. ...   ....  .  . IMM+:8D$MN?M7Z    ?=MMMDM7MM...78..   ....  ... .   .. MM .MI... +$,.?D.  . .. .. .,,M
....DDMNMI..... +OMD8=88?=N$+M?M8,,..  O?::IN.,+NZ,+~~ZNNO+MMD8=?I=I. .. IMMMNO8+=    M.... ......8 ~$.     .~.:O  .D~M .~.. D8,~N?.,~=8=NMM
....MOMM . ..... M?NMMMMMM:MDMMMMMZ: ~Z++ :$ :7N?..=:.MMM87MMZ7M+?M8.  . 7~?7M +7 ..OM ..  . ...  N? M      .Z8.O+~8:M...MMN8?    :O.~?O$.+M
..  MMN7N...... IM7. .II+ =MIMMMZM ,+Z7O I8=.ODD+I.~:IMMM$~M7 IZ.~,M.I=  .+,MM OD .. O..   . .....Z+ 7 ..  .O.Z7$ .:~. I$M7? . ~~I .M :....M
.. OMMM ........,D... ... .OM8MDDI~ON7=  .   ... . . $=ZMM~.   ..~M.?..   NMM+.?~ ..~   ....... ..O+ ...... 8?N. ..N.~N::..:  N:$ . ?N,, . M
.. MNMD ........N..........=DMM$N   ... ...  .. .    ?MMMN. 8  ..8M.....  $N+IMM ...8    ...... ..,M   ....8. ....7DI,7..~N .8+  =,,Z.=M.  M
..=MMN:........$...... D.. O::MM:N?DON:?7.::+IOO78DNM,.  ,8....  .~, .....$NNMMZ . ~ .  ........ ,,$ .....M. .......,  . +DM,N....7   8,=  M
,~ .ZM........ I......~ .~MN?IMMMMM+OMOD?:+,.DNNOM:..   I.= .... 8.........MMM , . M ........... O=.O....I............. . ..~. . ~.~ .=,8  M
....NM........D........ MZ ....++MMM+++++IMMMM7.         8$ =  .ZM+ Z......MM8Z, .I+.   ........ N=.7... $.     . ..... .   +:. $ I8...OO  M
....ND........M..........NMMMM::::::::,   . ..   .       ...,... ..O....  .MIMM...I:.   ..........N.    I   .:...... ....    M +$.,:$. NO  M
..  ?8........$.   ..........   ........       ....  .  . ..O88OD.Z .......,MNM.. M............ =.O?... M.O8 M... .. ....... .$ZM. OM. MZ  M
....+ ........M..............   .......        ...    .. ...   ,ZM.........,MNM   $...  ....... O..O....Z=MMN8.. ... ...... ...=.O  8= N.. M
...O,. .......8,..............  ..........    .77I77,  ..... . 7?. ... .....MM ..,+..II. . .... O,,$. .7M.IIDM+77... ...... ...?I.. ~Z N.. M
...O:   ....   .$M??: ....... ..   ++NMMZMMMNI ........$NMMMMM8 ...     ..$.MM ..I.DM?+ .N+  ..,.M $.N+MMM$Z$ZM~M.$.   .    ..~.?  ..DZ.   M
...O, ............ .. ,,,,.+,,,,,. ..   . MMM. ...   .   . . .$..  .  ..  NDIM ..M .    78.Z+..D.MMN+++MMM88=,,,=D:MM  . .. .. I7 ....M8O=~M
...O:  .....  .............$.....   .......M~ .....   .......  +.8= .. .  MN N...N   .  ..?:ON..=.~O..7MMMMMMMMMMMN. ...   ....? O   .,D~:OM
...O: .........   .... $$O8...      ....   .~ ....        .....M.  .  ....MM N ,+N....  .. D,O$.M,.=,D.   .ZZO,,.M. ... +ZZZ+. ..D.....$.?.M
....+ ...............~?8Z8. .       .  .   Z.  ...           8 D~ ..  ....I,,N  :... .   ...O.DOOM. 8 I   .  ..N.I....7.D888ZN8N.D.... .. 8M
... O,......   ..........M...   .  ....   .Z   ..       .....D,.,.. .... .NMMN..M    ... ...:.~?O~ ..IM....   ?~M  M=,7,......DI.= ......N.M
.. .ND ......+?  ..  . . O.. .       .,.   Z     .          .M:.8  ...   +M$IN.~N:,  .   .. :8 ~:  . ZM....   M M .8DM: ......:.?~ ......, M
OMMMNI. .~II7+  .7MII$DI$ ...   .      +   8...      .    ...I..O  . .IM$. IMN  ,I. $~. .   OM ~Z  . $M . .   M M M~I  ..... ..$M=       : M
OMMMOO   ~IZZ.    7OMZZ:M ...          M  .M..            .. ~ 7=MO, M  . 8.. ,DD M$+ ?=...  M..M...=ZI       M OZ~8MMMMMMMOZZO.8OZNOZZMZZZM
MM .   . .....    M  .. M ...       .  .,. M             .  :.. OO. .  .  .... IM. O..M::8MMMM=~D.. O,        D. 7M .  .D=:. =+.? .N .D,...M
 ..  ............ ..... M....           M. M              ..D  .:$  .. . ..??IMM7M7 .7IIIDMM7MM~. ?.MD   .   . 7.MM    OD ..7,DZ. ~. . ... M
................  .. ...NZ...           +..Z..   .          M. .~NMMNOO ==8MDNO .$..    ..==MDMIO,.?   ...   . 8..M  ~,~.....D I$    . ... M
.................. :... M+...    ....    N.7.....      ,,MMN.:,,MDD.M..7 . :+. $. ....  MMN+M.MIIM:7  ....     ., I$.M .... M DI..M .. .I  M
......: ~. ..... MMM? NMM+ .. .. ....   .:..~. ..MMM. MMM.  .    . .... ..+ .Z... ..    O. 8M M~.MM$Z..   ...   M..M . ....OZM.  ...ZM=~+MMM
. .NNNMMM:NNMM,,   . DMI.+ ...  .   .  .  NMM, NNMN :: .     .....  ... N .8.. ...... ..M  .:. :  D+.$   ..  .  .$ .MNMM..M~M MM$=M=.Z8NMD~M
DNMMN=.  . . OO~= .....?.M...  ... .OM~ +8Z~   .I..:. 8DMZ=ZO$.   =.  8 . ... .  .  . I~8=N~.M .M ZO.    .       ,. M=IMMM$NM,IDNMI.O7+~::DM
  M .?M .  ............M +  . 7MI.?NMI.O~     I  ?.MZM$OMMMM$MI7 ...= .,I.. 77M:~IMMZM~MMO=  :.   ..8.           .O M$MMMMM,M,.7MDI  I ... M
   .............  .....Z  NM, NN:..,.+~.   .+..= . Z:MDDNNNM::MD8..ODNM7= 7:M8,MMDMM8   ,MNMMMN,  + .. ..         M $M?$+. =. ...Z ......  M
 D.. .......... ... .ZM+~Z$M:.  . ..~..   O., .   .$ M......8DIM8M?M$OM MNI  MMM+?MMMD  .. ....,N :  D ...      . 7.$.Z,.7.....=  .... ... M
.. .$M77I      . 7M.+MM=.O  ..  .?:.   .~ .:.. ..,I$ M .  ..~MMM+$M~OM:=NMOMM7  ,,Z7~8MMIMMMMMMMM  Z.~ ...   ...  8.O$Z.....  8........... M
...     ..   +D:=OZ.:,.=, ..=. ~: .. .7.:7  +M$D.DIM+M:    ZDD,.ZZZMD$.O.  . .....$ZI$7?8ZI=IMMZ7M.~ .+...       .? ? ? ... 7......  ..... M
.. . .... ?8.IO.. ~:.  .. I, Z      ..~NZO ,$MN8.   N    =D?M .~.NM N~. ...  7 .I... :..:  O7$8:: 8 .,. ... . ?O+..7........  ............ M
.......~Z.8:  ..:: I,.. =:.+:    .ZN7=O:NMNM8MM..  788D8DD:  ,  .:8MM~.   .:,.~   ..$.   .I.    .. D:..Z    ..,Z.,N. ....... ............. M
.. ..N+$+... .,,.?... = .::..   ~.NM. ++OZMZOMMMIMMMZOOZODMMMMMMMMNMIZ$   I .?....+..   ?. .       I 7? .++=,..$M. ....   ................ M
.  M.N  ... +=.?. . ?. O.  +  .MM7Z. 8MMM?8 ....~,,M.~=7=~MONONMDI  .  .7. $ ..   ..     ..     ...$MM=..IMM7MMDM ODI...I+?7 .  .......... M
,D N......,~ ~,...:~.:::87D$,MMM8.NMN=. ?: ... ... ,O.. .?.. . . .. .. ,  ?...    ..     ..  ...8 ?.DIN88888888MMMIM?NZNNMZ,.~D.. ........ M
:Z .....:  . .. I: :8N ?:M+$7M:.Z.  .             ,.  .I .  ,.         .$.   ..               ..  M8MMMMMMMMMMMMMMD~+,Z7MIMMZ. .=........  M
Z..... ?.... .~:.=7 7N78.ZMD8. .   .             I.  ..   .......     ~=..... ....... .. ... I.  .II$O=77I7Z:?DDZOZ777III..I777..........  M
......,.... D,.=: ?+.. ZMI  .                 .$ .           .. .... ? ........  ...     ...:.. ...   .D.     ... ..  . .................. M
.... .... ?, ,.+:MMOO~$ . ...               .7.  .      . .. ... ..I,.    .... .......  ....   .     ,. ...  .  ..  .................. ... M
....... ? ... .ZD8MM= .......              $   ..        ....  ...8... .  .  .    ..     ..  ..    .Z..           .. ......... ....... ..  M
..... O ......... ..  ... ...            :     ..           ....7  .      .  ..   .. ... ...      ..  .....          ...... .............. M
....,. .........  ...........      .   .+ .      .   .       ..,....    ...  .       .   ..  ..  ~    .   .       ........................ M
...................... .......       .O                      .. ...... ....  .....   .   ....  .7. .     ..  .   ... ..................... M
..............................         .   .              ..    .       ...    ..    .                   . ...    .. ....................  M
............... ..............   .. ....          ... ... .. ..............  ..  ........  .       .   ....  .      ........... .......... M
............... .............                                ..................  .... ..... ... ...    ...    ............................ M
...............   ...........          .  .               .. ......... ....... .. ..     .........     .. .  .................. .......... M
...............    ..........                            .      ...     ...  .   ... .                              ...................... M
""")


page107_art = ("""


....................................... ................................................................................................. ..
.....................................................................................................................................  ...  
................   ...... ..................................................................................................................
..................   ..  ................................................................................................................ ..
...................... .......  ............................................................................................................
.................................   .         .   .  .   .         ..............    ....... ...      .... ..........  ..   ....  ..........
    .    .. ... ................ ..           .   .      .       .......  .   ....   .  ... ...........  . ...  . ..... ... ....  ..........
 .  ....... ............. ...... ..               .                .   .  ........   .  .  .....   ....... ............     ... ............
     ..............  .............. .      ....  .   .   .   .......   ... ......... ....  .   ...  ............. ...  ..  .  ....... .  ...
  ............................  .                        .       .....  ...  .....  ..  ...  ..     ...  . ...... ...  ..     ..............
..  ....    .. .........................   ................................  ...............................................................
. ...  . .....  ......................................  ............,8Z.   OD8~............. .. ...   ................. ........  ..........
     ... ..... ........................... ....... ...   ... ......M$7ZMMMMMMMMMN.... ............. ................... ....................
  ............ ....... ..............  ... ....... .............~MMI  7MMZMMM7?NNM7 .........  ....   ...  ...... ...  .....  ..  ..........
...................  . ................... ....  . ...  ..  .  7,~IMMMNMMMMMMMM=8MNM~..............   .  .   .  . ...   ....  ..  ........  
. ......   .... ............................................. OM8:D7,?MMMN$MMMM:$7DMMI...  .... ... ...  .....  ............... ............
. .................... ..............      ........  .   .   MZ8=,Z.?M8M+IM8M=+M?MMMM+, ......................  .........  .   .............
. ...... ..     ............................................=D,D?DMNDMZOMM~:?MMNDDMMMMM.............  .... .................................
..  ... ....................................  ..............M+D$D+. ~O78.N  =~OM?Z~.MMM$ ...... ..............  ....... ... ................
. ............ ....  ....... ........  ........  . ........+?MMI.MMMM $?...  .,,..MM,M~M~...   ...    .  . ...  . ...   .  .  .........  ...
    .... ..... ........................ .......  .....  ...MON:NM?M~:,8....,,....=,DMMMMO... .......  .    .................  ..............
         ..       ..................... .. ........  .    M8??MMMM+.M?? ..  ??$.  Z$M.MMO... .. ..  ...   .  .    ...  ..  ... .............
       .        ............ ..................  ........ MM88$MO   +~, .. $MMD  .  MMMMM..........   .  ........ .......  .................
       .        ......................................   MM$M:MM .M MM.O ~~?M,.M. .=8MMMM  ..  .....  .  .....  .........  .................
    ...  ..     ...  . ............ .      ....  . ...  MOMMM?$M  O=MOM, :.MMD=Z.,M8MOM+D...   ...    .  ..  .  . ...  ..  .   .............
  .....     ..  ................... .   .. ....  .   ...MMIOMMMMM, .MO.....8M+  . OM8MMNM ..   .      .  ........ ...  ..  .  ..............
    .................. ............................... MI8O?MDMMI,.. . ...........+M7MOM8= .................................................
    .... ...  .....  . ............ .  ... ....  ..  . D~NMIN?MD,......7$Z.Z.....$$MIMMND8......... ..........  .........  ... .............
                ...... ..... ........  .  ..  .   ....,O ~..DM7OI..... ,I+ . .. .,OM7M7.Z~O    ... ........     ........... ................
                ........................  ............=D?..,.MMNM.  . N,.. D~  .MM8MDN.D8.M .......    .. .............. ...................
    .....   .. .................... ...    .  ...    .M=Z. +.MM?MM.... $MM+, . MMMNO7M.888= ... ..............  ............  ..............
    .       ..  .....................  ........  .   .M$7M?+,NN~MMM ...........N:Z=M MOM8+ZD...... ...........  . ..........................
    .... ..     .......................................78N8+MN7.NDMD. ........D ,M.$MMMM8N7 ...... .........................................
         ..       ..................... .. ....  .   ..M=8MDMMMDDNM .D:.    7$.N,M8=DM8MDOO    ...    .   .  .  . ...  ..  ... .............
    .           ...... ................... ....  ...... MMNMN7MODMM.:.~M7MM$.. I.MMMMMMMM  ........ ...  ........ ..........................
       .        ............ ..................  ........NMM?MMNMMM,: ...D . .. M,.MMMMD   .   ...    .  . ...  . ...  ..  .................
    .... ..     .......................... ....  . .. 7  7IZMMMMMMMMD ...$   ...$.NMM ?DD7 ..  ...    .  ..  .  .........  ... .............
    .................. ...........................  ZO OMO8NMZM$88MNM:....... 8,OMMMM M.$, =M8.==:. ........................................
            ..  ...  . ............ ... .. ... ..  :7.N7M$8Z8M7IM:,DMMZ .. . O:MMM+?. . ~..D .D .~ = .......................................
    .... ...   ....  . ............ .  ... ....  .NZ ?,N. .$ ON ZN7~8IMM=~..:MM.8M.  .... . .:M~? . 7..  .....  .........  .  ..............
     ..         ...... .................  .....  .? I:M.   Z..I $?M.8O.NMMNNMM...~,.. ..., ..Z M.N..~.........  ............................
.               ........................  ..  ... .=$O+~ . Z... 7O  DO.?MMMMOO..:$...O...$,. N,.NNM.,~.................. ...................
    .... ..     ..     ..... .  ...  .....  ...  . 8ZZ.... Z=.. .   .O.+=Z.M$Z$.$...,M...Z.  M...:D+ :   .      .      .   .      .  .......
  ...... .........................................?,. ,.I. Z:. ....... : O M...,N.,  D.... ..O:.  NM. =..........   .   .  .... .. ..  ..   
 ...... ... .. ....... ................ ......   .N. ?..N DMM . N..M ..M:. MM, :  Z.+.~=O O..?O...,+N.    .  ...  .. ..       ....          
    ...  .. ....  .  . ..... ... .. ...........  :.~7Z..Z?MMN   $  M. DN+$.8M7.  ,N$MM M~7MD.+=.+  I8N.  .    ....   ... ..        .........
 ..................  ........... ................M +$=..:MMMN..~D  ?..$77.,MM$ . 7$MM ZMZMN$7ZDOZZ. ~+D.      ...                        ...
    ........... ............................... .Z ~Z...=MMMM .+. ~~..88Z ,MON  ,IMMMM8,.MNMMM8$O~O.::=D .    .........  .........    ......
  .. ... .. .. ....  . ......... .. ........... Z. 7..  .MIM.~ +N   .,:ZD ,M:,  :?MMMMDM...MMMMDMM:~ NOZN..   ....   ..              .   ...
  .....  ..... ....  .....  ........ .......  ..Z:,  ....MMM ..DO..  I:Z$.MM..  .MMMMMZZ . ,MMD=.+M7MMD+.M? ~   .      .   .... ..   .      
 .......... ....................................MO ......NMO ..IO  ..+7~ .MN.$  M,,8M ..   . MMMMIMD+I~M.N8O:~...    ......   .   .         
 .  .... ..........  . ...   .   .............. M7.......M$MD..:O :I 8?=I.MN.?..7M7MMI778  .  ,MO...   $  M.8 ... ..   .   ....   .  .   .  
 .............. ................... ...........:$O.......MOMM,+.~.~ .I8O. MN  ..~M.MD  =..... $OOMM8?   , $N: ..............................
    .... .......  .............................M$. ... . NMMMN.?,. ,..DM. NN. . .MM=. NN   . 7~DM  ~7DNMN~.7~ ...... ... ...................
..  ...............    .......  ... .......... DZ, ....I MMMMM IM..,8  D..NM.,  :=+N8MMD.,MMMMM8I: . ,,Z,NZM. ...   .  .   ........  . ...  
 .  ....... .. ...............................,I8+ ....8IZ~MM.7?M7...8..  MM.$?.,O.8MMZMMMMMMMM ZMM8Z,.  ,ZM~ ..  ..    .   ......   .      
 ....... .. .................... .. ....... ..MZ: ....+DZO~NM MZN?.? O?,..NM.8Z....=MMMM8DM?MMZ  .NNMZN.  ~IM.....   ... ..        .........
  ......... ................................  ZD......,IMZ,MN.7DNN .:II=..:M:Z8  .:NIMDM=ZM,O8N=   ??D+?.:ONM.  ..  .....     .   .  .......
 ..................  ........... ........... .ZD. ....:7Z.:N..7M8MM8 ,:+. +M,MN  .MM8MMM~$OZ $NN :D  :?ZM..M8Z...      .      . ..       ...
.   ........................................ MI.+ ...., M.,M..MMMMMMM, 8   .??  =MMOMMMM+.NM   . ..O  ...DM.$=...   ...    .    ..        ..
  .. ...... .................... ...........+IN+.......O$:OZ.,MM8MMMMMMMMMMMMMMMM8MMMMMM:I~MM.7I+...  .8MDM$. ....  .... ..... ... ....  ...
  .....  ..... ....  ............... ...... N7~  ..  ..MO~O= NMMMMNMM8MDMMMNM$MMMZZDMIM,  :M7~. MMM87 .  N:   ...      .   .......   .      
    .  . .. .. .  .  ........... ..  ..    =8?~   .~D .$~~M. NMMMMMM=Z8NMMMMMMMMMMMMMMM,   ...=M=8MIIMO.O.I.  ...    ..                     
........ .....................  ...........M:N.... +$~,N,,M  MMOM:,M,N,: 8,+N?=MMMMMMMMM.  . ..  ,M~MM+:,:....... ...  ..  ...........   .  
    ...  .. ....  ........................ ND,... .I7,NZ:IM .OMMM,M+ZMNMMMMMDMMMMDMMMMMD.. .........MZ ..  .. ....  .... ..   . .. .........
...................    .......  ... ......,8Z..  ..8I.O$ DO ..MMMMMMN$NNMMMMMMMMMMMMMMMMD=.    ... ... ....   ... ...  ..  ........  . ...  
  ...... .................................7.I..7 .8$7=7==D8..7MMMMMMMMMMMMMMMMMMMMMDMMMMM$...  ... ........   ...    ..     ...       .     
 .......... .. ...........................$... :? OO+~M?:M. 8MMMDOMZ.D=DOM8NOOONMMMMDNDM==N .  .....  .  ..  ...  ..    .  .......          
    ...  .. .......  . ......... .. ......M?.   7 ,ZI.MI,M +DM$M M+:~M.D,MN     NMNM.D8=.D=. ...                ..   ... ..        .........
 .........................................7$$.. I..ZM .$.Z~MM:M,+D, N$...:,.. ,=N:NM:.M,8MN. ..... ...    .  .....  .......   .....  .......
 ..................  .....................M:7,7,=.:Z?=,O?,N MI8 .,8MM,    ,.. .,M~ZO8.O .OMM          .       ...               ..       .  
    .    .. ..    .............. .. ......=7+ Z,I.IZ8O.Z7 M.N$O :..?N. .. ...  .:::  M,.8,N7:      .  .       ...    ..    ...  ..     .. ..
  ........................................ 7, O::.:M77DM .M~8MI ...,+ . D...... ,:? .MD.~=M+N..... .  .... .. ....  .... ......... ....  ...
  ............ ....  ..................... MZ ~ZI ?8NIM,. ?ODN, ...,,...O.N...MZ.~N ..$,.Z=M++..      .  .... ...    ...   .......          
 .  .  . ..   .....  . .......   ......... I?M .?7MMMM.. N~.8~I,.......O: 8 N.N  .D  .~ .,.MM= ... .  ....... ... ..   .   ........  .   .  
 .  ............................... ...... N~:=MIIMM7... 8$,8=I.....  .:M8+=$7M  .  . ~. .OMMM.............  ...  ...  ..  ........  . .. ..
  ......... .............................. O.. . OMI ...~~I.N.O ......., M7M.DM  .  ..$ . :MMM.....   .... .. ....  .... ..   . .. .........
 ..................  . .......  ... ....... Z~MM=+......M 8 D D.....   .?:MMM8N  ... ... ?.?MM.... ........   ... ...  ..  ........  . ..   
    .... ..... ........................ ...+,....M......N:Z.~,?,....   ...NMN:D..... ...,M,:M. ... ........   ...      ..  ........  .....  
  ...... .. .............................. N..:..M..... 7,+D=,: ........,,8MZ$N...   ...8:ODM. .....  .  ..  ...    .      .... ..          
 .  .... .. .. .  .  . .......   .. .......I..+. $.  . $,$ M 8,.   .   ..:8MMZN         8?NMM.....            ...      .      .      . .....
  ........................................7..~O .7.... M.8,D,$. .......  NIMMNM  .......87OMM............ ....  ...........   ..............
    .  . ..........  . ......... .........7. M+..7.....M Z~8.7  .        :.MMNM?    .M~ 8.OMM  .      .       ...                        .  
  ........................................7 =M O.7 ...,I~+ .,  .:  ..... .DD78MM    .NO.8,OMM..... .  .....   ....  .... ......... ....  ...
  ............................  ..........M NM.M.7 ...,?7.OM.,  O. .  ...ON8?ZND.    .=:M,OMN .       .  . .. ...      .      . ..          
 ......................  .................7,M?,.......,.$.,M ...7  ......M=M?ZNN ....,8+88NM8+..   ... ....   ... .. ... .. ..           .  
........ .. ...... ....................... O+MO.......,O?~?: ..7Z  ..... :,M8?NM..   $M MZ=NM=..              ...    ... .....           .  
..............................  ... .......?,=M ......I8Z.7.I..ID....... .ZN88N?,... +8,NZ N++.... ... ....  ....   .  ..  ...  ...       ..
 ................. ....  ...................=:........MZZ 7~ ..??   ... .+7,MDM$+,    7,8.NZ.M.   ..      ....       ...        ..          
...................  . .......  ... ..................MI?,8?:..+ ........N:+MMN8, .. .+,,+M,~M:... .............. .................      .  
. ....................................................ON7.$,$  + , ..... +,8MDM~     .M,.N=,8OD.   ...   .    ... .. .........  ..          
 ................. ... ......... .....................,$Z.$.$,8. M? ......$?MMM D     :  O=7M8N   ..   ... .. ...    ..    .             .  
 ................. .......... ........................,$=.D.$ D. +O..... =Z,MMM,N.  .. ...:?MDD   .        ...  .    ..  ..   .      .   ...
  .....................................................M+ 8,,.+ .N= ..=.,88:MNM:O.  .~   .+DMMD    .   ....   ...   .  . ......             
.................. .............................. .... M,,=.:,M  D ...+. M,:MNM:,   .,     :=+D          . .. ...    ... .. ..           .  
..................... ................................  ZZ 8=?I.7~:$..+..=.OM8M~ ,+  8. .  ,:M,.   .     .    ...    ..                  ...
.......................................................$.8??M , ?+,..I7.Z.Z8MIMO.=? .M, .Z .Z8..      .         ..   ... ..    ...     ..   
 ............................... ..................... 7==7.$,..7.?  8O M:I8MOZ,.D .M7 .8:8 ? ..   .     .      .    ..  ..              .  
........ .. ...... ....................................  ::~8, . N . N==8.NMMM.Z:D DM  8?$8:....   ... .. .  ....    ... ......          .  
..............................  ... ....................7Z~$MDM =,.. ?+.N~MDMODDM:,ZD OM8? D ..... ...   ..   ...   .  ..  ...           ...
.................. ....  ............................ ..?$?7=+7 +=8..I.Z8+MMMMO8M.DM MMNMM$    .  ..  .   ....       ...        ...         
. .......................................................8I+7N7$DIZ7N8?.DMMMMMMM$DM?NIZ?M.   ...   .          ...    ...    ..              
 ................. ... .................................. .+MMMMMM8M:MMMMMMM$NMMMMMMMMM,.   ................. ... ......   ... ...       .  
 ..................... .....................................$MMMMMMMMMZ~MMMN$=MMNMDIMMN,.    ...              ...    ..         ..          
 ...........................................................:MMM8MM=MM.~MMN8$~+MDDM.+MM .    ...         . .......   ..  ...   .     .......
  .......................................................... MMZ M?MMD 8D8NMO=+MMM=.MMD.     ...   .   ....   ...   .  . .. ...             
........ .........    ........  ................. .......... MMD,MMMZ8 ZM8MNDM?MOZ,~MM: .   ....         . .. ...   ....    ..           .  
............................................................ MMM:MN7M8 MM8MMMMMMINI:NM...   .   ..       .    ...        ..              .  
........... .................................................,MM.8IMNM.MM MIDMNM?D,OMM  .    ...  .   .         ..   ... ..    ...     ..   
 .............................   .............................MDO:NMNM.MM.MN8MMZ+$+8M?  .    ...   .     ....   .    ..  ..              .  
............................................................. MMO~NNNM MM.MMMMMON +MM ...   ....   .   .. .   ...    ...   ...           .  
..............................................................7M?:8MMZ+MM ,MMMMMN.+MN      . ...  .   .      ...    ....        ..     ..   
 .................   . .......  ... ..........................7OZ?ONMIZM..,M8MM7,~MMD....  ..  ....... .. ....... ..... ... ..  .. ..       
...............................................................MMMM=M.8M . MMN+M DNM.....  . ..... ...    .   ... .......  ...              
 ................. ... ......... ..............................MMMMMN.NM   MMMMM :MM  ...   ...... .   ... .. ...   ....   ... ...       .  
 ..................... ........................................MM+8M:,M8   MMMDM::MO  ...    ...              ...    ..  ..     ..          
 ..............................................................M$IOM ZM,.. MMMN+,MMZ    .    ...           ......... ..  ...   ...   .......
  .............................................................NMMM?,?M.   MM7M .MM.  ...    ...   .          ...   .    ..   .             
 ....... .........   .........  ...............................MMNM? IM.  ,MMMM..MM. ...    ...... ....  .... ... .......   ..  ...      .  
..............................................................7MMM8~ IM.  MM7IM .MM7  ...   ... ..       .    ...                        .  
 ............................    ............................ IMMNN, 7OD .MMM8M:.NMZ.        ...   .   ......   .    ..  ..     ..   .   .  
..............................................................MMMMM.,+MM.:M8M8M .ZMM, ...   ....   .          ...    ...   ...           .  
............................................................ MMMM$MM IMM.MM78DM, 7MM8....  ....... ........  ....    .......... ...         
.................. ......................................... MMM7NMMO NI.MMMDMM8 +DMM   .  . ...              ..    ...         ..          
 ...........................................................,MMM+NMMM,+MMMMMODMI IMMM ...  . ............ ....... ............  ...    ..   
............................................................O8MM+DMMM+ NMMMMNNMO .8MM ...  ..   .. ...   ..   ... .. ....  ...              
.................. ... .......................... ........ .MMMN?NM?MM,DMMMMMMN,.7DM,8...   ...... ... ...    ...    ...   ... ...       .  
 ..................... ................................... .MMZ$NOMMMD~MM7MMMM?.+MMMN.~     ...   .   .... .. .........  ..                 
    ....... ......... ....... ................... ....  ..  MMMMM??DZ~MMIMMMMMN7MN,8:?M..    ...  .       ...   .    ..        ... .. .   ..
. ...... .................................................  :.MMMMMNO.N8MONDMMMMN8.M.MO..    ...   .  .  . .. ... ...  .... ..    .      .  
..............................  .......................... =.87I+MMMMM$N O.8.ZM 8:~I.DD.    .   ..       .    ...    ..                  .  
...........................................................~~O:8.O=MM=O~ .=$:O, ::D,=M$+     ...  .   .         ..   ... ..    ... ..       
 .................     ......    .............................7.Z~ZN=,I.Z,7:.8.:~~OI:N..     ...         .      ..       ..              .  
............................................................... D?7M+.,7+.N+I7.Z,,$.7=: .  . ...   ... .. .   ...    ...   ...           .  
................................................................,,O$ = +.=?,:Z.I..I~N I+.  ....... ....  ..  ....    .......... ...         
.................. ...............................................8.=.,N8:O,,8.= 8:$.N.8.  . .....            ..    ...         ..          
 ................................................................  ,,.7$=$N:I+ ~,D,I.O~Z=~:    .......... ....... .................    ..   
...................  . .......  ...................................... .I?N,7:I?.,~I.M N,+$ .  ... .     .    ... .. ....   ..              
 ..................... ................................................,.~O.8.=.M,?=~Z N,I~=Z,..         .    ...   ...  ..              .  
 .  ..................................................  .........  ....:.M O~.I,?.$:II:I.$ M Z  . ..  .  .........   ..  ...   ... .. .   ..
 ........................................................................ .?,8$.Z,8==$.Z,D.O.D,7  .             ..       ..   .      .      
  ...... .........    ........  ........................................  .::Z:.:~+=~Z,:~:Z:~:8.8.D.   ... .. ... ...  ..  ...           .  
....................................................................  .   .O:,+=$+~$, :.?.$ 7.8,Z.+::7.Z,,    ..     ..  .. ..           .  
 .......................................................................   D~?III?~8N.N.O.=.?:,~.? I D 7.7+..   ..   ..  ..    ... ..       
..............................   .......................................  . =~=O~O$:D  .Z,~:.. : O $,Z.? M$.    ..     . ..          .   .  
........................................................................    M..,M::.. ,:,=~..Z:O.~.Z 8,D,:$I8 ...    ..     ..           .  
..................   ...................................................    ..NM I.7.M.., .,II?. :.N:8 ~ M,O  ...    ... ......   .      .  
....................................................................  ..  = =?,Z:Z....~  ,$,: .7,..: .. .O,?=...    ....   ...  ...       ..
...................  . .......  ........................................ M+:D,,..:.. ....  ..  ... ... ....   ... .......  .... ...      .  
........................................................................ ? ... ...   ....   ...... ... ...    ... .. ....  ... ...          
 ................. ... .......   .......................................   ..           .         .      .    ...           ..           .  
 .....................................................  ...............   .   .     ..  .    .......  .   ....  .... ..  ..    ... .. .   ..
 ................. ...........  ........................................     .      . ...    ...           .. ....       ..   .      .   .  
.   ..............   .........   .......................................   ...        ...    ...   .     .    ...   .  .   ...           .  
""")

page111_art = ("""

...................................................... .M7,.................................................................................
......................................................:+.~.M................................................................................
......................................................ID. .8M  .............................................................................
...............................................  .. .~+?.7...+.  ...........................................................................
........................................... ~=NN7MO8MMZ+8MM?MMDMMD~.........................................................................
..........................................OM$NMMMMMMMMO.MZMMM$MMMMMO$. .....................................................................
.......................................I8MN?MMM.8ODN+8O.,MZMM+M,MZ:NM,M+....................................................................
......................................+MM:MD~:7MM:MM++N+.N8+8=M+..+M?M,ZMZ .................................................................
.....................................N?8$DDM~DIMMDM.7ND8  ,  ?=:D,N$M=D,MDM, ...............................................................
.................................. Z?MM7D.OD=Z+MMMNDM$OMZ~~..MM8MM$Z8.,O$M$MM:..............................................................
................................ ,MM,~MZ88MNMM$IO.~7~,:NDM. .M~OOZOMMNMMZ$78M$+  ...........................................................
............................... N7M:MI:7MMZM=N~DZMOMNM7MM$, .M..D$++~OMM8MM,N OD............................................................
............................. +MMM,NM8NN~O..DMI7DM8~8D8?8D:7DMNNM:.=OM DMMMMMMM+M...........................................................
.............................,=8OM.ZMM~.,:DMI7 IMMIM,MMMMD NMM~~?MMM M ~OMOD=MMMM+..........................................................
............................~:,+M?MM.D :NM~7INM$8..8M?M M.8M+MO:N+M8=MO,OI MMM.=MM .........................................................
.......................... ,8MN=MMMN.Z?I=MZZ?MIO+D~8MM?Z~:NM~=MM+DMMD?DMM, :DII=MM:.........................................................
...........................MM,:DDM .MD=M= ~D$.MOMMM=D~DMM.MMMM8MZND=+$D8MN$D8MMM,MM ........................................................
..........................$,~?MM,M.MN.8.NO8DMMM8O==D 7=MZ 8+ OD.,MOMM8 :DMMM:MMNM8D.........................................................
....................... .,?=,M7O MD8,MDI.:MZ?O$ ?O. N.O+MM M ,==:M+I,N=D?ZDM~7NNMNM. .......................................................
.......................  MM7MM..MMZDIID.MMMIO$. .D.OMMMZMMMMM?~Z.?.+M+MMM7ZMMD NMM.. .......................................................
....................... $MMMNM.IO=M+=..8ODN. Z .MM$$O?,ZMMM=M OM.?:.M+7MMM7M?M~OMMM.........................................................
....................... MMM88DMMMM8I,MM78+  OD?7,:.7MIMZM8~DM D=MDM M.:MMMODDNMDM7M. .......................................................
.......................~M7MI N=8M$ZMN:M.,Z I$NMMDNMOZ7MMMMODM:NMM8M~M..ZMMMZ$O:8 MO. .......................................................
.......................77MM~=M .=ZMM,M +.Z+MODMM+DD.IMM+MOM,MM8,O78MMZ.ZMIMM?.D8.Z:M........................................................
.......................7DM?MN+7?DM~$MM..8NNN.+$D8MI8NMM M8MMMM~~NNI:MM NM,MD8DMM8N:M........................................................
.......................7M~+MM OO.MM..N.?NNMMM77$$N.++~~+,88:.MDNMD. ZOOD$~+MM=MMMM,M........................................................
.......................IM~N8+.8=MMN+.N=MO$MIDDMNM,+:M: O.,8=8NDZM?DMZMN$$??MMMD~NMDM........................................................
.......................7M~MD.N+M,.M.NMMMM88+Z$DO+ $,:DO$+$DMM=7=MNM:MM8M$O?DDOZNM7IM .......................................................
.......................OI+ZOMMMON=M:NZMDM+=M$.7M7I7.N:=+,MD+OMM Z =NDM+OM8?:MMOOM?8M .......................................................
.......................M+8.,~OM.:MMM=MMM,MM,..MI:: OM8+..M+M I...,M.M?MNIN?:MMMMMD~M........................................................
.......................8DMOMMMM. MMM7M.ZD7 .........I ...7I ..... .? Z8IOMMOIMZMMI M........................................................
.......................$+MZMMMM..MZMM,8I,  ..........   ............8.IO MMDDM8MMD$M .......................................................
....................... MMZNM8I,NMMD ,N:,...........  M,,,:........, $.ONNMD.M?8:~N.........................................................
........................=M= MN8ZM.$ZM$.    .... ....I 7. . +  :::OM? :7,Z.MN:OMN.?7.........................................................
.........................M?DNZN+MMMNN,=ZIMM7,,,OM:ZZZ: .:  =ZII8,   ...:+MNDNIM=MZ  ........................................................
.......................  I8IM ?MM.MN,.  OMNZNMDMM. ..... ~NM=   ...... Z.?$MMIMMM,..........................................................
.......................  MOMMMMNMMMZ.?I...  .. 8?. ..... $$. N$$7O=,....:.MNMM~MM ..........................................................
.........................MNM=.M+NMM ... M=,,,,M?.OM.....8,ZM, MMMI7D....+7$+MMM:M...........................................................
.........................8,$$I$M$M$ . :M7$MM7I.+MD .....N~,+MMMMMM=?M.7: Z MM8$NM...........................................................
..........................8=M.MMD$D ..M= 8MMMMMO.8......MMZZMMO8MM+.?=~+. .MMM=NM...........................................................
...........................+NNM?M .,N: ..8MMMMM:M~......:N .MMMMM$.M$ ...=+MD$NNM...........................................................
............................NM$O,$ 7?IN. .NMMMMM8,........D$.??,$MM,......~MMMMM............................................................
............................ MMD.M ..ZO~OMNNMMM.Z........=Z7OMM8O... ......N$MO8............................................................
.............................~MO.M . +$ ===~~D. Z,........8=N......8  .... 8~MM= ...........................................................
............................ ?D.+Z ....,$7$7I? ..I....~?. +Z.D . ?$........NM~O. ...........................................................
.............................,.NN  ........ ~D.7ON,. ~.MM,M?...,..........$M=M..............................................................
............................. $$M7 .........ZIM$..=D7.....8$............~ NMM...............................................................
.............................. Z$M..........,8........ . ..ZM...........$ MN7...............................................................
................................OMN. ......,+O ..,:...OM~.. MD.........~.M+.. ..............................................................
................................. .IN. ....78, DM.D7+N ?N~MM$MM:.......Z?DMD~7..............................................................
................................DMN=+M.... M,+?  ..ZO.O.. .. .:M.......~MZZN$I,.............................................................
................................MMM$M:. ..D~8MI. ............=~.=. ... ~MO.+8M=.............................................................
.............................. :MIMD77+. :Z ....8?..........I .. =.....8$~MMMMM.............................................................
............................. IMM~NNNN ..~ .... ..N,MOD8~8+NN ..   ....MZIM?~MD8 ...........................................................
............................ M MMMMMMM .. .......~?Z~~. .~: ..........IMM.$~.MM+M ..........................................................
...........................=MIMOZIM+MI?.,8 .......~:+III, I$..... +:..DMMMM+MOM:MI..........................................................
.......................... MMM :M8MDO,D.NM7,  .....$MMON8Z...... .MD:IMMMMN7.M8~NI..........................................................
...........................~M=MM?ZOZNON$8MM+N8...............I 7D=MMMM.N8M.D8ZDMM?..........................................................
............................NNMM+$O~MNMMNNMM=$M: +..... .+,DM8=MNMMM$MM,$8~= MO~MM? ........................................................
............................,MMI,,:=8N~?M+MMNMMMMNM8~$.MMMMMMMMM?MMMMM:DMIMMM7 MMMD=DD .:...................................................
......................... :DIMMMNMMO.$M.NNMMMNMMM+MMM?OMMD8MNNMMMM8MM8.=8MMMNMMMMMMMMM7?...7+...............................................
....................... ,87MMMMMMMN?DDM78M,$DMMMMDMMMMOMM~DMMMMMD?Z8.:$=$D.NMMMMM7MMM+:.... M=.8Z...........................................
.......................MMMMMNMMMMMMMM 8MMM.MMMMMMDIMM8MMM,MMNMMM,?MNM:M+Z+MDMMMMMMMM MN ....MN..?7MM7.......................................
................... .DNMMMOZMMM8MMMMMMZMM7DM7$MMMM7MM8DMMIMNMMM$ IM7$D8~8$DMMMMMM???.M  . .7M .. I~..O.. ...................................
..................?IZMOMOD$MMMMMMMMMMMMMN+NMM7M=NMM8MMOMM?MMMMIMMM+M=M7NMMMM?M8..... M......=~ . I.. Z~ 8M..................................
............ . O8OM$IMON8MMMZMMM8MMMMNMMM7MO8MZMOMMDMMMMM8MMMO8MMMM?MDM7NMM..........M ...  M... M...Z?..$8I................................
........  .,IO:ZDIMO7DMMMM7MMMMMMMMM$MMOIMMMMMM7DNM,MMMMMMMMM ZM7$MMDOMM8Z?.......  MM M777IM...:I.. M... :.~,..............................
....I~~:ND: ZD8NOM~NDMMMIM$M?DNMMDN$MDM$MMM$MMNMMZ7MDM?MMMMNN??MMMMMMM$MIND ......~MM?$MM8:.NZ..??.. M...:D~ M: ............................
.. M+$ . $M$MINM:8MM7$88MDDM$M$NM?MNODZMMMMMMN8MMNDMMMMMMMMMM8MM$DMM7ZM8ZMDMM .ZMZMMM~.. =+MM..~MZ..++ ..8ZMMZM ............................
.. .$,MMMMMNO8:MD.+=DOMNZD8MMNMM+8M?OMMMM?ZMMMMMDMM+MMMMMMDMMMMMMOD+MI$MM$NMMDI8MMMMM?.....~O..I. .,D  ..MMZ?.,8:...........................
. ~D7=.MMMMD ,M+8?M:MN77MMM=MMMI=MMMM+MMMNM$IMMMO8MMMMMMMMMNMMNMMMZ8MMNMDMIDMMMM~NMMMI.....N. Z,  O$. ..+MMMZ=.:? ..........................
.M:.I+.,M+,OMZN?MMMM$??ZNIMO7+M7NMDDMNM7MNM~MDM8MMMMMMMMMMMMMM=DM8MN7MM8MMM8:MMMMDMMMMMOZ$MMM,Z$DNZ. ,DZDMMMNM.,.N,.........................
D8.  M  .MNN?ZM+8MOMIMMM+~NM+MDNMOMI,M~MMM7MMMOM==MMMMMDMMMMMMMDMDMDM+MMOIODMZ7MMMMMMMMM8 ....   . .   M88MOMM..?.N.........................
I..D. MM+.8NOZMMM$$D$NOM+=OD+NMMDMNMM~M7N+MM?DMNZNMMMMMMMMMMMM7=MMNMMM~MMMNNDMMINMMMMMMM.~8........  .MMD7NMMM.. ,,D........................
....O..M8M.$M78MZ=DOMDZMM$MM8.MMMM7MINNO:DMID$7MMMZMMMMMMMMMMMMDMZM=MMM=MM$ZMMMM77MMMMMM:=......... 7:8OZM.OM7... .:I.......................
 ... $..78I:,MDNO?NM7Z8D:8NIMDN$~.M7M~MOMDMDD7MO?MMO+MMMMMMMM?=NMI?M$MMM7DO8DNM=MNN~DMMM8= ...........$ONN?NM~....~ I.......................
..... ? .M.=+.:8INI?78=D+M$N7M$NOMOMNMDM8NMMM7M$OMMMMMMMMMM8MMMMNM?8+MMMMDZMMDD=OMMMM8=M$= ............MD8MMM,.......7 .....................
....... ? Z=  .=MD+MM~ZM7D$:MNM+OM:I:$MMO+OMMMM$NNMO8M M:MMOZMMMINMZDMMMMDMZMMMMNMNM,MMM8= ........... ?MNMMMD.......:M~....................
.........M.,7.O ,+8M:MMNZ=$M8:7MNMNMMMMMMMM78DIM7M7MM8 $, MM=MMMMN7NOMIMM$D8,~MM+MMMMMMM8M............. N8NMMN ......,D.?  .................
......... +, Z:...O?D~?7M:NO~8ZDMN?DO?=DM+ZDO8DMMDMMM..Z.OOMNMMMMM$DOOMM$MD?M:DMM8DMMOMMD7 .............,MMMMM....... + :7$ ................
........... I.,8$+ .=ZZMZ~$MM$MO,IM+MN8I~OMZM+MMO=NDM$.~.:~NMM=MMMMMZN7OMNMM7M?NMIM$M$MMM?...............?MMZM....... .Z :IDZ$I.............
............  7 ZD~+,..OMMD=+MZ+NM.N:?+7DONN=D$MNN?M:O ...8=M8M?MMM+MDM+7MOMMMM8NMMM~Z=MM= .............. MMO,.........?...?=.,7+...........
............... I :D~== ~?8+N.M$M.ND$M8878+ON+MDO=DM ,.....$?M7DM+8NMMOM8MMMMOMMN=MM  MIMO................ M+,..........I. .$. ?.8..........
................ .:+,7+:?~.~MOD?.M?+MD?DD8M?M8DMMOM+O..... ,.OMMIM?MMMN8$$MD:MMDO  ~Z:NO=M ................D7 ..........I....7 ,=.Z.........
...................  . $D:,.:~MMMMMMN,8M8DZMDDMMDDM.8 ......MI=MMMN8MMM8MMMM=: ,87 OD,8~MZN:,...............Z........... 8.. ~,.Z I. .......
.......................+Z,8D . ,,Z$M,MOZ~ZZOOMM7O+I.~.........O8O8M=MM+7 ..,I$~?MZ +$... M=,7.............D7 ............:O...O..: M........
........................ .D:OM=OO.. OM8ZM+MDNNMDNN?O~........OD.8$=8?... ...~DZ.=+:. .... $O ? .......... OI.............  ...Z....O. ......
..........................  :Z,~NO,..,,,+=DMM$NMND.O..........?..+8O: ,,88~.,..   .........$N.7 .........NN. ..................7... +.......
............................. . 7I.7MI?$7$MI     7 O.........Z..MM?M7=..I?~.................Z8 $7~..... Z?:....................$ ...Z ......
................................. ,  ..:88DDD=~~~++Z~........=~~~~IOZD:.. ...................7M:  .,::.8~+......................,.. Z ......
......................................  .... . .. ?$ ..........., ........................... .IMZ ...M=Z ........................... ......
.................................................................................................?MD?OO.....................................
...................................................................................................,I,DD.  .................................
.....................................................................................................I....,.......................... ......
............................................................................................................................................
............................................................................................................................................
............................................................................................................................................
............................................................................................................................................
............................................................................................................................................
............................................................................................................................................
............................................................................................................................................
 .  ....................................................~M::.............................~M.................................................
                                                                                                                            
""")

page112_art = ("""

....    ..................... .................... .......  ..........  ..                  .       ..       .                         ...  
.... .. .........................................................   .. .  .   .       ..           .   ..    .                ..   ..  .. ..
....... ........................ .. ................. ................ ....... ...... ...  .....  .....  ................  .  .......  .. ..
...................... ......... .. ................................   ......    ... .  .    .. .. ... .......  . .......     ..   ..    .  
.....   ....  .................................................. ...  ..     .             .                 .... ..   ..   ..              
.......  ...................  ......    .......  ................          ..                                                      ..       
............  . ...  . ......    ... .. .......  . ..... ....   ...           N,                                .      .      .             
....    ...........................................................           M,.                                 ..          .          .  
....... ....  ..  .  ....... ... .......  ........... .. ....... ..          =M.                                                            
.........  .....  .....  ... ... .. ...  .     .. ~I77,I7DIIIII~.     .  .   +8                                                             
........ ..   ....   .   .    ....    IDNMMZM+=~ .  7     .. ..,...====MMZO  ND ....  .......  ... .   ... .....  ...  .... .. ... ...... ..
........                 ...  .ONMNN,..,,NDDNNM  . $.$          Z  .,,DZMM, .,,MNM,  .   .. .   ..    ...                ..        ..  ...  
........               ... =DMZ?~ ZI= ..    ..I ...  =.         $  .~  .D. MM=OO8MMZ:OMM?.. .  ... ....... .. ..  ...   ... .. ...... ......
........        ...  . .7MMNN$?~M7$~:~~       .+ ZMMM.. . ... ..Z  .IIZMN  $+ D  .M,.?,77.7OM: .    .. ... ..    .  .  .   .  . .. ..  ..   
........        .. ..ZMI,,8N ..Z,.+7N,~?.. .?7~8.    .MNNNNNNNN :      =..,MMO7  M?. .M. ,,ZMZ.=O$..   ..            ..  ..       ... ......
........ ..   .   ~M: . ..  .   .  .:O+~7.8.7.,D      O ...8MMMMMMMDN,.=..~~~.   ~. .D.. ~Z~.=8D~ .$DD ...    .. ... ..  ..       ... ...   
........        ~D:,                :~=M+, ....M..   +.   ...  M ...   N..,M+.. :M   D +N$OO?MMMM?$7  =MD+... ...        ...  ..   ... .....
...........   .8++ . . ..       .   M OMZM::7MMDDDDD88Z         DDDD8NMMMD~M8DD: .  .,DNM:.:NODMMMN8,~:ND $$: .. .  .    ..       .... .....
........      M O .    ...  ..?NMMZ MMMZ                       . .. ... ..MN$$Z,DMI$D=..   ZM+,$$OMN?MM7Z7. .ZZ.. ...  . ..   .   ... ......
........   .7MM???Z$ .    ..MMI.?M?.             .                     . $MM+.   . NN$. .. ....I87=,=IDMMM$?Z: .I$.    . ..        ..  .....
........ ..:+.. ...   .. ,M: DZ.              .      .    .....     ...8MMMMMO        .~~MO,:MD.. .M8.:+=OMMMMMM7.ID       .  .   ....... ..
 .. .... ..D~..         D~.M..                             .MMMM+MMMMMMNNMMMM?M            .,MM. D+ . OM .Z7DMMMMI..,M ....        ..       
M=+O8MD==+N: ..        7:8~                              $MMOMMZMMMMM8MMMNMMNM8MMMN==....  .   .,8I,   . ,M=ZI7MMM$+8Z=M~..        ..       
. ...?IIMMON.   MMMMMI I$=                            .$MMM8NMMM7$MMM8MOMMMMDMMMMMMMZ$MMM:      ..  ?M:... .?8=+I.O$:... N~        ..       
....... .M:8.  ~     NO D.       ..              . .,DINNNMNDMMMMM8NMMMMDMMMNMMMMN8M8MN8MM$ .        . =8Z.  . :8M    ..7 ~8       ..       
..........O~:..NN8,,,,O D        ..               ~MMZDMDMMMM8=N=~M=+MMMMZMMDID+MMND7MMM+MMM.   ....   ....8= .:I...      ..?I     ..       
........  N : .       ..D                      ..MMMMM=MMMM$M8NMMM$,,MMM,.,,MNMNM:MONMMMNNM+M+            .. .N..N..   7+OM$$MM    ..       
.....  . .8,..  ...=MO~.Z=                   .=M8DN=MMD88M8IMIMD.MMMMMMM,~MMM=.ZOMMMNNM8MNMMMMN...     ...    ..D  M.+7D+.     D.. ..       
........  :?   .,D.  .. .?+               .=MMM8MMOZOMMM8M78M. =7MMMNMMM.MMMMMMM?.NMMZMMMDMMMMMM  .   ....    .. =8.D~$.......  N:.   .     
........ ..?,.Z.$,      +~ M             .NMMMM$MOMMM$8M?M7DMMM~MMMMOZO..IMMMMMMMM=7MMIMMM+DMMMMMD .............. .+MMO Z D....  $+..       
........ .. D..  =~      .Z :N .       .MMMMMZMM=M,DMMMM$ZMM++MM?MMMMMMO,MMMMN,:,,O..NMMNMMMMMMMDMM.  .       ..     M N . 7  .   $..  ..   
........ ..  M    ,~.  .  OMMMN=.       . .NNMMMMMMMN$MMMM=MOMM7M,NMMMM.~MMNMMMMMMM=MMMMNN+8MMMNZM?M,  ..            .O ?M=.       M.       
........ ..  .M .=  8 =Z..    M?M+.        .:ODMM7OMMMO=MZM87M$MO~MD$MD.MMMMMMMMO.D8NMMMMMMMM=MMMNDMOM ..         ..  .D.,+8Z=  .Z7$O.      
........ ..   .D$8I. . ..   . +.I=+O.     ?8MMMMMZ8M8MMOMOM$MM$DZNZZNMM $7$$$$7MMMM?MMMMMOMNMD.NMMMMMMM.  ... .. ...   ~M..        .I.      
............    Z8M:      .,D7~== ~ ~N8MZMM~=DNNM=ZNMMIM$MM$8MM$N+MMDNN?MMMMMNMMM8MNMMMMMDN7MIMMMMNMMM8MO       . ..   .$...    .....$      
........ ..      ~M~O    .M~..  .:8 8~~~M,. . .    MMMMMZMDZMM7NMMDDMMMMMMMMMM:MMM?N8MMMMMMM8MOMMMMMMMMMM8.            $:..         .Z      
........          .M,,+.~?=               $M: ..  MMMMMMMMNMMDZMZMMMMMMMMMMN$MMM:MMIMIMNMMMMMOM+MMM8MMMMN8M.  ..  .. . M.   ... .   .M.. .  
........ ..        .,M.7$~  ..              .,D+,MMNMIM8?M8IMN+MMM8MMMMMMOMMMN+M8=MOMMMMNMMMMMMMMMMMMMMMMMMMI ..      Z  ..    ,NI. D8MMM++.
........ ..     ..   .+M8  .?M8, ..          I$ .?MMMMMM88M8M8MOMMM7MMMMMM7$DMMM8MMODZMMMMMM$MMMMMMMMMMI?IMMM     ...O:  ..   .8 .I. Z    ,I
........ ...            =O =+D,DM+.    .I.~M..  NM?  ,~MMMM8M?MDMMMMMDMMM?MM7DDMMOMMM8:MMMMMM~~. ~+MMMMMZ.       ..8Z. . ..  ., $O.N$       
........ ..    .         ..M .M8=.MMI  . N=7.. +:  . MO  .  +MM. NMMMIM+NMMMMM~MMMMM8M8MMMMMM   .DMM  . D=.    ,MM  ..MM ...7     MM7       
........ ..                 .N: DM8??MM:      ,      .. .    .  .  8DMMM:?MMMMDM:MMMMMDMMMMM~I. .. .  .. MMMDO .::D:. . MMM?7.M. 877        
........ ..          .       . I$ .7OZ+?8M?.  8                 ~$?ZM8?.M .7$D$MMMMMMMNMMMMM8MMMMMMMM7M7~?M$7....        D7~.   ?==.        
........                    .     MO  DMD,=MM8I  .Z      .       .. D ..N.?NMMMZMZ$$ .N. N  8     ,? . ~$..     . $$.   . N?  8.M,          
........   ...    .       ...     . =M7  IMO..   .= M Z= +          D.  7. III?, ... .M  M .N..:   .    ,:.     .O  +    .+O   8   ......   
........ ..     ..   ..     .   ... .  .$8.$8D  ......  ,.~O.O.  .  ,....:M88$.8    . +. =..~ .:  .....   .   ..., D,   . OI+N,.     .......
........        ..   .      .             .,8M~8:,             I,.IOD  = .,,?D,D     ::. ~ :=.Z:       ....       ... .D.NM8..        ...   
........   .    ..   .   .  . .. ..    .  ..  .~$7~. . .          = ?..O.??I=..M    .DM....,:.  ..       ,+      . ?I. +8.  ..        ....  
........                    .             .      . .+M$= ??O? .   MM.. =.++?MO ,.   .           ?7.       + . .Z$,  OO?                     
........    ..  ..       ....    ..           .  .   .   .,MDD. :MMDZ .. 8DDD,~ .    .  .. .. .  $..     .+    .DM: .    .. ..        ....  
........   ...       ........ .......  .  .................. ....NZMM.?,~O:MN Z,..  . . . ~$.=.  .:N  ..:MMNN.  .      ..   .. .     .......
........      . ..   .      .   ...     ...   .             .    :8. . .  O8DMMMM===+=========NMMOOOO .  . ..   ..   .......   ...          
........             .   .       ..       .      .   .           MZ   .   7.~,:, M...........  . .  ..        ..         ..          .....  
........              .     .                 .  .               MO.....  M ?,~ ,.......       .......   ..     .   ... .  ....       ... ..
........    ..  .. ...   ....    ..  ..   .....  .......  ...... M. ... . M O O.: ....  .  .... ......   . .. .. ...   ..  ....   ... ... ..
........   .    .. ..    .  . .....       . ...  . .. .. .   .. =D.....  ,..$.8.M.  ....    ........     . ..    ....   ... .. .     .......
........ ..   . ..    .  .  .    .. .   ... ......       ...... N . ..    ..I=,.D                  .                     ..    .     ..  .  
........ ..   ....   .    ...      ..   .......   .  .  .   ... M          D.= ...                                     . ..                 
 ........       ..    .     .   ...    ........  . ..... ... ...8   ....   M O.N  ...          ... ... ..                .. ...    .........
........    ..  ..... ....  . .. ....  .  .....  . ..... .     I ..         .Z M.                                 ..                   ..   
........        ..   ..     .          .  .        ...    ..   M.            ~~,.    .  .  ..      .      ... .. .  .  .....   ...        ..
........                    .   .         .      .       .     M   .....  ... :.. ... ..       .....  .  ....   . ..     ..   ..     ....   
........                 .  .   .      .  .   .  .             7   .  .    ...N..                 .      .       ...     .. ....     ..   ..
........ ..                 .             .                                   .         .                       ..     . ..    .            
""")

page115_art = ("""

................      .. ...  .....     .  .       .             ...    .  ......   ....   .  ...  ...   .. .....  .  ...  .  .. .. ............................
..............  ...   .. .......            ..      ..                  .                       ...      ..     .       .     ..   ..... ..   .. .. ..   .....  
................ ..................   ..... .... .. ..  ....                                    .        ..   ..      ...     ..    ........  .. ...  .. .....  
......... Z........................ .............   O,.............                         ..  .        ..     .     ...    .++++NZZ ......  .. .. .... .....  
.........,M ..   ................        ..   ..   ..M?,           .    .                  .    .        ..               MM?MD ...   ..............    ........
.........Z? ..  .................  .~.   ..     .   .OZ8.   ..                          .   ..  .     .. ..   ...     ,88M~N.  .    ........  .. ....... .......
......8..OO.  ..  .=  ..... ..  ... ~M+         .    :MM           .    ....               .    .  .     ..     ...  N87:Z? ..      .................? .........
.... .M...:.......MD............... .DM............ ..I= .......... ..  ....    .  .  .. ...  ...  . ~+, .. ..  ....M~~M8  .  ...  .................... N.......
.... .M..  ...   ~.M.... .......     .+          .+=  ..   .                       . 7I,            .  M=..        MZ =M=     ..   .  ..... ........    .MM ....
.... .M7 .....  .M.M.. O ..           .. .. ..   ..M.   .          .    ...     ...NM .         .  .  .MM.      ..$MMN.8.  .        .......   .. ........ M~....
.... .?M:........D.=  M ... .. 8M~.        ...     .N+           ................MMI ............  ....M8...  ...D .DM7..........  ......................  M: ..
.... .Z8D.....  .NI  DM. .....   MM      : .  ...   NDI     ..  .  .......... ?~IN  ...................MM  ......N~.7N7 ................................. :ZM ..
..... M M+ ......,...MM ..........ND..  .?......... M=DZ   ..... ............MZ?M.....................ZZN.......+I.:ZI  ..................................MIZ,..
.... .OOZ?+ ........?IMI....     .O78.............. 7~IM.     ...........  $M+7M ................... ,7.,.......OZ~,MM. .................................~+?M...
.......M D?8........?DNM .. ......:7M   ............M+I~8...  .. .........$M+.M  ................... MMN .......M~N.MM. ................. ~M.   .........?M=7...
...... $ZZIMD...   . DO?D.  ..  .  NM      ........ ?,N M          ......I,N ,8.....................NO$ ..M.....?+$M:M. ...................,MDM .....  D, :M....
...... 7+~N.DZ, .  . =N7~+?...     .N   .  ...   .. ~+,O:=       ..... .M7.O??. ....................?N. ..ZO....,:~Z,~. ................... M+OM,... $IO8:M.....
........Z8:Z8,88 .. ..,NOODN=........N.......... . .==,N,=...... ..... ?8Z:D~O  ......  ...........7N ....O8.... DIN 8.  ...  ..............DOOO8~IMOZMIZN......
........:Z=M.Z=787  .....D8OMD  .~= . +? .. .. .D  .Z.M7.=. ..   .....+.D~ DIO.....................M, ...$.?.....D~$7N......................? 777M~77:IM:. .....
........ .7:=M,M DMN    . . .M..  . ... =N. .... ...N:M~=+       ... .$.D,=M,Z........ ............ .....M 8.....:MNMM...........   . =NMMO8MDMMMMNNMMZ ........
..........I?D.N.O:,D=$   .. ..  ..........IM,..  ...+M787+  ..  .7 .  M ?O 7ZD. ...... ,................ ?.7..... MMM~......     7M7NOZI.7D7M777?8MMI...........
............DD=??=M:OZ?M8~  ......,8:  ..... ~MI8MMMMM.DOMMNZ,. ....  Z~,D::7,O...............  ........ ?8...... M+=... .. .OM?MO88IDO?OZDOMZZ8NM .............
............ 8+Z:D +$:N,DD7O,.......~:O~.........OMMNM7MMIIDO+8+......$$ 8,.Z7+I .................. .............:N7.  ...D8D,,.......... ,O,~88D= .............
.  ...........:$O:,D~$+?M+=O8M?. ...  $.D.............+NM+ . 7MZ8I  .. M.=7.I?778 .... .. ....   ....... ....... $ .. 8 ..................8.IIII8. .. .. .......
..........  ....  O7$N N=~7D~7,N,. ....O N.............~MM...... :M,....D N,O +?$D .  ..MM ..................... ..  MM,.   .... ........Z~~~~NN......DO.  .....
.........8~$. .........7$NMMIONM88.... ?,, ...... . .... +O ........  .. 8~,M.I$ D$8. ..DO....  .  ........ ........MMM:     .......... MMM8MD$ ................
... ..... $. 8. .  ..... ..... =+NN.....Z N..... ?? ........  ...~$.  ... ,$.~,?=8,ZM ..DD8.  ...  .........  .....+MM7 ...$D....... .8?+???M ..................
...........M..$ ... .... .. ......,......D=...................... ,M .   ....DNI?Z88=N..8IO.........  .......... ..M8M . .DD+ ...... MDNODN...........      . ..
... . ..... :.M ......... .8...........................  ..   . ...MM ..........,MD$DM .,M.............N......... ,M, ...ZMM.....   MMMMM,.......    $NMMMMMN,..
... M  ......8$ ...................................... DM  ..D~. ..D~M. .  .........88I..  ........ ...8..........D  . N~MO ......D~~~8.... ......MMMOODM~~N,M.M
...ZMM  ....................  ........... ..............MM= . MM...IM:  ......     . OI. ...    .  .  Z,~.......... . MZ~.. ....7$7MI...  I$.... 7....  ... O$+8
...$+ZO .........  .  .. ..~+.. ....7.....I..... . .....,MZ:..I,D. IO$I .........  .....    ..  ......MZ,...........    .  ...7MZM.  ...ZZO......... .. ....~=7?
.....,N7.........  .  .. .. 8M.....7  ... M ....M, ..... DZD..:~8,..$MI .........  .....    $Z  ......7I........Z...    .  . MMO .+ON8+I7M,..........?+......$78
... NN$Z8.................. .M,=NDM7D.... . .... M......  $M.. ~$8. MM. .  .  ...  .  .: .. $M:.      , .7$ ...M:...     ..MN:,NM~M:M?MM.. ......... .......NMM 
...  ~~7+D,........   ....... ,MND+M. ......  .. ~M.......MD+  87D+.~M. ... .....  ...      M7D ......... ...==+ .......8MM.M7M8O. ,.  .  +................DIO..
.... .OI:Z$Z. ...  .  ..... .. ..ZZ=.............:??.......M  . DOM . =....................,O$D............ ~$,.......ZN~.. ............?M8 ..............N ..?8
.... . +=8.MN~MZ$$$$............~Z:Z.............:IM....... ....ZZI=... .  .........  ...  I88D ... ..=$$.  ........$N~.... ....N.....Z7MM......$NM?..  D+ ...  
........OZ+M.8$$ZMM$7Z: ........  .8DM$..........~MM,............?M7....,M.................MI$, . .OMMMM$$$:= ... =M ...... ....   ..,$M.... ,M$M~..?.   .......
... ......    ... .  .. ... ~ ......,~M.DM8 .... :M7O. .$.........MI.....MM .......=..... ~~7O. ~+=Z.  ......... 7 .......Z.......7Z== . ..,DMO$. .,N ....M ....
....................  ....... ......  D..DOMD$I+MN~7O.7M.......... .D... $7,  .....?M... .MMD .MM~  ........   ,I.  ..      ..  ?~  ......::=M,....... =NM ,D~N 
:....................... ........... ?   .MN$MMMMMM?N,87............  ..... .......MM ... MZ.ZIO  . ..........+~ ........... , I. .... +MMMZM+M..... ~MO~ $N8D7O
:N, ........   ..D................. +....MMMZ$,D7=MIN,Z=.................... :  ...M+....   $M:..8= .....,,...~............. $.? ... .Z :DNNMN M=,NDMNM8MM=N~D:7
..8$8?  ... N.. ....   ++  .......?+.. $N8MMM.7+.MM=M+I ...................... .. .??~.....+M. .=M ...... .. ..8$........... ,MMN. ...  .ZIOM$.:.7=8MI=M=$+78:I8
. .,MZ.OMMM.  ..  Z$MZ7ZMOM7...$Z.  :MM8 MMO:DMMMMMM=MI=N.. .8MM? ............... OIM ....:M .  ZM .......... NM.... M+. Z. ?MMMMMDMZZMMD$NIM=Z7M+DM+:M+77$~ZNO:
...,=:DDMM . ,D8$=~OD~.. .. .  ::NM7 :$?~ M:NMMMMMMN:NM,M .. =MO O8M, ...........:I88.....D... Z+M .........I~=+ .. :  +?NM?MNMMM+=N.,N 87=?IMMMMMN,,NN=MMMN7~=$
.. . $$7=,+ZM O,IDZM?MMMMMMD?+NMOMMI..NMMZMN87MZMMZMM,MD,+ . ..MI:+OMZ  .........DZM...... ....MZM. ....... MD  .7MMMMMZM+.M=N78IMO..M M M$$$7MZOD :..MZMMMO. 7~
M7D:MM+:N,M:.N=MMD:MMDIZ :MMZ$M ZMI78MMMMMNM=7NN:MMIN~D.8M, 7$ .IDN.,NM..   ....?IN$.....  ....MD+ ..8  ...... ,MNMDMM$M.I:M.N+D=M,+MIMDM7NM$ND7M.I~M8.ZNMMMN~MN
..8M7=MZ+M$MM DIN~+MM8  MM7 ~NMM,N+7DMMM:. =?  M?.,D?N.7N8+ $M ..   8MOM. ++... OMD........... NI+..  ....... ==O:MMM?D,8$MM?7??=M.MMMM+OM7O .M.=~MDMM+DNMMMMMMM
....  MI7M?,M  $ +.. O.MMMM$MMMIM:I7Z.$Z ~:M.~ Z =MMO$M~$.8DM+M.. .....N~  N=..ZOM,.:M........ ZZM.. ......$MI$I8:MMMOONNDZN8O8OD...MZM+ 7O.O7.?~MMMIM.  ..DMMMO
..... M+D..$D8MMI....:~=MMM=MDM,=.$D $ $,M$MMI.M+IMMO:8MM8?~O+NM?~ ..I. . .MD. MZI. :=........ .M, ..Z=.=M:M=D +M....?8MNDNNMON8. . +~...M:M7$M=N~87MM O... M+$.
.  Z... ...M.OMM~...MM~.MD?=.M $+D. :. 8MDOZMMM=~DM  .  ?8+MM8Z~DMZ~I. ....M8. M$.. MM..........~... 7MM8MMM8M?M=?.O. IMO~NM?..~7.$., ,$.~MMMMMM7ZO7M+~M....M7+.
 .MMM...~+ M. ,,7 .MMMM .Z..~$ .N..,.M.+M$MMMM~NZ8,  ,7 .:M?MMMMMMM:D=7.. ++D  Z .. +M...... 7  I:. 8.$MMM7MIM8M:OZI8 IM8M8M....M:N.D~$ ~7D77+M:?M,N:MMMMM 8,O:7
.MIMM :M?MMN .M. DZOM8. MM. ,Z.M$7MM.M  .NMMM?.. 8. M=?M=~OONM~+MN,MMM$$  +~N. .   MM8 =N .. ?M  M....8M8ZNDM~M OMMMM?$N88N:~...~.:MM. M: .OMMD. $MN .MDOM. ND=Z
.IM8M8.$M7N8:7MMIM.N$D . MN :,:DMMMMN,D:..:D.....:=MI+ZMMDMD$:++?MMMMMMN:7.MM.... .O88.MN.~8 ?D?.ND..O+8M. 8, MMN=?MM N8..D8N,M,~MIZDODD ..DDNDO~,IZ. MOD$.. M+ 
..$M   7.I M.MMNM.7,.?.MMM+...,NMMMI....D...... . $MMD7DMMD+8.+D=DDMMMM7D~?+..~,  8Z:M.NN....?,8 NM ,=MMM 7, N $O7I$,.+N .$$:~?7.MMMM8M...O.... ~N+ .  .    Z.  
. D  M M,,7.$MNMM+. .ZDMM     . MM~..... O.... OM.$DMZ7O.M+ ZOMO N8MMMM.,8Z$    ..M+Z8.ON=...M:M.NM M$+M.Z~M.,,+.=, MD.87MM: . 8,?MNM88 $I, =M...? .$+ D?N  ~  8
. D O MMMM   ..8I  .+~MMM  .M.  M..  .77.Z ... MM8  .:~  M$DMM++MMMM~=M. 7:8+ ...:M.8M MDI ..M8:O=M,MDDNMMOIMDM? ...:.$MMN8MM,8N: :DMM . I+I$DMD ,.8......N . MM
..N .MMOI....D? 7  D?,~MM 7DMM7 Z .=I ZZ7M7 .. MZ.........NDMMMMMMMD?MM$. D,M....ZN=M7 =OO . ZD?MM=IM$MMNMMMOMZ: ... $7DOMMMM=$???M? 8  .IZM8MMMO8I.   ? ..O$~MM
...8 ~D7:..Z.ZD:.ZM..... MMMMMMM. 8.8.DIN?I  .~=.. .... :8N8M~MMN,.~MMNN~.N.N .. MIDM ..8M   NINOM NDMMMMM?D$D:~I~ +8D7..M8ONZ.D+D+.O.O ,ODNZMNN$.I.8NNNO, M.,M8
........ ...MM8I N.. .O~. MODDM,D~$.?, M= 8+O$ .. MN~~.N....?M7M+. ..MMM~:+O8... M=ZD ..,M .ZZ?N ,ZOMMMMMZ~O+ .. D,  $+Z,.,..~MM= .O~+M$ ..,MMM==?DMMMMDZM:~?:..
...........MMMMM?. .:,N   MMM8    O~.$MMNDMM,I: . D7.N ...........,.8MD=+Z+D. ...8I7,... M..M$7$ NMM7OM?:M,.. 7+8. 8 N.8D+..$MMMMMMM MO  =.......+ MIMMMZZ .~..=
...........NMMMM7~ . DMDO~7...  .?M.MMMMMMM~.I:O .=D7 ... ...... ..NMN$OIN,MN ...8:M .. .M .M8~.M?+MM= O8 ~.. MM..M=8?. ,N~. NIMMOM8MM  .7 ...,. .D M=O8M..8..M7
....... . .IMNM8  M7MMZMM:..  ..O :~MMDNMM.. M..M=....  7M......=.MM.M8O8I?M8 ...~D=.D...~ ..~.MMMO=$~OMD Z  Z M.DM~INM?O7$II.D8IMM$ 8? 8.    N8=: . II ...N~MMD
....  $DN=NO N$.D. . ,NNM,  OMNM.....MMNMM  ...ZI8.    MMN. .....NMMMMN=8N NI, ...M :M?. I M.+DMMM,,,::NM,, $.O.NMMMMMMMIMM...,NN==   ,:M:,OZDMM........ ..~ZNNM
.... N  .~. $. O.. IM  M. :$ +ZZO= ...IN:........~N,.=MMM=...... NOMMMN,8$ I +M.. ,7.MM. ~MM:DM8MN O?=?.O$ = +.=I OIMMD..?Z=   ....,::.,M7:......8  ....  ~.MNII
....=. N.  . ? =....M .O..7~. ...N~..... ........  .NN$OM+...... ~+MOMM MM....NM . ..MIM I,MM,M:N:,NMMM.~? ,M .+. .=MM.. .,.M=. ....D7N.8, . 8.. ~  ....7, .?+MM
... + .7MM..D  =,MMMN=Z .D,: 7.:DO=M........,MZ....$, NZ~NO .....~+MMDM~DM..  8Z,....ON.N .MMIMN+N=. O.MN .. .N  ...M~..... .O  ~D..MM. 8. .7....,7... O  ..7 ,,
... :7MMMMMI,Z?NN77MMMZ.NNO.M$7MOM$M7 .....,~8I.. .MI 7M..MD.. 8=:=MMMIDIM..  $O$... .8.I~77MZ,=?D..~=I7... =   .D.. ~.... . =~7 .+IIZZ.8.:Z$NM .?....Z...?7   $
... ,MNM8,. 88.OOZNNM. MNNM~MINIMM~ZD......M=$:+?. MM88N  MN.. .$M+M=M$=ZM .  M$ ?:.. M,NI.,M .$D :O7+M ...D....ND.. M...:Z . :I~+7M:N.MIZMMMMMM IOO, Z:$$?8. .$
.....8D, .....N..OO,.~ .8NNNM88M$M.. 8: ...M7D+7DD~MMMI . M+7...IM+8IM?7OD .. ZD  N7. 7=D? :. DM?MM,8.$...O....8MM . 8....~+..:IIMMIM.$M  D7NDMDDI7+D$NMMDMNMOZ~
.....8+ ...,: 8,.... ~ .M.. :$MMMM...  ,,$MMMNI+N~D$M+,.. M=M   ,MM,NN.=,  D~  ...8M..,NM? ~ +DO.N+IO .DZ.OD.  .$D.. O  . MM.. NMM+Z8OM,:$.M7MMM?~7O,? DMMMMMD+.
.....M=:M+MM= Z  +MNDNNM,...   . . .D ... .M .. I?MMDM  . N:M.M IOM7M .. .. ......MM8 .MM.+ .?M Z:OM8..MM +MMNMO.8 ..8... MM....MN,MM$.NM$~.  NM=~  MN+~MIDMMDN.
....+M$MNDOMMM+IM. ONN$.M. +........D .....MMM.?Z7MMMM....M:MZM:7$MMO $M.... M  ..MZD. M ..8 ~DO+M7MMM ZZ.7N?M:MMD ..M...I$MMN:.MMMMNO   =8.. M$ID.   . $MMMIM +
. ~7..MIOMDMM.O=I:. OMM.MMI?: ......MM? ...MMMMMM~M.8N+...M:MM7:M+NM .7O~... M:.. MMM .=...M?.DZ+NM+IM  D7N.?:?D?:...=....,MM.  .+MN. .....O. N$N:::.OZNO7,MI+M~
. I . +M~ZMM .M:ID. 7NZ.I8I8?7......MMN., :IN~?ZMIMDMD=$NIM.8M$=8?M8..$M~.. OON . D~D. =:.,$?.NDINZ7. II..=8=NMMM . I ... .M?..~..  ....$   8 IM+NO~I~?8MZ,N=INO
...... ,:   8ZM.N,OMMD N.8 MNM......~:N,D7=MODMMZ8MMDNI.. ZDNMMMI?I7. M?~.. IDN....D.  =: MM.?,:D=8N~,7MDMMNMMMM$...M .....M.. M........D7...NNMODI,MIM8N.NMM,~M
.... ..     .MM:..ND.MZ+ M .NIMMNNNM=NO,OZMD.,~=   ,O.... M?NMMD7=M   MM~..~=MM ... =  =~MMM $~MMMMN: I   ?:I+MM ..=..... =   ?M.... .MMMM .. MMND7OMZ+?7ON8MM. 
... NMMMMOMN.=M,Z8+Z+=Z=M ..,D NMNM::+O,$ Z.=7Z8MMNOZM$,+8D?=D8DZ,M.O NM ..N=ND.... ..I+MDM,:+8OZ.8:7.ODMONO8,OM. .O.....,,.  II...~88+MOON7...87IMMMMMMMO+I7MM~
.,DD~MI$M+$8N~NN.~O$7,M+,...N.NM?M~M8.7ZNM D.?Z$?M . .MD=,N+?N.M?~M 8.?.8? M=I8...,...7+8$, DNZDIZO,O,.8DMN+,DNM8 $ ....,$.. ZDI..:78:O8M~,M$ NZ77$?MMMMMDDMZMNM
.8D M7D8I.$M MMZMN7IMM~IM, MN $ZM,7?M7M, . M?OMOM  ..?=~MMDD?M:M~IM 8...88+:ZZM~..M~  O77= N877M+MO.   MM.+7O$+.~NM...OMNM..=7ZI..Z.D$=MDI~:M?M=~NMM$$DMMMM$8MMM
Z~O N87 Z?.~.MII$NND$?IM ~M+8+:ZND7D.MO7.DMM8M=MM. ..8.,N8ODM?+M+~$ 8...MM+,INN ..M7,:IM .8=DD= M8.:8?Z~.:7.~~OO8DO,.MZZ=MMO.NM:.N+ZD$OM.I=M.M ?IMNM~MZMM~ :~MDI
MZ:.+. I~=.N:M?MNMMMM~MMNDI,N D.$M8 Z O.NMMMMNMDM....Z  DZMNMM NM8O7DN. NIM.M?D..=87 :,8 N~NM.DNN8ONMD .. +DZNN7 :NNN+ .M.MDMNM  ,NI8..MDMNN?NN7MNMMMMM8?..ZMMOM
.:$~Z.MZIO+,MM+$DD.M=IMOZ$M?+DMZZMDI:M7?.7 .:7Z8M..+IO. ,MI+MM:8ZM878+M.~ M+N~N .D77 O7.$,+I?M=?M+MMO,.   +O ...?8?.M?MZI8?,7DM . 8~M .N 7?,MM$O?8MMMMM78M,=?NDD
~$~$8DDDDDDDM ~M+8M.M7MZM:IZZ,.O8D8Z88MMZ8:. ,~ZMN MO.+~ :N=MDDO7,ON8.$N. +~DM:.MZN..~M~?N N+MN8, =DMM:,. ND+..  ..   .8:IM8~M8...,8+M: .:,NNND~M87~.=$D8?:~$8MI
M.NMDMMZ$ MMM.,7D7M ?MMM. +8+$$M$:ZO~..=~MM?:7?ZMIM$D.. ZM= DMM8I,=MN,?NM +7MD M8IM.8=~$MI7N78$+D IO. 8MMMDNZ=+?~..?Z7O=:D?+=N~....MNM,7~7O8M .DMM+~ Z~Z$+M8M~,M
D$M$MZMMMMMMM~.7OD.IMMMD 77I,:NZ?=8??. .?M=.MM8N.+ MN +:....=MMN8:MM~.87M  MM.D?7M:=.MMMMNDDM+ ......M.M~$MM?~.ZOOO,====== . N  ..=. OMMNDOMO??N=MM~..?O =.~D M?
MOMMZMOZIMMMMM+.=DMZMMM?M~ZMMMM+$N?,7$8:?.O7. N,..MMMM?.M? ... .IMMMDMMMD..MM:ZO$N.7MM+MM8.DM.......7.MZMMMNM7M ....  +DOZMD$?.. ?OZ,~D+.=MM8$MM++Z$M $Z~..8D.M~
M8DM=$7+Z.MMMD==8Z$,MMM MI=?I+N.M7O~=M?7DMMO$+=M8DMMMM8NMZ .. ..D+... .+???IMMDDMMMM++ .... MD ,.$7.,IIMM?M8IMZ=. .  .7=+8Z$8M: M.7?, = 88.MDNZOMND.+: ~$...I.7?
D,M. 8:Z+D$.MMNM$=:MMMM7D 7O:ODMN+M.ZOZNIMMN87IMZ8 NMMMI8ZMMN7:D7.:.        ..OM ....  . ... MO$+DMMMM7MMMNNN+MOZ:. .+?:DNMM=:87:= O:.MMDN8O7MDOM7D:D,7.     8 M
.M:.?.O7D?8.DMZMZIMM:ZMM  :~O Z,MIM88MMMO+MZNMMMZZZZ8MM8OM7IM~OMMNMZ.7ZZZDM,..DMM+++=8MZ:.,+MMM7ZMMMMMMMD?M8DMMDOZ:...=MM.O .$?7:? ...$.~M?M.MMMM$MM.M8:7:ZM?$D$
 M M:.ZI8M7 MMI87,DZ,8MM 8.$D7M~.NMMMDMMD +MMNZN+DDD8MDNMMMMMN+MZDZ,8MM?+MNMMMMMMMDMMMI8~M?MNMMMODMMDMM,MM+8MNMMMDZ:M+,D+$, .8:NDN ....,8$Z MMM$IMMZM $M+MM+MND 
.M.  $8M$87.,$Z?MIM8?88M?.~I??.Z87MMI?M.=MDMMM+=.. .  = MM888MZMMD$~8I+INDO?7MMMMMI8?.ZDMDMMDM$8M?+ZM7$ND.$NM8?$Z:ZMM=+  .+ZMN~.M,M ..... ..DMM+MN  .MM~8MIMO8DZ
.?7.M?MID7 N MDOM~MMMMM+?:.$ ..7MMMMMMO8 +7 MZNI~DN+DZ N,$8OMMZDM=$MMMMMMM:ZOMNM8MMM$OMMMMDM8ZDM+,M8+$M,MOMN8~M+=MM=,8.D ..MDZM.MINO,. .  :D?. .M,.??+NNMMM~IM7 
=.M?MM?$,MM:MMODMD8MM=D++II=+~=MM?MMDM===:?,+N?MZD8.O:?D.?8MNDMM$MOMM?MIMMM8M~MOZD.ZM+MM+$M:?MD,ZN77DM7M8NDDN?,M~8MOM:I: +~.$8M.MM,ZO,M:+D+:MM~:N8,:=MMMMMM8Z.$,
N.+MD,?MNDDMMMMMDMOMO.ND MMD7MO+D8. ~M $.$ =MD~+M:.$=.:  . ..=D:M=ID7M?88?M:7MMMMDMDMMDOMDMMMMMMM:=M?MIND7NM:M:MMDM?M.$, .NM$,N.MMM8MN~MNN~MO MMO :MMMMMM8M?.8.M
N?D.,D,DD,.,,MMMM+MM ,MN.~N.+D~~N?=7~.Z. N.:+M:=M ... .......I,N:D8,M:?N M.N,NNMINM$MZ,M~78M,$NZ.MOI8?$M:INNI. .Z8MODN 8..8D:.8,M:?MD,,N8M O.8MNNN..DMMMNNM 7~?7
=ZZ8$ZNON~DM 8NMMM,+.NMM.:M++D?+877OZ.8NM.OM ?=NM$$8I~~    .M.  7+.$.,O,N Z:+OMZZ=OMZ=M=~M~~$$MMMN+I8NI$MMMMZ. ODDO$+~M..=. . $7M ..:MM.M~7.NNN~M878 MMMMM.D M7:
IZ:Z:I?=$~D$7M,M:,M7$.OZM7MNZ8M$M=MMMMODI.ZI =MIM?ID.   .DDD$O$,$ZM +N=M78MMM$78MMNM?M=+M$N,   .M7M7M~8MN . .7MMM8+=MM N?~MNMM:M  I8D8ZM:8 N?..M++7Z .MMMM M.8O$
.I 8 Z~+D.NMMM$=:?Z8 .M+ MNMO8M.MNMMZM+DM=N? M,M.7 +8DMZNMNMZM,O$,8Z..$:Z.DM=O?MMM8DMNDMD+.=8  8D,==+MMM, O++NMMMMMM. +$8MMNN:MM. ODN8MM M,+. .$NO7IM.NMDM.M 8OD
 =:N$MM?D8OZMMM,I=$..NNM.MMMMZMN8MN .$~8Z,M,8?D~ZI.IMODDM= .:MMMO?8M...D,?+:,MZ.ZDMIDDM+? D,ZI+$.,M.NMMMMMMNZNNM~M  ..  ?ZMMMMMZZ=MM8MMM8M:=.M. =+~=..MNMM.D +.=
..D7M~M7DNMDMNM8,..  8Z NMMMMMMN,:MDM,?M~MNN~,D?D NIZO..~=.DM,~N. .N=~..D?+,.I:77M,$NZ$M.$ D,:~NO.MM,,Z. ,D=.=~MM:,.OZNNMMMNMND,~NM~DOIM,:MO ..,..D ..MDMM.D.8.,
 ONOMZMIDMMMMDMMD .~$D.7M=NMM?.MO=.+=,7D8:,ZDZ~ON8.IDDZNZ7MM=+. ~~,7ODMO8DZMMMMMO=8MIODM~M.M~,ZMMN +~= +NM~.7 OM$ .NM=M$.:MM8ON: .N8MMDOMD~+M.. D:.IZ.ZZM7M .O,$
 .MOMM$M$:7MMMDM8N.77 8D.MMM=O..87M :.+78+IIII:$8M.M?  :M+ZM.M..~D?MM M8N=Z ?MNIOI.MMMMMN8+N8MNZM,Z.O  7IIDN~N M$..ZMM=.8.,I$?~~?. +87MMMMID$MIMMNI...M+. 7$7N.M
. MDMMO.D... ?=MMM, 7O.IOMM:8 Z.D$DI=M.MMMM$ZI:MN?~ 8....M,D.Z .IDOMO M..M,M:~Z?NNN.DMM7M$D,7.$D?,ZI, . ~=N+D?.ZM.O7+M.N..NMN~ODM,.7:MMMM$M+NMMM:DO$...   N MO, 
...=8$7~ IO  .N:OMMMMMMMM.M8.8..7O?MZM.MMM$NN87MMMM$$M. $M~N.$N =?N8 .I.8M+7  .IZD8M.MMMMON78$IMM.Z7.....ZO~IM =M:$MM~ 8.  7:=+8~I.$.MMMM78NMMMO,  =MZM$?D,$.NO.
...M~N.I:.:DO,+~$DM8ZNOONDM~+M,8N8~MDD MNNDM+M?MZMMMNOMD+MMD8D~.?IN7.M~MMDMN.+ ..MNI,OM , N=+ZN$M:OI,N+: D+~?D ZMMMM~~ 8O. . ~8I+:.$.MMMMMMMZM8,=?.O:?$8N.N.I~D?
. DD7.8D  $ZMO=~M.MMOMMIMMM$M: .+D,?MM8MDMMM8ONMM.M.ND$MNMMNM~...O8 MMMIMIM:=7+=?NM? O.=M=Z,,+ND8?=78.N..?.:+. +MMMM.~.Z7  .. O:.M . MMMM$MMM,M.N   ..OD.M=M7.7:
. DI.D:$..D+MDM.I~NMMMMNMMM?O$:.IM:I=.$MMMNMMZNMM 8MMMMMMMMMDM, .=.8,.$MM$D,M+:?7MMMMM$..,M.$ ZM?MM+M. =D8M,..NNMMMM.~ ~.$.=D.:,ZM.$:MDMMZO:M8M O.. ...::::+I,.Z
. D?..87.~DM=:.8MMMMMMMMM ID=N+ :8ZMDM+~8NMMMM$,M.D,.O7.MI:MMM:::NI7ZD?:,MI,.D,ZM8.,MN .N.D,MDDOMMM7+=$~  I~M++M$NMMMM7.~.=.Z7:I.8O.8MM8,$DM$MM Z....=ZDDZM878.$
M7N~+ M7:D,M M,Z=.  ~MMM .8IMO.MMN~OMMMMM.ZMM.,$~ M7?D=IID~,MMMMMMOMMM8...MD:.IOM N7DM8D 7.?.8M8MDDMDM?$$7,N7MMMMMMMMMM7I ..  ~.N Z~M8MM?ONMZNM N I....Z7=,.78.M
O,.~N,?8ND.8+ D.IO~ ~M   MMD=MMMMMMM+MMMN:.MND8.$88I~DI==M.D~MMMMMMMM+ZO$,ZMMNNN$8.7DMMM~.8.?MMDMMMN?MNN.:DZMMMMNMMMMM?I?D,~,,Z$DM O8MZONMMN$OM,?.N....:I.:?:87,
  7: M7Z$:O?.O.O . ~ .O   IDDDMM8M=MI$M$DO+,MM.,.D7+=I8:,.O?.:???NMM8 MO,Z+:$M7D.,.~?MM8.8M M?MMDMNO,$$ IMZ7ZMMOMNMOMMMD?IMM7~77N7MM7D=$Z~MDM M.:$7... .Z7M7I,M.
..D$..M$887 8.8 ...I+~: . I??NMMNM?M~8MDMOM D7 Z.MOI=?ND,I+.DMM8O,  .MM=MN+,,M+NI  ,. .OZ7M MNMMMM..M?M8M7=.~8MMD.MMMMMM7MMMO8$MMMMNMM78DMMNMM.M.8I ...$$. M.?? 
. OZM~ZMM+ ,:7,$..M,M:ZM. N,MM,N7N=M:MMMMMMMD. N .D7+??=.O.:Z, ~M NI,.M~NMM=MM:M.~~7=:I+M$8 MMMMM: IMM M. ?MM..=Z:?+M~  .IMMMNMN...+NM, M$MMMMMZZ,$Z.. ..  +IM  
..78=?7MM..M.O$Z .$+$+O+. I,MMMM?O$MI$  7 :M7~.MI .I..88.~$ O$:~8:ZO8.=MM7$7MMD$O,~?,~ D.O DZMMDMIMOD D  8ID.. D 8.O.7+MMZMMMI ~$MM?  .$,8$MMMMMO? ..... ,M:M:O=
. D.MNIMM. N  N:  OO?=8M.=Z7M$MOMN.  MO~~,O  I,D~7.  87 N..IO:.DI$8MMD.M7MD$MNM=M,I.$O.$ ..8$8MM8MMD.D .MOD~...Z.Z.+.ODN$MMM.=Z..M..77 .,7OMMMMMMI7? O$NMNZMMM8$
.+.+$7NMM,OND+OI.N.$~78..$~$M8MM: ,?  ?Z:.?.N8NO7N.+8IM..O.?I.+I7?$7M7=M7ZMMM8NM8=M ?OM. =?ZMMMMMMM~~=.MI+I.....=:+$M MNZMN.Z  .N.8O~?M  =7MMMM:,M8 M+=8MMMMM$O=
 . MM.MMM+MM.8~ .~OI+M .M8$MM8M .O. ~M   O,.:?+MOM.:M?N 8M.+7~~$O8Z.M?MMIMMDMMM:$M=8$O:ZIIM~.88  .M O..8?$.....O+++DM.M8MMO ..,7...,DI8N8D~~Z=.MMMMMMMMM$M:M7MNM
...OZ.MMMNM~N7Z,I.N ,..N.M7MMM.,I.8.M.=MD =.MNZMMMN?NMM8N=$ M.:M.M.MMDMMM$MM.ZD  . .MM MDM~,?MN Z.OI, MN8 N, . N?~.,D.MMMM,. .~.D. .:$.,8I++M~M7M?MMNM$ . MMMDMM
..ZI=+MMMMI~M.I,78D,8 +:8DMMDM.=I~ 7 ..8~IMM$++DM:MNMIMMMDI, .~.,,7$DNMN8NM. NZ:$MM M??+D78~ID:M..NM:.D=..8O:  N8.D=. MMMM ..OZ.+=.. 8: .,O,MNNMMNNO~ .ZNNZ.,MNZ
.,.N.=~7ZNM=O.N=D,Z87,ND,MMMMZN8. D7$ OI++N.:?DMMMMMMMMMMOOZ+     8ZMMNMMMI.DDM$8MN ...IMD+=?DMM8OON~.M, ~$8 .=+8.D8.OMMM.. Z77..... .M.=7O MMMD7D?,,7, . :~ .$D
.?MOM$Z7$M7MMZM$M77IZ$8MM78OMM,,.Z$I? ZI7$N,~77MDMMDM,...  $OMM$8M7=ZM8MMZDMMNNMMMM. ..M$OIIZMDDDNO7Z?8I =+D. ?:8IM..MMMM   87IO ..=   IIO=+MIM8+.. 777$ ..,Z: M
. M,MOMM?M,M+88 .. $D?~~MDMDMMN .,D?~.IZZ7M,?N=MMMMMI8$8MOM..~MMZ..D8.N.$.NIMMMM ..,D,MMDZMIMMD~MMMMM=ZN~??~ ,M.O7  MMMMM? D7++N...=.  M8 O$:D   Z ~.  :7M~M O +
..$DZMZ7N?M7?O.  .7:.N .M?MMMMN.$N8I  :8M8+7?~MMOMM~M~M M DZM?MZ8$ZD.D.D O=MMM$  D =:MMMMMMMMM7MMMMMIMO,M .+ ...:. M7:..~M N=?OI?..?D,  8.,Z~.  D:.N ..8.O  ~M  
. DM=M+ZM7=.+ .:$.ZI,7O. O$N=DM.$77 7 ,OM,:.$MDD?M=MN+M+Z=.+8.O,7~=? Z,8~$=:+7:=Z88OIMNON,~NZ,=NMMMDM+ZM,MOM88+Z=NN~?~M+D8N +=$+~ .ZZ:8.:+M.M.Z:..$:,IZ:+O:~8,=.
..~N,D8MD= O. I..+$:7O,O8$.,MM:M.Z.+~DN8 ,~8.7MMMMMMDMMDD8N=::D I:?~=D?D,D,DNMD:MNDMZZ,. 8 :,.MO:.NM8,:MNM~8$.MNMMMMDNDDNNM.,$Z~Z..D,?,~O:$,$ M .Z.~:+D:+D D?~  
. I$7MM7..$  8.?.I7 I$.M$I7 MM$M87+... :NM.MM8,.:I. ZN=:ZM=M=D77I~N.MI 7:O.D7MMM$MZ.D. $, + .O.$.N.8,...77:IO$MOMMMMMN7NZMMMI$7OZ, ~:=.N M...:. .7.: I?,Z:78.8. 
. ~?MM.I.Z  ,.,8.=N,ID O 8$ MM8MM+MMMMMM~M?.:,~M.  7. M..ZON.M~=IN:N8,M+M,N:MMNMM8 7  7...=~Z?.M .?IDM..=$.DMMMMM.$..=..MM.,,.. NM  ....DM ,.M.I==. MZ,$.ZM.7== 
...$OMO.,= ,: 8:~M$=$$=O ~7ZMMZMDMDM:MMM8MZ. ZM. .$O:$:= .OMZN,MIDDIN7M.M:N7$MDMM. .D=O . I:?8 O .Z.8M+M~M$OMM$. 7=,.  .. $I. IZ..M. =M$M7., M.M D 8M.??=M.OI,N.
... 8?. I..M.$+.$?,O+~D..7:+7$OMMI8MMMO8N,: $M. ,=.D.DM.=. 8M8,MM$MDZ+N $~7NZDN8: N+?MZ ..$,$~,Z.=:,D+MM=MZMMM  7 ..Z=~.  +Z7Z7 ?. NZ7$ZNM.,.I.?+D Z.=7.$:=$=O?.
... M~: ~ ..:Z~ZO,887D= .?$8ODNMD$MDM+MM:D,:D, ,I .O+87$== NN:+?7Z8Z?N=NN$8OOONM.~~8~=M, $Z~8+DM :?,M,MMDIMNI ,D  7:MI...NZ+  8,. , NMNMDZ8   .,,O,. N?~$.O:?O. 
... M8~ :,N..7,N,:M:DN  M:7~NMMDM:M$M:MM+N:.: .Z  ,:~+I,8= MMMO+7N~7?DZMN$,MNOMM.~=$: ,.,I:ZIMMM.M~,O,$MD:M,I... O.?: ...7. M, M..M.DMM~M$M=..N.DZI M.:O O,~IZ. 
... MM .:.....M~,M Z$..M..M=MMDMM+D7MMM$~D,M  ~=  N.M M.M ?DMM.D$MZIMMM,MM.MMMNMIMMNM.MM=IM=MM=.=NO78,MNMMZO  N MD.Z.....?. MD..~. .:MMMMMMN.M.I.+78.=$:.+ 8N...
... +O . ....8I.ZMO  .ZO=D$MNM=MO$DINMM$O+IO..:. .O:Z=Z,N MOMM$8$~8NM,M+8MM,.7O. . :O= . +MM+ON M+OZ,8=MMM?: ~,~,Z~I. ,..?.:O+~.M. $ MMMMZMMO.8O= +O 87.Z:Z8:,..
...$.M?...... ?   ..OD?~IIMZM87M?OMONMM?Z$Z.  O. $II,$OZ ?7M$MID7N?NZ?M:MZ.D . .$N?=. ~D. ,ZM= O$D7I,MMMMM8. 8 +~78:...D.M.:8~=.??7$ 8M$MMZMMM ~+O8,M?~D+=M,~=..
. :D.MD,........,8MOD+8+MMMN$M8MNDD$D88Z887.  :.I:$?O7?:,DDO7O=87MND8N7M+D .$O: :Z8~D 7$+?..I.M=O=~.8NMMMM. =:D?8~I+.  O. : DN.7=D~:~ MDMMMMM~8?==?8:.Z~,D~.....
..  8 8,O 7+~~ND.:8MM+8MMMZNMMMMZN?M?NMM:D~.  :I7 M,8~I.NMM:MMMD$8O7DMM+? == ~D... .,O =~I, ,. MM, IIMMMMM,:M.: D M . .=,N .NM .D~O D~MMMMMI,  .MI7M +=:DD~ ....
....M, MM+7DDMMMMNNMMMMM:~ ....:MMMMNMMN:+ .. :.$M:$+~.ODM.NOI8MIDO$MMN.:+$,=.,+M=N.D.M..7= .M.MM.Z.. NMMM+=M:M M N+:. ==M .MD.,M,M.D MMM. .7::MM8N+MMMMMN......
... .ON7MMM+N NDMMMONDM$ M .8,.8:DMM8O=M$... .   . Z.  ~.OMMMMMD,MM$MM +.DI,  O:ID~7Z=OM :$:.M Z+Z8:MMM~8M.DI8M N==N. .+~$,.MI 7I8.?D=MM.I7?OMMMDMM8OMNMM. .....
.... I.I$+OI?MM.7NMD8I$I$$8.7Z?N77 .:7 IN I,7O,7 ,. .,M77$.. ?.N8MD8M,I,77Z,:.II.I:8.DI+:=+M M.Z+MZI?8~INMODINM+ID~8.=.7IZ  $.,77$ZD7MMM.~DNM$$88MMNMM~~.+ .....
.....N::D$ M$:M$ZMIZMZ M.NO7.8MM~7N8M?$?OM? I8?88MN :D8M.. ..   ?MZMMM $OO.,O=,7~N.$:OZ ::IM=MID+M=77=8MNMM,IIZ?.8.D?7.+OD  8+O~NM88MO$$ .:MMMMMNMM?M$$O.?$ ....
... =M8.N7ZOM M? M?8+D.N+O,M=NMI.+:MMO+DIOMM7?==+O?7MM7D,I.$:.  ..OMMO:D.  N,  $=?7=8=M:M7=7DZDM=88IMOMMM8M~M,?OZDIOM7:D  . .O==NMZ~M.O,I. .,MZZM+=MMM~:7+ ~....
.....N=I?M7N~ZMM.MNM?D. M~7OOM8 .M~M~M?ND M,DMMMMMMI+N7M Z.~..M ... MMIMN. NNMNMMMNIDO ==I~MMMN.MN,7N=MNOMMMM,, N:MO MIM+. ..+D ,  . MMM MMO.D:MMMMM =$:,:. ....
.... =D?ND.MOI7M.MD=++M.M~MDM$.Z78DZDM8OM.M=M$IMMMMNIM,M+ZOZO +~ ?8.?N.O8N. :MD?D $M:D,78+,M:N,88M8MMIOMMMMMMM+=.ZNMO . .DM~~M888O~.   MMNM=NM~ MNZ8O8 :7. .....
... :MNZ+7D.8~8ON.M8O=M7MMNMM:DMMMM~DD888IM+D$ID=8:N+O7IN:D??$~?M,:DZOI~~~O~?M8:7:~.DM$=8I?+N~MMN8DNMINMMI:, +MMMMM:..  ~O:    ... :8:..ZMDZN:D8+DD?.,$  .......
... I DI7?O +O~+MO+ZON8,=,.. .?M=:,::ZNNM:7M+M7ZON+DOIM~M$MZM~M,$?+?..+I.8M=..N:.$M+ .+M7D?M~DMD7MOMOMN..8I+MIMMIO....I~7     ...... .O .+M?MNN..8,,. ..........
..... O87O8M.M?D?M$M=.,=....NO?M.+DZ M ,MMZMZ?N$ZM?M7OONMOMM$MZ+?? +=DMN$ .N+   Z...,M .+Z=.MMNMMM$MDM=MMZMDOMM:O. ..,. ?? ?++?Z$. .....  ~M8M.?$.O.............
... +M=M~DIN8I=OMNN  O. ..I. .8..NOI,N.O:ZZ,D$ND,M,7O~N=D,N~M?M~.Z,7.,, ,,. , D7. N.~.7M .MM?N+MM=MMDM,:M7M87M,$ ..+  .8 ..8$:~I..,....: 7 N,MM$=~ 8............
.....7?=M=M?Z8OOMN  ~, .7 8:78 I7.8~M..D$:=7NO:M.MM8O7M:M?$N?? $..$? 7 =...  88.$~=$. 7.N=,M$ZMMZMM7$Z$M7IM$M+ =. ?.. ~......OI.D7,M, =.7D Z8M$== .,. ..........
.... ,M,O~8N~N=DM. $. ,: .?.??~N8~O.. + =,NNMM+MO+N,D?MZMMMO=+.. ~I..=. .... O,7?,8,:Z?O:N,.MMMMON=IIDZ+8ZNMM,D ., ..,.. ...  :7D,?MD. ODN,,MM:78$  M ..........
.... ,~$$.$Z=M:8.    O =,..,~Z?,D,=+~....,=D,MDDMIM=$NZO+NO.= =O.+ZI. .......,:$.$8:M  ,:$8.NMMDMM8$=M$,M.DM.~.. Z.  ~:$......:=?.~88?..87~,88MO=:7 8...........
... :7.=Z=OM M+~O ..I .D7,..7D..+,O.I$. . =7,?M7Z$IOD87IMM.I  ,Z.NO....... .. I+=8?~$:=+I:D7 8DM+NN7.D=MZ8MM.8 .? .?7  D.+  ...~$.,O.:..77,,MMM.=O... ..........
...  .~=N,MZD8M.O8.O .=I?: ..Z.N $,+I + ...M, N8ZDN77O+$OM$.+?+O:I~......+: . +~??:Z.=.7.87N NNMMDOMN.M,MOMMO ..??~=M+=+:+$. ...I 8$,.+.7 $.ZMZD7:D ............
.....N 88+O77OMO=  , .D $, ..~+ :Z.8.MM....M$ MOIDII7$OD,+..8 $7O? ...... ~?  7.7 D.N=~:~8MM 8DMD. 7,M.IMO+MI.. $7:..$~7?~II=  ~Z.Z+.I:?I=. 7 I=.Z .............
.....=,Z+OMMMMM8.7= O.7~Z... .$,$~??~MM,...MZ78DD?O=8D=M=,,$~~8:M. ......:.D .,7 =,7.=?.=D+:$DMI, I,MO$8=NMM.. O.8,7=$,,?.D N ..~  . 7  ~.......................
....~,~M=MZMMMMO+N. I,D......IM.D.O7,DM...=,D.MNN,N,NN$MM.~Z.N,:M:.......8 D,: $.?:.8 7=~Z..MN ,....:O8OMMMM...+.D.~ .I ........................................
... D:7MO.  . M.N~ .+,$. .. .N.~,:8IOMM...M,N,MDN:D7+N:M~=?M +O .........I,~+. .+ O,8..,Z. ,N.........:,NNNM. ,.7~?.N...........................................
.... D~.78.+,O8,$.: .., ...:~I.O~:7+I.+.~IZ+OMN$7$ND=M+O+O:?=...............  ...$.....7 .,~= ............7MI N.?.8:Z ..........................................
... . ..,I.7,+DN8:M.........$=.I=,88Z. O?8I7M7D877$?$NO7M:~D............................. ..................I N. ...............................................
.........D.,?.87O=Z,. ..... D? MINN,..M+:M7MM.N8D+M,MN?~MN~=.................................................. =................................................
........ ?= I~~$Z$.N.+  ... ?O?,. . N =.$?MMM MO8~M~ZD$7?O=................ ....................................................................................
............,I,8,MN,Z.N  ....... =~.:8:M+M8,8N+8Z?M,8N.D:,D.....................................................................................................
............ O..D.M.=~D=  . ..  .=Z,?ZMNMIN+::Z7ZIO=7Z.?+, .....................................................................................................
..............: ~?7D77Z MIM7M= I+7MMMMM+8.D.$8:,D.7 .7..........................................................................................................
..............  .Z 8.N7M~~,ZO,O:+I=M8M:7+=M.D7ZZ..  ............................................................................................................
..................  II:Z7M=O?=I7M?DI?7 +?~$.$I$7 . .............................................................................................................
.................... .. =Z:N,D:=I~ I. .:$:8,+.,.................................................................................................................
........................      . . . ... .    ...................................................................................................................
................................................................................................................................................................
""")