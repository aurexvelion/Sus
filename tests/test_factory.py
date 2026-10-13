import unittest
from factory import create_story, make_frame, TOPICS

class CartoonTests(unittest.TestCase):
    def test_scripts_have_arcs_and_unique_foci(self):
        for topic in TOPICS:
            hero,location,title,scenes=create_story(topic,1502)
            self.assertEqual(len(scenes),7)
            self.assertEqual(scenes[0].kind,'intro')
            self.assertEqual(scenes[-1].kind,'finish')
            self.assertEqual(len({s.focus for s in scenes[1:6]}),5 if topic != 'counting' else 1)
            self.assertTrue(all(s.speech for s in scenes))
    def test_visuals(self):
        for topic in TOPICS:
            hero,_,_,scenes=create_story(topic,123)
            for s in scenes:
                img=make_frame(s,hero,0,0,123)
                self.assertEqual(img.size,(960,540))

if __name__=='__main__': unittest.main()
