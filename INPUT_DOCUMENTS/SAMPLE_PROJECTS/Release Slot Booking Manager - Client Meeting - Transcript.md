## **Release Slot Booking Manager \- Client Meeting \- 2026/07/10 10:31 IST \- Transcript**

# **Attendees**

Manoj Singh, Prabhjot Singh

# **Transcript**

Manoj Singh: as of now. Yes. Team was trying to change the requirement but he refused. No, we'll have to. So, let's start with the question. There are nine questions. Initially, the claw generated 26 questions out of which I think only nine are critical. So, this is a workshop. Okay. So don't mind take your mind help across we will ask you people to join that tell them we get because this is more like cross training also we will be recognizing everything it is not like everything will be notified but I don't

Manoj Singh: I want this to be this time everyone has to come out with something so that is my objective I'll ask you people or their people to come here or you people to go there explain them for 30 minutes strategy come back so that they can again come back to So as I said there were 26 questions then out of which nine are critical questions which I'm going to discuss. So first question is what exactly is the system roles for users let's say you have say release manager then super admin.

Manoj Singh: So there are two ways one for superm we can say SA release manager we can say RM. So is that good approach or do you want to define roles? I think let's make it dynamic. I don't want any UI to do that but let's permission driven roles. So let's define one role called engineering manager one is those are role we can create it right and just map it that in the database somewhere What is the permission of them right? So instead of I don't want to make it hardcoded because the dynamic is more UI but it has to be dynamic as a back end correct you just keep in the DB. So yeah now coming to the roles and all personas one is release manager one is engineering manager right one is product or someone business right and one is this guy and

Manoj Singh: Of course my team also. Next question is the unavailable slot blind to everyone including? No, we are discussing. So there are some queries.

Manoj Singh: So is the unavailable slot blind to everyone including release manager release manager will have the privilege to unavailable for let's be open for everyone it doesn't matter right so if it is unavailable so I just wanted to make it in future what we can do we can make it restrict right what release is going on right others it doesn't matter to them right so for now if

Manoj Singh: It is okay you make okay unavailable but release manager can have a information right can see who has the data and all right right so I think either it is open right doesn't matter let's say there are two project managers one is making the routine and I'm another project manager I can talk to him yeah just shift because I have some priority offline whatever right then he can shift for us other day right so let's be open doesn't matter it should be restricted the project information let's be understood So it is going to open for everyone. I'm I mean both the things. Okay. What are the exact start and end times or is it going to be So India business hours just consider around 10:00 a.m. to 10 to 8 or something. Right. So mostly the deployment slot will be starting from 5 to 9:00 a.m. Okay. And 5 in the evening.

Manoj Singh: No morning 5 to 8 two hours per slot and how many slots can be booked per day? I mean how many 5 to 7 7 to 9 accordingly you can imum two slot in a day maximum two slot but it depends right this guy football match is going on in night right India night right but Z5 is some of the audience they watch in day right so that depend right during this event you can request but the slot m Time period should be maximum two hours and it will be up to the admin to approve it And Minimum two releases. Minimum time 30 minutes 30 minutes or 1 hour.

### 00:05:00

Manoj Singh: But how does it matter because only the point is if it is extending beyond the time maybe some issue or role maybe they can that's a good point yes okay next question this is not making sense to me so I'll skip this describes three mandatory documents but the enforcement rule says both files both check boxes is it two or three uploads or how many check boxes should Total three. One is release Second is steps. What steps deops will exute. Right.

Manoj Singh: And third was can you open the document? Any other go down? Yeah, it's not QA em no document upload deployment step and hand over to devops. hand over right hand over. Okay. Yeah.

Manoj Singh: Any Three more question but we'll discuss that later. if the designated approver is not available, is there a backup delegate mechanism? The release manager will coordinate over email and he has ultimately rights to do that. On rejection, must the entire request be deleted or restarted from the scratch or once it is rejected there should be some reason, right? The release manager should cancel Release manager should be able to delete this slot, right?

Manoj Singh: For example, QA sign off is not there or engineering manager say no no we are not going today I mean there's no confidence on the team or whatever right so they can reject end of the day release manager can delete it release manager has all the rights to do that right and even if let's say one team has said okay they are available another is saying no we're not available then also the deployment won't but mostly I mean it doesn't happen because this is pre-cheduled right the ops engineer x name this guy will come and execute it because deployment is nothing.

Manoj Singh: It is not very straightforward because this guy should know the steps access rights whatever if they are deploying onto Azure there should be repo access there should be DB access all of them is required right before making anything right so it is needed and the same person should be there so I think question is confirmation not supposed to be required for every single person if approved the slot then I think that is release manager right release manager offline

Manoj Singh: they will do see right now they are doing 100% manual right now by the system they should be able to save 90% of time right 10% coordination that might be needed right right otherwise one team will say they're available and another say but no it is not 100% replacement of release manager it is just offload is work right nice right nice so 90% if we can make it automated then we are good okay one more question what do you want to develop web or

Manoj Singh: mobile doesn't matter to me any of I mention either web or mobile whatever compatibility means both au authentication mechanism should be there we have considered simple user ID and password it's like email id and password do email id password only do email ID password no issues token token I mean there are two questions one is ad or just normal that also I'm saying okay I mean which is okay username password is okay for

Manoj Singh: I have a question right do you want to ask that but idle requirement is maybe in future we should have edict because it should be authenticated within ecosystem maybe there are vendors but vendors can be onboarded right Indigo right Kelton is vendor right but let's say Kelton project project manager is raising request for production deployment right so they can be onboarded onto their ecosystem right exactly but I mean to be frank SSO is needed but for now if you wanted to go

### 00:10:00

Manoj Singh: with email address password which is I think if time permits we can try with the SSO also right so last time we were trying to add SS you didn't problem authenticator I know that anyway so I was having two questions one is key should we give any option to the PM or any team to cancel their reports cancel their slot yes of course we can right and for proper

Manoj Singh: There's a proper reason why we are canceling our just box whatever comment or whatever they wanted to and second was question that is saying three checklist should be there which is release notes deployment steps and hand over to DevOps. So the hand over to DevOps availability that will be offline or there will be a slot for devops.

Manoj Singh: that is a offline meeting between S devOps and all right so that is what the check box where okay hand head over is done that's all that is offline thinguling meeting who is available who is not available who will be part of that that is offline so there is a team right one person represent S they will be part of it they will ask lot of questions to technical team why we are doing how we are doing what are the new infra we are provisioning for this particular deployment is it are already there or not whatever Monitoring what should we monitor and during that window as well they do monitor okay if there is deviation in the API response time or something is failing or whatever right they do check all the progress is nothing nowhere there in only the fruit of sources PM who is going to providing that checklist that's it right basically this

Manoj Singh: This is K of release manager actually not project manager coordination can be done by project manager but end of the day release manager will make sure okay this is done then only they will provide final confirmation otherwise they will not but release manager doesn't have any further information that the maximum they are in the offline scheduled meeting release manager is part of it there is in the checklist as well they can say okay this There is a steps right? Mhm. So handover is needed is important Handover is also offline. Maybe whatever right we'll share the meeting with Thank you. recording is

### Meeting ended after 00:13:05 👋

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*

