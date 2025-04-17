# utils/joke_solver.py
from .base_solver import BaseSolver

class JokeSolver(BaseSolver):
    def handle(self, query: str, context: str = "") -> str:
        """
        Handle the joke queries to respond with a fun joke.
        """
        jokes = [
            "Student: Sir, can I go to the washroom?\nTeacher: You just went 5 minutes ago!\nStudent: Yes, but I forgot to wash my hands the first time. This is the sequel.",
            "Doctor: I have bad news and worse news.\nPatient: Give me the bad news first.\nDoctor: You have 24 hours to live.\nPatient: What could be worse than that?!\nDoctor: I forgot to tell you yesterday.",
            "Wife: I dreamed you bought me a diamond necklace.\nHusband: You’ll know what it means tonight.\nThat evening, the husband hands her a small package. Excited, she opens it...\nIt’s a book titled 'The Meaning of Dreams'.",
            "Ram: I joined a gym last month and still didn’t lose any weight.\nMohan: Did you go regularly?\nRam: Of course! I go there every morning...\nMohan: Wow, really?\nRam: Yes, I stand outside and drink chai from the tea stall next to it.",
            "Teacher: Why are you late?\nStudent: I saved a kid from getting hit by a car.\nTeacher: That’s heroic! How did you do it?\nStudent: I took the car keys from my dad before he could drive drunk.",
            "Boss: We’re like a family here.\nEmployee: Oh? Then I want to be the distant cousin who only visits on holidays and doesn’t do anything.",
            "Person1: I told my wife she was drawing her eyebrows too high.\nPerson2: What did she say?\nPerson1: Nothing. She just looked surprised for the rest of the day.",
            "Doctor: Your test results came in. You’re completely fine.\nPatient: Then why do I feel tired all the time?\nDoctor: Because you spend 10 hours scrolling Instagram and another 6 convincing yourself you'll sleep early tonight.",
            "Mother: Why are your eyes red?\nSon: I was crying because of homework.\nMother: Don’t lie! You’ve been playing video games all night!\nSon: Same difference.",
            "Teacher: If you fail the test, it’s not the end of the world.\nStudent: But it’s the end of Netflix, my phone, and possibly my social life.",
            "Friend1: Why are you looking so tired?\nFriend2: I stayed up all night thinking about why my crush liked my 2017 photo.\nFriend1: Maybe they're just scrolling back?\nFriend2: Or maybe they love me secretly!\nFriend1: Or maybe they were just bored.\nFriend2: That’s offensive.",
            "Boy: Can I copy your homework?\nGirl: No, do it yourself!\nBoy: I already copied your attitude. Now I just need your answers.",
            "Manager: We need to talk about your performance.\nEmployee: Do we also need to talk about my salary?\nManager: That wasn’t part of the plan.\nEmployee: Neither was overworking for free, but here we are.",
            "Teacher: Who can explain gravity?\nStudent: It’s simple. Anything that goes up must come down.\nTeacher: Okay, give an example.\nStudent: My grades.",
            "Wife: Did you fix the leaky faucet?\nHusband: I watched three YouTube videos and now the kitchen has a waterfall.",
            "Doctor: You need to reduce stress.\nPatient: So should I stop coming here?\nDoctor: You’ll stop permanently if you don’t listen.",
            "Girl: I hate my boss.\nFriend: Then quit.\nGirl: And miss out on gossip, free coffee, and 10 paid sick days? Never.",
            "Father: I see you on the phone all day. Do something productive!\nSon: I’m networking, Dad.\nFather: It looks like meme-working.",
            "Teacher: Read page 52.\nStudent: Can I read it mentally?\nTeacher: No. Use your voice.\nStudent: I lost it in the morning.\nTeacher: Then I’ll call your parents.\nStudent: My voice just came back.",
            "Mother: Why are your clothes on the floor?\nKid: Gravity.\nMother: And your books?\nKid: They’re keeping the clothes company.",
            "Friend1: Do you believe in love at first sight?\nFriend2: I believe in food at first bite.",
            "Boy: I think I failed my driving test.\nFriend: What happened?\nBoy: The instructor asked me to drive in reverse and I said, 'Why? Are we going back in time?'",
            "Boss: Why are you always late?\nEmployee: I believe in slow success.\nBoss: Then you’re on the right path.",
            "Son: Dad, why do I look like you?\nDad: Because your mom has great taste.",
            "Doctor: Do you smoke?\nPatient: Only when I’m on fire with rage.",
            "Husband: I cleaned the house.\nWife: You mean you moved the mess to one side?\nHusband: Same difference.",
            "Student: I need an extension.\nTeacher: On what?\nStudent: My will to study.",
            "Friend1: Let’s go to the gym!\nFriend2: Can’t. My bed needs me.",
            "Mom: Study for your exams!\nKid: I am studying... the art of patience.",
            "Teacher: What is the capital of Italy?\nStudent: I.\nTeacher: What?\nStudent: Capital ‘I’.",
            "Girl: My lipstick is expensive.\nBoy: Your attitude is free but costs a lot.",
            "Doctor: Are you allergic to anything?\nPatient: Yes. Mornings.",
            "Student: Can I skip class today?\nTeacher: Why?\nStudent: I need time to mentally prepare for being in class tomorrow.",
            "Ram: I started a new diet.\nMohan: What is it?\nRam: I just look at food and cry.",
            "Boss: Why are you sleeping?\nEmployee: My brain is in low-power mode.",
            "Mom: What did you learn today?\nKid: That asking questions leads to more homework.",
            "Wife: Do you remember what day it is today?\nHusband: Of course, it's Tuesday!\nWife: It’s our anniversary.\nHusband: That’s what I meant. It’s Love Tuesday!",
            "Student: I think I have a photographic memory.\nTeacher: That’s great!\nStudent: Yeah, but it never developed.",
            "Girl: What are you doing?\nBoy: Waiting for motivation to strike.\nGirl: You’ll be fossilized before that happens.",
            "Teacher: Explain the water cycle.\nStudent: Water falls, gets dirty, we pay for it, and drink it.",
            "Patient: Can I eat pizza?\nDoctor: Only if it’s imaginary.",
            "Friend1: Let’s make plans!\nFriend2: I already made one.\nFriend1: What?\nFriend2: Stay home and avoid humans.",
            "Kid: I want to be a millionaire.\nDad: Study hard.\nKid: I’ll just make memes instead.",
            "Teacher: Don’t talk during the test.\nStudent: I was talking to myself.\nTeacher: Then keep it to a whisper.",
            "Wife: The sink is leaking.\nHusband: That’s not a leak, that’s a water feature.",
            "Boss: What motivates you?\nEmployee: The fear of being broke.",
            "Girl: Let’s take a selfie.\nBoy: My face isn’t updated yet.",
            "Student: I need help with this equation.\nFriend: Just divide your problems and multiply your snacks.",
            "Mom: Why are you eating so fast?\nKid: I’m trying to outrun my feelings.",
            "Doctor: You should exercise.\nPatient: I do... my right to remain lazy.",
            "Teacher: Where’s your assignment?\nStudent: It committed suicide due to stress.",
            "Friend: You never call me.\nMe: That’s because I respect your phone battery.",
            "Boy: Will you marry me?\nGirl: Let me check my WiFi signal first.",
            "Dad: Why don’t you answer my calls?\nSon: I only accept calls from food delivery apps."
        ]

        
        # Pick a random joke
        import random
        return random.choice(jokes)
