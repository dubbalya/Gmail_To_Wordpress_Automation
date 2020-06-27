# Gmail_To_WordPress_Automation

Simple use case for this automation: I recently built a website for my mother to showcase her beautiful paintings to the world, but her tech savvy is limited. This automation eliminates her need to log into the WordPress dashboard and figure out how to draft a post, insert a featured image, and publish for public view. Instead, she can simply email her painting to me, along with a short description and the subject line as the title of the post, and a post will be automatically created for her!

This automation utilizes Al Sweigart's ezgmail module and the Wordpress REST API. This class allows users to email a Gmail address, read the email contents (limited to 200 characters per post), download the image provided (limited to one per email), and upload the Subject, Email Contents, and Image as a new WP post. Note that only unread messages from the email address(es) specified will be picked up. Messages will be marked as read after upload completion.

Note that you will need to use the Application Passwords plug-in to generate a Key for authentication. Be sure not to store this key in the production code. Up to three (3) email addresses can be inserted for the automation to "listen" for.

https://ezgmail.readthedocs.io/en/latest/

https://developer.wordpress.org/rest-api/

