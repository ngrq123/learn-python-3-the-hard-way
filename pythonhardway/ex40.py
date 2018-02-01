class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def destroy(self):
        self.lyrics = []

happy_bday = Song(["Happy Birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

call_me_maybe_lyrics = ["I threw a wish in the well",
                        "Don't ask me I'll never tell",
                        "Blah Blah"]
call_me_maybe = Song(call_me_maybe_lyrics)

call_me_maybe.sing_me_a_song()
call_me_maybe.destroy()
call_me_maybe.sing_me_a_song()
