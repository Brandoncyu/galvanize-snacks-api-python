from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models.snacks import SnacksModel
from models.reviews import ReviewsModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

db.session.add_all([
    SnacksModel("Pork Rinds", "Mauris lacinia sapien quis libero. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis.", 8, "https://az808821.vo.msecnd.net/content/images/thumbs/0000398_salt-pepper-pork-rinds-2-oz_560.jpeg", True),
    SnacksModel("Soup - Campbells Beef Noodle", "Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Etiam vel augue. Vestibulum rutrum rutrum neque.", 26, "https://images-na.ssl-images-amazon.com/images/I/71MavWF1P9L._SY550_.jpg", False),
    SnacksModel("Pie Filling - Cherry", "Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Fusce posuere felis sed lacus.", 3, "http://wickedgoodkitchen.com/wp-content/uploads/2018/06/Mom%E2%80%99s-Homemade-Tart-Cherry-Pie-Filling.png", False),
    SnacksModel("Chicken - Chicken Phyllo", "Donec vitae nisi. Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla.", 5, "https://tmbidigitalassetsazure.blob.core.windows.net/secure/RMS/attachments/37/1200x1200/exps191978_SD163575C10_07_6b.jpg", True),
    SnacksModel("Foam Dinner Plate", "In quis justo. Maecenas rhoncus aliquam lacus. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis.", 5, "http://www.uscasehouse.com/media/catalog/product/cache/1/image/736x460/9df78eab33525d08d6e5fb8d27136e95/p/a/pactiv-0th1001000y-satinware-white-foam-dinner-plate-540-case-bulk-us-casehouse.jpg", False),
    SnacksModel("Wine - White, Riesling, Semi - Dry", "Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Suspendisse potenti. Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum.", 13, "https://www.bothamvineyards.com/wp-content/uploads/2013/03/riesling-cropped-lo-res.jpg", False),
    SnacksModel("Cheese - Taleggio D.o.p.", "Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Nulla ut erat id mauris vulputate elementum. Nullam varius.", 1, "https://www.melburyandappleton.co.uk/ekmps/shops/melburyapple/images/taleggio-dop-500g-4422-p.jpg", True),
    SnacksModel("Cheese - Brie", "Nam dui. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis.", 26, "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Brie_01.jpg/1200px-Brie_01.jpg", False),
    SnacksModel("Tea - Darjeeling, Azzura", "Phasellus sit amet erat. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.", 18, "https://www.udyantea.com/media/catalog/product/cache/1/image/1800x/af097278c5db4767b0fe9bb92fe21690/c/a/castleton_muscatel_gold_black_tea_01.jpg", True),
    SnacksModel("Veal Chops", "In est risus, auctor sed, tristique in, tempus sit amet, sem. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Fusce consequat. Nulla nisl.", 24, "https://foodsogoodmall.com/wp-content/uploads/2014/05/Pan-Seared-Oven-Roasted-Veal-Chops.jpg", True),
    SnacksModel("Tomatoes - Roma", "Phasellus in felis. Donec semper sapien a libero. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Nam dui.", 14, "https://windsetfarms.com/wp-content/uploads/2016/10/WF_Website_Product-on-White-500x375_ROMA.jpg", True),
    SnacksModel("Sauce - Bearnaise, Mix", "Cras pellentesque volutpat dui.Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam.", 8, "https://i5.walmartimages.ca/images/Large/151/164/151164.jpg?odnBound=460", False),
    SnacksModel("Jam - Strawberry, 20 Ml Jar", "Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Quisque ut erat. Curabitur gravida nisi at nibh. In hac habitasse platea dictumst.", 8, "https://happymoneysaver.com/wp-content/uploads/2014/06/1.jpg", True),
    SnacksModel("Cheese - Ricotta", "Nulla tempus. Vivamus in felis eu sapien cursus vestibulum. Proin eu mi. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis.", 14, "https://www.thepkpway.com/wp-content/uploads/2016/12/how-to-make-ricotta-cheese-5f.jpg", True),
    SnacksModel("Remy Red Berry Infusion", "Nunc purus. Phasellus in felis. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Donec semper sapien a libero.", 20, "https://cdn3.volusion.com/nelew.mwyhw/v/vspfiles/photos/RemyRed--2.jpg?1443985288", False),
    SnacksModel("Wine - Chateau Bonnet", "Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Nam nulla. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis.", 21, "https://www.wespeakwine.com/Shared/Images/Product/Andre-Lurton-Chateau-Bonnet-Bordeaux-Rouge-2010-750ML/bonnet_red_bottle.jpg", True),
    SnacksModel("Vegetable - Base", "Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede. Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus.", 10, "https://cdn.shopify.com/s/files/1/1078/9836/products/0844VegLSFront.jpg?v=1470685826", False),
    SnacksModel("Squeeze Bottle", "Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis. Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl.", 15, "https://cdnimg.webstaurantstore.com/images/products/large/48478/1424919.jpg", False),
    SnacksModel(" Pure Vanilla Extract", "Duis at velit eu est congue elementum. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla.Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Sed accumsan felis.", 12, "https://www.dollargeneral.com/media/catalog/product/cache/image/700x700/e9c3970ab036de70892d86c6d221abfe/8/8/889301.jpg", False),
    SnacksModel("Beef Striploin", "Donec dapibus. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis.", 6, "https://s3.amazonaws.com/product-images.imshopping.com/nimblebuy/the-butcher-shoppe-1169042-1976272-regular.jpg", True),
    SnacksModel("Tea - Jasmin Green", "Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis.", 6, "https://www.teabeau.com/wp-content/uploads/2017/12/Mo-Li-Piao-Xue-Jasmine-Green-Tea-1.jpg", True),
    SnacksModel("Wine - Red, Gamay Noir", "Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet. Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo.", 28, "https://moorewilsons.co.nz/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/t/e/te-mata-estate-vineyards-ga/te-mata-estate-vineyards-gamay-noir-31.1513226341.jpg", False),
    SnacksModel("All Natural Organic Black Plastique Fork (qty: 1)", "It is like a really really nice fork... You'd be at a loss to not have such a fantasic piece of cutlery in your home let alone your hand.", 5000000, "https://cdn.shopify.com/s/files/1/1516/1182/products/Black_6inch_Fork_1080x1080_160b0a6d-8f00-4bf0-a40c-1870c761baaf_1024x1024.png?v=1482161307", True),
    SnacksModel("Mushroom - Shitake, Dry", "Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio.", 13, "http://www.2funguys.com/store/media/catalog/product/cache/1/image/1800x/040ec09b1e35df139433887a97daa66f/i/t/itop_shiitake_dried.jpg", True),
    SnacksModel("Lettuce - Radicchio", "Aenean sit amet justo. Morbi ut odio. Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo.", 16, "http://cdn.shopify.com/s/files/1/0206/9470/products/Lettuce_Radichia_0140e32a-b0e7-4fef-ac83-46c597a1f71d_grande.jpeg?v=1479149541", True),
    SnacksModel("Olives - Black, Pitted", "Sed accumsan felis. Ut at dolor quis odio consequat varius. Integer ac leo. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis.", 14, "https://sc02.alicdn.com/kf/HTB1Rp02KFXXXXXwXFXXq6xXFXXXG/Pitted-Black-Olives.jpg", True),
    SnacksModel("Cocoa Powder - Natural", "Donec semper sapien a libero.Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Nam dui.", 20, "http://www.ciranda.com/sites/ciranda.com/files/Organic-Cocoa-Powder-Natural-10-12-gold-w-shadow.png", False),
    SnacksModel("Mushroom - Oyster, Fresh", "Morbi ut odio. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis.", 27, "http://stockarch.com/files/13/08/oyster_mushroom_uncooked.jpg", True),
    SnacksModel("Rosemary - Primerba, Paste", "Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.", 17, "http://www.food.reaton.ru/glimg/food/0912115L.jpg", False),
    SnacksModel("Apple Flavored Scooby Snacks", "A caramel-flavored cookie with special munchy-inducing properties. Good at any time, at home or on the go.", 8, "https://www.k9bytesgifts.com/gallery/dog-treat-samples-loose.jpg", False),
    SnacksModel("BB-8's Brownie Balls", "Delicious and rollable, these flavorful bites will melt in your mouth without tempting you to join the darkside.", 8, "https://foodsofdiversepopulations.files.wordpress.com/2012/08/brownie-ball-pic1.jpg", False)
])

