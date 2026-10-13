import unittest
from factory import create_story, make_frame, make_short_frame, TOPICS

class CartoonTests(unittest.TestCase):
    def test_topic_catalog_size_and_uniqueness(self):
        from expanded_contexts import CONTEXTS
        from batch_shorts import plan_topics
        self.assertEqual(len(CONTEXTS), 150)
        self.assertEqual(len(TOPICS), 183)
        self.assertEqual(len(set(TOPICS)), len(TOPICS))
        for total in (10, 100):
            picks = plan_topics(total, 1502)
            self.assertEqual(len(picks), total)
            self.assertEqual(len(set(picks)), total)
            self.assertEqual(picks, plan_topics(total, 1502))

    def test_context_vocabulary_matches_headlines(self):
        from expanded_contexts import CONTEXTS
        for topic, (_, title, words) in CONTEXTS.items():
            self.assertEqual(len(words), 5, topic)
            self.assertEqual(len(set(words)), 5, topic)
            _, _, actual_title, scenes = create_story(topic, 1234)
            self.assertEqual(actual_title, title)
            self.assertEqual([s.focus for s in scenes[1:6]], list(words))
            self.assertTrue(all(s.kind == "context" for s in scenes[1:6]))


    def test_scripts_have_arcs_and_unique_foci(self):
        for topic in TOPICS:
            hero,location,title,scenes=create_story(topic,1502)
            self.assertEqual(len(scenes),7)
            self.assertEqual(scenes[0].kind,'intro')
            self.assertEqual(scenes[-1].kind,'finish')
            self.assertEqual(len({s.focus for s in scenes[1:6]}), 1 if scenes[1].kind == 'count' else 5)
            self.assertTrue(all(s.speech for s in scenes))
    def test_visuals(self):
        for topic in TOPICS:
            hero,_,_,scenes=create_story(topic,123)
            for s in scenes:
                img=make_frame(s,hero,0,0,123)
                self.assertEqual(img.size,(960,540))
                self.assertEqual(make_short_frame(s,hero,0,0,123).size,(720,1280))

if __name__=='__main__': unittest.main()
