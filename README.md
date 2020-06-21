# Gmail_To_WordPress_Automation

Simple use case for this automation: I recently built a website for my mother to showcase her beautiful paintings to th world, but her tech savvy is limited. This automation eliminates her need to log into the WordPress dashboard and figure out how to draft a post, insert a featured image, and upload. Instead, she can simply email me with her painting, along with a short description, and a post will be automatically created for her!

This simple automation utilizes Al Sweigart's ezgmail module and the Wordpress REST API. This class allows users to email a gmail address, read the email contents, download the image provided (limited to one per email), and upload the Subject, Email Contents, and Image as a new WP post.

Note that you will need to use the Application Passwords plug-in to generate a Key for authentication. Be sure not to store this key in the production code! Up to three (3) email addresses can be inserted for the automation to "listen" for. 