db.session.add_all([
    ReviewsModel("Incredible!", "If it were a person I'd say to it: Is your name Dan Druff? You get into people's hair. I mean like, I'd say that you're funny but looks aren't everything.", 1, 1), 
    ReviewsModel("Tasty!", "If it were a person I'd say to this snack: I appreciate all of your opinions. I mean like, You have ten of the best fingers I have ever seen!", 3, 2), 
    ReviewsModel("Tasty!", "If it were a person I'd say to it: Learn from your parents' mistakes - use birth control! I mean like, I thought of you all day today. I was at the zoo.", 2, 3), 
    ReviewsModel("Refined!", "If it were a person I'd say to this snack: I would share my dessert with you. I mean like, You are a champ!", 5, 4), 
    ReviewsModel("Ergonomic!", "If it were a person I'd say to it: It looks like your face caught on fire and someone tried to put it out with a hammer. I mean like, You're so fat your belly button has an echo echo echo...", 1, 5), 
    ReviewsModel("Refined!", "If it were a person I'd say to this snack: We would enjoy a cookout with you! I mean like, You are the rare catalyst to my volatile compound.", 4, 6), 
    ReviewsModel("Small!", "If it were a person I'd say to it: You're so fat your shadow casts a shadow. I mean like, You may not be the best looking girl here, but beauty is only a light switch away!", 2, 7), 
    ReviewsModel("Intelligent!", "If it were a person I'd say to this snack: There isn't a thing about you that I don't like. I mean like, You will still be beautiful when you get older.", 2, 8), 
    ReviewsModel("Practical!", "If it were a person I'd say to it: You're so dumb, your dog teaches you tricks. I mean like, I don't exactly hate you, but if you were on fire and I had water, I'd drink it.", 2, 9), 
    ReviewsModel("Ergonomic!", "If it were a person I'd say to this snack: You are the gravy to my mashed potatoes. I mean like, Will you sign my yearbook?", 5, 10), 
    ReviewsModel("Incredible!", "If it were a person I'd say to it: You are proof that evolution CAN go in reverse. I mean like, Even if you were twice as smart, you'd still be stupid!", 2, 11), 
    ReviewsModel("Ergonomic!", "If it were a person I'd say to this snack: You make babies smile. I mean like, You're so rad.", 3, 12), 
    ReviewsModel("Fantastic!", "If it were a person I'd say to it: Your ears are so big when you stand on a mountain they look like trophy handles. I mean like, I wish you no harm, but it would have been much better if you had never lived.", 1, 13), 
    ReviewsModel("Refined!", "If it were a person I'd say to this snack: I would enjoy a roadtrip with you. I mean like, You have very smooth hair.", 5, 14), 
    ReviewsModel("Tasty!", "If it were a person I'd say to it: Shut up, you'll never be the man your mother is. I mean like, Ever since I saw you in your family tree, I've wanted to cut it down.", 2, 15), 
    ReviewsModel("Licensed!", "If it were a person I'd say to this snack: Don't worry. You'll do great. I mean like, Don't worry about procrastinating on your studies, I know you'll do great!", 7, 16), 
    ReviewsModel("Awesome!", "If it were a person I'd say to it: Nice tan, orange is my favorite color. I mean like, Somewhere out there is a tree, tirelessly producing oxygen so you can breathe. I think you owe it an apology.", 2, 17), 
    ReviewsModel("Practical!", "If it were a person I'd say to this snack: Your skin is radiant. I mean like, You look so perfect.", 5, 18), 
    ReviewsModel("Generic!", "If it were a person I'd say to it: What are you doing here? Did someone leave your cage open? I mean like, You're so ugly, when you popped out the doctor said \"Aww what a treasure\" and your mom said \"Yeah, lets bury it.\"", 1, 19), 
    ReviewsModel("Fantastic!", "If it were a person I'd say to this snack: I like those shoes more than mine. I mean like, You're nicer than a day on the beach.", 4, 20), 
    ReviewsModel("Small!", "If it were a person I'd say to it: It's better to keep your mouth shut and give the 'impression' that you're stupid than to open it and remove all doubt. I mean like, You are proof that God has a sense of humor.", 2, 21), 
    ReviewsModel("Small!", "If it were a person I'd say to this snack: I heard you make really good French Toast. I mean like, I'd wake up for an 8 a.m. class just so I could sit next to you.", 5, 22), 
    ReviewsModel("Incredible!", "If it were a person I'd say to it: If what you don't know can't hurt you, you're invulnerable. I mean like, Are you always an idiot, or just when I'm around?", 1, 23), 
    ReviewsModel("Sleek!", "If it were a person I'd say to this snack: I would do your taxes any day. I mean like, You deserve a promotion.", 4, 24), 
    ReviewsModel("Handmade!", "If it were a person I'd say to it: The best part of you is still running down your old mans leg. I mean like, I was pro life before I met you.", 2, 25), 
    ReviewsModel("Rustic!", "If it were a person I'd say to this snack: Take a break; you've earned it. I mean like, I don't speak much English, but with you all I really need to say is beautiful.", 4, 26), 
    ReviewsModel("Tasty!", "If it were a person I'd say to it: Keep talking, someday you'll say something intelligent! I mean like, Your dad's condom is a bigger than your personality.", 1, 27), 
    ReviewsModel("Gorgeous!", "If it were a person I'd say to this snack: I heard you make really good French Toast. I mean like, I love what you've done with the place.", 5, 28), 
    ReviewsModel("Fantastic!", "If it were a person I'd say to it: I could eat a bowl of alphabet soup and shit out a smarter statement than that. I mean like, It's kinda sad watching you attempt to fit your entire vocabulary into a sentence.", 1, 29), 
    ReviewsModel("Handmade!", "If it were a person I'd say to this snack: Treat yourself to another compliment! I mean like, You smell nice.", 5, 30), 
    ReviewsModel("Gorgeous!", "If it were a person I'd say to it: If brains were dynamite you wouldn't have enough to blow your nose. I mean like, You do realize makeup isn't going to fix your stupidity?", 2, 31), 
    ReviewsModel("Tasty", "If it were a person I'd say to it: What are you going to do for a face when the baboon wants his butt back? I mean like, You are depriving some poor village of its idiot.", 2, 1), 
    ReviewsModel("Practical", "If it were a person I'd say to this snack: Shall I compare thee to a summer's day?  Thou art more lovely and more temperate. I mean like, Your body fat percentage is perfectly suited for your height.", 4, 2), 
    ReviewsModel("Awesome", "If it were a person I'd say to it: If I wanted to hear from an asshole, I'd fart. I mean like, I heard you went to a haunted house and they offered you a job.", 1, 3), 
    ReviewsModel("Small", "If it were a person I'd say to this snack: You and Chuck Norris are on equal levels. I mean like, You make the gloomy days a little less gloomy.", 3, 4), 
    ReviewsModel("Small", "If it were a person I'd say to it: I was pro life before I met you. I mean like, You're as useful as an ashtray on a motorcycle.", 1, 5), 
    ReviewsModel("Licensed", "If it were a person I'd say to this snack: You look great in this or any other light. I mean like, Your cooking reminds me of my mother's.", 4, 6), 
    ReviewsModel("Gorgeous", "If it were a person I'd say to it: You're so ugly, the only dates you get are on a calendar. I mean like, A sharp tongue is no indication of a keen mind.", 1, 7), 
    ReviewsModel("Sleek", "If it were a person I'd say to this snack: <3 I mean like, You're more cuddly than the Downy Bear.", 4, 8), 
    ReviewsModel("Licensed", "If it were a person I'd say to it: You must have a Teflon brain, because nothing sticks. I mean like, Your ambition outweighs your relevant skills.", 2, 9), 
    ReviewsModel("Rustic", "If it were a person I'd say to this snack: I like your socks. I mean like, You're real happening in a far out way.", 4, 10), 
    ReviewsModel("Unbranded", "If it were a person I'd say to it: You have the perfect face for radio. I mean like, Why don't you slip into something more comfortable -- like a coma.", 1, 11), 
    ReviewsModel("Unbranded", "If it were a person I'd say to this snack: If we were playing kickball, I'd pick you first. I mean like, I like your pants.", 5, 12), 
    ReviewsModel("Tasty", "If it were a person I'd say to it: You prefer three left turns to one right turn. I mean like, You're so ugly you have to trick or treat over the phone.", 2, 13), 
    ReviewsModel("Handmade", "If it were a person I'd say to this snack: Your eyebrows really make your pretty eyes stand out. I mean like, You listen to the coolest music.", 5, 14), 
    ReviewsModel("Gorgeous", "If it were a person I'd say to it: Your breath is so stinky, we look forward to your farts. I mean like, You must have a very low opinion of people if you think they are your equals.", 2, 15), 
    ReviewsModel("Gorgeous", "If it were a person I'd say to this snack: If you were around, I would enjoy doing my taxes. I mean like, You're nicer than a day on the beach.", 4, 16), 
    ReviewsModel("Rustic", "If it were a person I'd say to it: For those who never forget a face, you are an exception. I mean like, It's hard to get the big picture when you have such a small screen.", 1, 17), 
    ReviewsModel("Practical", "If it were a person I'd say to this snack: You are the star of my daydreams. I mean like, You're sweeter than than a bucket of bon-bons!", 5, 18), 
    ReviewsModel("Refined", "If it were a person I'd say to it: You look like a before picture. I mean like, You do realize makeup isn't going to fix your stupidity?", 2, 19), 
    ReviewsModel("Rustic", "If it were a person I'd say to this snack: Well done! I mean like, You would look good in glasses OR contacts.", 5, 20), 
    ReviewsModel("Handcrafted", "If it were a person I'd say to it: Why don't you check eBay and see if they have a life for sale. I mean like, Just reminding u there is a very fine line between hobby and mental illness.", 2, 21), 
    ReviewsModel("Intelligent", "If it were a person I'd say to this snack: You're the bee's knees. I mean like, Your feet are perfect size!", 1, 22), 
    ReviewsModel("Handcrafted", "If it were a person I'd say to it: Any similarity between you and a human is purely coincidental. I mean like, If ignorance is bliss, you must be the happiest person on earth.", 1, 23), 
    ReviewsModel("Refined", "If it were a person I'd say to this snack: You are a bucket of awesome. I mean like, You are infatuating.", 5, 24), 
    ReviewsModel("Small", "If it were a person I'd say to it: Is your ass jealous of the amount of shit that just came out of your mouth? I mean like, Your family tree must be a cactus because everybody on it is a prick.", 1, 25), 
    ReviewsModel("Gorgeous", "If it were a person I'd say to this snack: I would share my fruit Gushers with you. I mean like, I could hang out with you for a solid year and never get tired of you.", 1, 26), 
    ReviewsModel("Small", "If it were a person I'd say to it: Nice tan, orange is my favorite color. I mean like, You must have a very low opinion of people if you think they are your equals.", 2, 27), 
    ReviewsModel("Rustic", "If it were a person I'd say to this snack: I wish I could move your furniture. I mean like, If you were in a movie you wouldn't get killed off.", 4, 28), 
    ReviewsModel("Handcrafted", "If it were a person I'd say to it: Looks aren't everything; in your case, they aren't anything I mean like, Nice tan, orange is my favorite color.", 1, 29), 
    ReviewsModel("Tasty", "If it were a person I'd say to this snack: You are a champ! I mean like, I like those shoes more than mine.", 5, 30), 
    ReviewsModel("Awesome", "If it were a person I'd say to it: Your dad's condom is a bigger than your personality. I mean like, You're so fat your belly button has an echo echo echo...", 2, 31), 
    ReviewsModel("Bad for business", "My guards love these, but you try keeping the larder full when all of your Gamorians have the munchies!", 1, 31),
    ReviewsModel("Biscotti Bliss!", "Cookie! Me want cookie!", 4, 31),
    ReviewsModel("The treat that travels well", "I like 'em, and they are great at sea; they don't even need to be salt-packed!", 4, 31),
    ReviewsModel("Seriously? Yuck", "I have certainly had sooooo much better.", 1, 31),
    ReviewsModel("Solo! Solo! Too Nakma Noya Solo!", "Han ma boo-kee, keelee ka-lya dooka. Wadja da boolya ra Moy. Han, Mah kee cheezay. Hassatamooma koh kee malyaloongee.", 5, 31),
    ReviewsModel("*Snobby Voice*", "Well I have certainly had sooooo much better.", 1, 2),
    ReviewsModel("I can't have just one!", 'I love these! Not only are they yummy, but they give me that certain je ne sais quoi I need in the courage department to fight ghosts.', 5, 31)
  ])

db.session.commit()