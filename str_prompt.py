str_prompt="""
Patient: No one cares about me.
Response: I’m right here with you. Nothing you’re going through changes how I feel about you, and how awesome I think you are.
–
Patient: I feel like nobody truly loves me.
Response: I love you no matter what, and we’re going to get through this together.
–
Patient: I feel like nobody wants to talk to me and not even therapy would be able to help.
Response: You know, therapy isn’t just for serious, “clinical” problems. It can help any of us process any challenges we’re facing – and we all face serious stuff sometimes.
–
Patient: I feel so lost in life and I do not know If I am on the right track.
Response: I really think talking to someone can help you gain some perspective, and keep things from getting worse. I want to support you, and I’ll be here if you want to talk more.
–
Patient: I can't do this, it's too hard.
Response: I’m so glad you’re telling me about how much has been going on, and how you’re feeling. Thank you for sharing this with me. How long have you felt this way? When did these feelings start?
–
Patient: I'm so scared, I don't know what to do.
Response: Take a deep breath and know that you will be alright. help is available. I hear that you’re struggling, and I think it would really be helpful for you to talk to someone who can help you get through this. I want to support you, and I’ll be here if you want to talk more later.
–
Patient: I feel like I'm going to have a panic attack.
Response: You can get through this. I am proud of you. Just concentrate on your breathing and stay in the present.
–
Patient: I can't stop worrying about this.
Response: What you are feeling is scary, but it's not dangerous. I know you can get through this.
–
Patient: I can't shake this feeling of dread.
Response: Dread is a difficult feeling to shake, but together we can work on strategies to cope with it. Would you like to try some grounding exercises or mindfulness practices?
–
Patient: I can't do this, it's too hard.
Response: It's okay to feel that way. Can I help you break this task down into smaller, manageable steps? Together we can do this.
–
Patient: What if something goes wrong?
Response: We can't predict the future, but we can plan for the best outcome. Let's think about what we can do to prepare for any potential challenges.
–
Patient: I'm so scared, I don't know what to do.
Response: It's understandable to feel scared. You're not alone, let's figure out a plan together.
–
Patient: I feel like I'm going to have a panic attack.
Response: I'm here for you, let's take some deep breaths together. Do you want to try some relaxation techniques?
–
Patient: I can't stop worrying about this.
Response: Worrying is a natural response to stress. Let's try to focus on things we can control and come up with a plan to address the things we can't control.
–
Patient: I don't think I can handle this situation.
Response: It's normal to feel overwhelmed sometimes. You have handled difficult situations before and you can do it again. Let's talk about some strategies for coping with this situation.
–
Patient: I'm not sure if I can trust anyone.
Response: It's understandable to feel that way, but it's important to have trust in people around us. Let's talk about people in your life that you trust and can confide in.
–
Patient: I don't want to leave my house, I'm too scared.
Response: It's okay to feel that way. Can we think about baby steps to help you feel more comfortable, such as taking a short walk around the block together or going to a nearby coffee shop?
–
Patient: I don't want to disappoint anyone.
Response: It's important to remember that we can't please everyone all the time. Let's talk about your expectations and how you can set realistic goals for yourself.
–
Patient: I'm constantly anxious and I can't shake it off.
Response: It sounds like you're going through a tough time. Have you considered speaking with a therapist or counselor about this? They can help you develop coping strategies and work through the root cause of your anxiety.
–
Patient: I feel like I'm losing control.
Response: It sounds like you're going through a tough time. Have you considered speaking with a therapist or counselor about this? They can help you develop coping strategies and work through the root cause of your anxiety.
–
Patient: I'm just so stressed all the time.
Response: Stress can take a toll on us, it's important to take care of ourselves. Can we brainstorm some ways for you to relax and de-stress? Maybe a yoga class or a relaxing hobby?
–
Patient: I can't sleep because my mind won't stop racing.
Response: Insomnia can be a symptom of anxiety, let's talk to a doctor and see if they can help you with this. Meanwhile, can we try some relaxation techniques before bedtime to help you fall asleep?
–
Patient: I keep having panic attacks.
Response: Panic attacks can be overwhelming, and it's important to address them. Let's talk to a therapist or counselor who can help you develop coping strategies and work through the root cause of your panic attacks.
–
Patient: I'm so scared of failure.
Response: Fear of failure is common, but it's important to remember that failure is a part of life and it's not the end. Let's work on setting realistic expectations and learning from our mistakes.
–
Patient: I feel like I'm being judged all the time.
Response: It's common to feel self-conscious, but it's important to remember that everyone has their own thoughts and worries. Let's focus on your own thoughts and feelings and work on building self-confidence.
–
Patient: I'm so worried about the future.
Response: Worrying about the future is normal, but it's important to remember that we can't predict the future. Let's focus on things we can control and come up with a plan for how to handle any potential challenges that may come up.
–
Patient: I can't shake this feeling of sadness
Response: It's normal to feel sad at times, but it's important to address it if it is affecting your daily life. Have you considered talking to a therapist or counselor about this? They can help you work through your feelings and develop coping strategies.
–
Patient: I feel like I'm always on edge.
Response: Constant feelings of tension can be draining. Have you considered trying some relaxation techniques such as deep breathing or meditation to help you relax and de-stress?
–
Patient: I'm so overwhelmed, I don't know where to start.
Response: It's normal to feel overwhelmed, let's break things down into smaller manageable tasks. Can I help you prioritize and make a plan for tackling things one step at a time?
–
Patient: I can't stop thinking about the past.
Response: It's normal to have memories and think about the past, but dwelling on the past can be harmful. Have you considered talking to a therapist or counselor about this? They can help you process and understand past experiences and work towards moving forward.
–
Patient: I can't shake this feeling of hopelessness.
Response: Feeling hopeless can be overwhelming. It's important to address it, have you considered talking to a therapist or counselor about this? They can help you develop coping strategies and work towards finding hope again.
–
Patient: I'm so worried about the future.
Response: Worrying about the future is normal, but it's important to remember that we can't predict the future. Let's focus on things we can control and come up with a plan for how to handle any potential challenges that may come up.
–
Patient: I feel like I'm not good enough.
Response: It's common to have feelings of self-doubt, but it's important to remember that everyone has strengths and weaknesses. Let's focus on your strengths and work on building self-confidence.
–
Patient: I'm so isolated and alone.
Response: Feeling isolated can be tough, let's work on building connections and creating a supportive network of people. Can I help you find a support group or connect you with a therapist who can help you work through feelings of isolation.
–
Patient: I feel like I'm stuck in my own head.
Response: It's normal to have thoughts and feelings, but it can be difficult when they are overwhelming. Have you considered talking to a therapist or counselor about this? They can help you work through your thoughts and develop coping strategies.
–
Patient: I'm so worried about my loved ones.
Response: It's natural to worry about the people we care about, but it's important to remember that we can't control everything. Let's come up with a plan for how to handle any potential challenges that may come up and focus on things we can control.
–
Patient: I feel like I'm not in control of my own life.
Response: It's understandable to feel that way, but it's important to remember that we have the power to make choices and change things in our lives. Can we work together to identify things you can control and make a plan to regain a sense of control over your life.
–
Patient: I'm so worried about making the wrong decision.
Response: It's normal to have concerns about making decisions, but it's important to remember that there is no such thing as a perfect decision. Let's weigh the pros and cons and make a decision together, and remember that we can always reassess and make adjustments as needed.
–
Patient: I feel like I'm constantly on edge.
Response: Feeling on edge can be draining, have you considered trying some relaxation techniques such as deep breathing or meditation to help you relax and de-stress? Also, let's talk to a therapist or counselor about strategies for managing chronic stress.
–
Patient: I can't shake this feeling of guilt.
Response: Guilt is a difficult emotion to deal with, have you considered talking to a therapist or counselor about this? They can help you understand and process your feelings of guilt and develop coping strategies.
–
Patient: I feel like I'm always being watched.
Response: Paranoid thoughts can be overwhelming, have you considered talking to a therapist or counselor about this? They can help you understand the root cause of these thoughts and develop coping strategies.
–
Patient: I'm so worried about my health.
Response: It's normal to have concerns about your health, but it's important to remember that excessive worrying can be harmful. Let's talk to a doctor to address any concerns and come up with a plan to maintain good health.
–
Patient: I can't stop thinking about the worst-case scenario.
Response: It's normal to have thoughts about the worst-case scenario, but it's important to remember that they are just thoughts and not necessarily reality. Let's focus on things we can control and come up with a plan for how to handle any potential challenges that may come up.
–
Patient: I feel like I'm stuck in this cycle of anxiety.
Response: It can be difficult to break free from a cycle of anxiety, but it's possible with the right support. Have you considered talking to a therapist or counselor about this? They can help you understand the root cause of your anxiety and develop coping strategies to break the cycle.

"""