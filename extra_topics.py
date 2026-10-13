"""Thirty additional original preschool lesson themes using existing safe visuals."""
import random

EXTRA_TOPICS = ["alphabet","numbers","animals","farm","ocean","space","weather","seasons","fruits","vegetables","vehicles","dinosaurs","insects","birds","flowers","trees","opposites","emotions","body","senses","music","instruments","sports","food","clothes","bedtime","morning","friendship","safety","nature"]
LESSONS = {"alphabet":["Alphabet Adventure","letters of the alphabet","shape",["circle","triangle","square","heart","oval"]],"numbers":["Number Explorers","numbers one to five","count",["stars"]],"animals":["Animal Friends","animal friends","shape",["circle","heart","oval","triangle","square"]],"farm":["Farmyard Fun","farm animals","count",["apples"]],"ocean":["Ocean Adventure","underwater wonders","shape",["oval","heart","circle","triangle","square"]],"space":["Space Explorers","stars and planets","count",["stars"]],"weather":["Weather Watch","sunshine and rainy days","color",["yellow","blue","purple","green","red"]],"seasons":["Four Seasons","the changing seasons","color",["green","yellow","red","blue","purple"]],"fruits":["Fruit Basket","colorful fruits","count",["apples"]],"vegetables":["Veggie Garden","healthy vegetables","color",["green","red","yellow","purple","blue"]],"vehicles":["Things That Go","vehicles and travel","shape",["circle","square","triangle","oval","heart"]],"dinosaurs":["Dinosaur Discovery","friendly dinosaurs","count",["stars"]],"insects":["Little Bugs","tiny garden insects","count",["butterflies"]],"birds":["Birdwatching","feathered friends","count",["butterflies"]],"flowers":["Flower Garden","beautiful flowers","color",["purple","yellow","red","blue","green"]],"trees":["Forest Friends","trees and leaves","color",["green","red","yellow","purple","blue"]],"opposites":["Opposites Day","big and small and other opposites","shape",["circle","square","oval","heart","triangle"]],"emotions":["Feelings Friends","happy, sad, calm, excited, and proud feelings","shape",["heart","circle","oval","square","triangle"]],"body":["My Amazing Body","hands, feet, eyes, ears, and nose","shape",["circle","oval","heart","square","triangle"]],"senses":["Five Senses","seeing, hearing, smelling, tasting, and touching","count",["stars"]],"music":["Music Time","rhythm and melodies","count",["stars"]],"instruments":["Instrument Parade","musical instruments","shape",["circle","triangle","square","oval","heart"]],"sports":["Let's Move","playful movement","count",["stars"]],"food":["Food Friends","different foods","count",["apples"]],"clothes":["Getting Dressed","clothes for every day","color",["red","blue","green","yellow","purple"]],"bedtime":["Sleepy Stars","a peaceful bedtime routine","count",["stars"]],"morning":["Good Morning","a cheerful morning routine","color",["yellow","blue","green","purple","red"]],"friendship":["Kindness Club","sharing and being kind","shape",["heart","circle","square","oval","triangle"]],"safety":["Stay Safe","everyday safety habits","color",["red","yellow","green","blue","purple"]],"nature":["Nature Walk","wonders of nature","count",["butterflies"]]}

def make_extra_story(topic, seed, Scene):
    rng = random.Random(seed)
    hero = rng.choice(("Bibi Bunny", "Pip Puppy", "Mimi Kitten", "Toto Bear"))
    landscape = rng.choice(("the Rainbow Meadow", "the Sunny Valley", "the Starry Garden"))
    title, subject, kind, items = LESSONS[topic]
    scenes = [Scene("intro", title.upper(), f"Hello! I'm {hero}. Today we will discover {subject} together. Are you ready?")]
    for i in range(5):
        item = items[i % len(items)]
        if kind == "count":
            focus = item
            speech = f"Let's count together! One, two, three, four, {i+1}! Look at our {subject}. Great counting!" if i == 4 else f"Let's count! We can see {i+1} {item}. Can you count with me? Great job!"
            scenes.append(Scene("count", f"{title.upper()} {i+1}", speech, focus, i+1))
        elif kind == "color":
            obj = {"red":"balloon","blue":"kite","yellow":"sun","purple":"flower","green":"leaf"}[item]
            scenes.append(Scene("color", f"{item.upper()} {obj.upper()}", f"Look at this {item} {obj}! Let's explore {subject}. Can you say {item}? Wonderful!", item, i))
        else:
            scenes.append(Scene("shape", item.upper(), f"Look at this {item}! Today we are learning about {subject}. Can you say {item}? Well done!", item, i))
    scenes.append(Scene("finish", "GREAT EXPLORING!", f"We learned about {subject} today! Thank you for exploring with me. See you next time!"))
    return hero, landscape, title, scenes
