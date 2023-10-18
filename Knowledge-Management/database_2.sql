DROP DATABASE IF EXISTS KNOWLEDGE_MAPPING;
CREATE DATABASE KNOWLEDGE_MAPPING;
USE KNOWLEDGE_MAPPING;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL
);

CREATE TABLE restaurants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255) NOT NULL,
    open_time TIME NOT NULL,
    close_time TIME NOT NULL
);

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT NOT NULL,
    customer_id INT NOT NULL,
    order_total DECIMAL(7 , 2 ) NOT NULL,
    order_time DATETIME NOT NULL,
    order_status ENUM('ON-GOING', 'FINISHED'),
    FOREIGN KEY (customer_id)
        REFERENCES users (id),
    FOREIGN KEY (restaurant_id)
        REFERENCES restaurants (id)
);


CREATE TABLE payment_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    payment_method ENUM('CASH', 'CREDIT-CARD'),
    payment_status ENUM('SUCCESS', 'FAILED'),
    FOREIGN KEY (order_id)
        REFERENCES orders (id)
);

CREATE TABLE menu_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    item_description VARCHAR(255),
    price DECIMAL(7 , 2 ) NOT NULL,
    restaurant_id INT NOT NULL,
    FOREIGN KEY (restaurant_id)
        REFERENCES restaurants (id)
);

CREATE TABLE order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    item_id INT NOT NULL,
    item_quantity INT NOT NULL,
    FOREIGN KEY (order_id)
        REFERENCES orders (id),
    FOREIGN KEY (item_id)
        REFERENCES menu_items (id)
);


INSERT INTO users (username, email, password, first_name, last_name, address)
VALUES
  ("44277","eget@hotmail.ca","NRO46IQC9QR","Magee","Papadopoulos","Κουντουριώτου 6-16, Νέα Σμύρνη 17122"),
  ("05447","venenatis.a.magna@yahoo.org","CXN58IWE1BB","Maia","Pappa","Νυμφαίου 13-9, Νέα Σμύρνη 17121"),
  ("68536","donec.egestas@icloud.couk","PGT76GAB1CQ","Dane","Vlahos","Λεωφ. Ελ. Βενιζέλου 5, Νέα Σμύρνη 17121"),
  ("25738","pellentesque@aol.net","MTA70FUI9XN","Sierra","Karagianni","Σεβδικίου 13, Νέα Σμύρνη 171 21"),
  ("55343","risus@aol.org","ILE20PRW7IF","Denise","Vlahos","Καΐρη Θεοφίλου 3, Νέα Σμύρνη 17122"),
  ("08331","aliquam@protonmail.org","YOY94WEP6KN","Silas","Papageorgiou"," Μεγ. Αλεξάνδρου 11, Νέα Σμύρνη 17121"),
  ("11422","neque@hotmail.couk","CUR77SDH1BU","Jonas","Makris","Χρήστου Αρώνη 5-1, Νέα Σμύρνη 17122"),
  ("32732","cursus.et@hotmail.couk","QKT53COT3IE","Eve","Konstantinidi","Καλύμνου 5, Νέα Σμύρνη 171 22"),
  ("62148","nunc.pulvinar@protonmail.edu","OEJ61ABA5ZF","Ayanna","Dimopoulos","Πλ. Βασιλέως Γεωργίου Β 44, Νέα Σμύρνη 17122"),
  ("88013","pharetra.nam@icloud.ca","YAS35LUX2YO","Gannon","Antoniou","Νίκαιας 5, Νέα Σμύρνη 17122"),
  ("17321","nulla.eget.metus@protonmail.com","ZHL16EAY5ZQ","Shaine","Vasiliou","Σεβαστείας 20, Νέα Σμύρνη 17122"),
  ("30765","orci@google.couk","KKT89CJJ8YF","Christen","Nikolaou","Μαδύτου 3, Νέα Σμύρνη 17123"),
  ("03351","aliquam@aol.couk","OOH43DPR5JR","Lynn","Papadakis","Βοσπόρου 101-93, Νέα Σμύρνη 17123"),
  ("72278","nec.urna@icloud.com","USV04CWR6QU","Irene","Georgiadis"," Μαδύτου 10, Νέα Σμύρνη 17123"),
  ("32976","mauris@outlook.org","VHK48BQW1VU","Alexander","Makiavelis","Ηπείρου 63, Πέραμα 18863");
  
  INSERT INTO restaurants (restaurant_name, email, address, phone_number, open_time, close_time)
  VALUES
  ("Sante", "sante@kal.gr", "ΕΛ.ΒΕΝΙΖΕΛΟΥ 74, Καλλιθέα 17672", "2109520777", "06:00:00", "06:00:00"),
  ("Tiou Pizza", "tioupizza@per.gr", "Ελευθερίας 94 Πέραμα 18863, Πειραιάς", "2104417209", "09:00:00", "01:00:00"),
  ("Coffee Island", "coffeeisland@ad.gr", "Αγίου Δημητρίου 97 Άγιος Δημήτριος 17343, Αθήνα", "2114004200", "07:00:00", "18:00:00"),
  ("Coffee Berry", "coffeeberry@ns.gr", "2ας Μαΐου 38 Νέα Σμύρνη 17121, Αθήνα", "2109370420", "07:30:00", "19:30:00"),
  ("Coffee Lab", "coffeelab@ns.gr", "Ελευθερίου Βενιζέλου 205 Νέα Σμύρνη 17123, Αθήνα", "2109337752", "07:00:00", "20:00:00"),
  ("Πιάτσα Καλαμάκι", "piatsakalamaki@ns.gr", "2ας Μαΐου 34 Νέα Σμύρνη 17121, Αθήνα", "2109343023", "12:00:00", "02:00:00"),
  ("Pueblo Chido cocina mexicana", "mexicana@ns.gr", "Λεωφόρος Ελευθερίου Βενιζέλου 24, Αττική, 17121", "2109323230", "13:00:00", "24:00:00"),
  ("Sushi `Ο", "sushi@pf.gr", "Αχιλλέως 74 Παλαιό Φάληρο 17563, Αθήνα", "2113115555", "13:30:00", "23:30:00"),
  ("Castello pizza", "castello@alimos.gr", "Θεμιστοκλέους 25 Άλιμος 17455, Αθήνα", "2109818439", "12:00:00", "01:00:00"),
  ("Mr Dion Cafe", "mrdion@ns.gr", "Αιγαίου 27 Νέα Σμύρνη 17121, Αθήνα", "2114168254", "06:50:00", "18:50:00");
  
  
  INSERT INTO menu_items (item_name, item_description, price, restaurant_id)
  VALUES
  ("Μπουγάτσα κρέμα","Μερίδα. Με ζάχαρη άχνη & κανέλα",2.5,1),
  ("Μπουγάτσα σοκολάτα","Μερίδα. Με κρέμα & επικάλυψη πραλίνα σοκολάτα",3.5,1),
  ("Φωλιά μπιφτέκι","Με μπιφτέκι από 100% μοσχαρίσιο κιμά, τυρί & σάλτσα",3.2,1),
  ("Μπουγάτσα τυρί","Μερίδα",2.5,1),
  ("Νερό 500ml","",0.5,1),
  ("Coca-Cola 330ml","",1.2,1),
  ("Χωριάτικη","8 Κομμάτια. Με σάλτσα ντομάτας, φέτα, ντομάτα, κρεμμύδι, πιπεριά & ελιές",8.5,2),
  ("Carbonara","Με κρέμα γάλακτος, μπέικον & ζαμπόν. Συνοδεύεται από τριμμένο gouda & χειροποίητο ψωμί",6.9,2),
  ("Special","8 Κομμάτια. Με σάλτσα ντομάτας, gouda, ζαμπόν, μπέικον, μανιτάρια & πιπεριά",8.5,2),
  ("Μαργαρίτα","8 Κομμάτια. Με σάλτσα ντομάτας & gouda",6.0,2),
  ("Νερό 500ml","",0.5,2),
  ("Coca-Cola 330ml","",1.2,2),
  ("Freddo espresso","12oz",2.1,3),
  ("Coffeeccino","12oz",2.4,3),
  ("Iced latte","12oz",2.6,3),
  ("Muffin διπλή σοκολάτα","Με γεύση πραλίνα φουντουκιού",2.0,3),
  ("Φυσικός χυμός πορτοκάλι","12oz",2.2,3),
  ("Νερό 500ml","",0.5,3),
  ("Coca-Cola 330ml","",1.0,3),
  ("Βιεννέζικη μπαγκέτα γαλοπούλα","Μπαγκέτα βιεννέζικη με μαγιονέζα, λόλα, τυρί edam, γαλοπούλα βραστή & ντομάτα",3.0,4),
  ("Τορτίγια κοτόπουλο","1 Τεμάχιο. Τορτίγια με sauce μουστάρδα, σαλάτα Caesar`s, τυρί edam, κοτόπουλο φιλέτο & ντομάτα",1.6,4),
  ("Κρουασάν βουτύρου με γέμιση σοκολάτα","",1.9,4),
  ("Freddo espresso","",1.8,4),
  ("Cappuccino","",1.8,4),
  ("Νερό 500ml","",0.5,4),
  ("Coca-Cola 330ml","",1.2,4),
  ("Donut πραλίνα","",1.5,5),
  ("Chocco Ball με donut","Με πάγο, γάλα, Nutella, σκόνη βανίλια, σιρόπι σοκολάτα & από πάνω Donut σοκολάτα",3.5,5),
  ("Freddo espresso","",1.9,5),
  ("Cappuccino","",1.8,5),
  ("Freddo cappuccino","",2.0,5),
  ("Νερό 500ml","",0.5,5),
  ("Coca-Cola 330ml","",1.2,5),
  ("Καλαμάκι κοτόπουλο μπούτι σε πίτα","Πίτα καλαμάκι κοτόπουλο μπούτι με τα υλικά της επιλογής σας",3.5,6),
  ("Γύρος χοιρινός σε θρακόψωμο","Θρακόψωμο γύρος χοιρινός με τα υλικά της επιλογής σας",7.2,6),
  ("Caesar με γύρο κοτόπουλο","Σαλάτα με γύρο κοτόπουλο, μαρούλι, κρουτόν, τριμμένη παρμεζάνα & sauce Caesar",5.6,6),
  ("Γύρος χοιρινός σε πίτα","Πίτα γύρος χοιρινός με τα υλικά της επιλογής σας",3.6,6), 
  ("Σκεπαστή γύρος χοιρινός","Σκεπαστή γύρος χοιρινός με τα υλικά της επιλογής σας",8.8,6),
  ("Classic burger","Με χειροποίητο μπιφτέκι 150gr, cheddar, λόλα, κρεμμύδι, ντομάτα, BBQ σως & σως μουστάρδας",5.6,6),
  ("Νερό 500ml","",0.5,6),
  ("Coca-Cola 330ml","",1.2,6),
  ("Βurrito pulled pork","Tortilla σίτου με γέμιση pulled pork, μεξικάνικο ρύζι, cheddar mix & καλυμμένο από queso ranch, sour cream sauce, pico de gallo, guacamole & salsa casera",12.5,7),
  ("Fajitas al pastor","Με χοιρινό λεπτοκομμένο 300gr, ανανά, πιπεριές πολύχρωμες & κρεμμύδια ψημένα στο μαντέμι. Συνοδεύεται από 5 tortillas soft, μεξικάνικο ρύζι, sour cream sauce, pico de gallo & salsa casera",20.0,7),
  ("Pollo al cubano","350gr. Kομμάτια μαριναρισμένα από στήθος & μπούτι κοτόπουλο, ψημένα στη σχάρα, πάνω σε 3 soft tortillas με jalapenos, φύλλα κόλιανδρου & lime. Συνοδεύεται από μεξικάνικο ρύζι & chipotle mayo",16.5,7),
  ("De passion","Σαλάτα με σπανάκι, φύλλα παντζαριού, ρόκα, avocado, τραγανές τορτίγιες, φυστίκι, mango, τυρί cotija & dressing passion fruit",12.5,7),
  ("Elote Mexican street corn","1 Καλαμπόκι ψημένο στη σχάρα με chipotle mayo, μπέικον, παρμεζάνα, κόλιανδρο & nachos τριμμένα",7.2,7),
  ("Νερό 500ml","",0.5,7),
  ("Coca-Cola 330ml","",1.2,7),
  ("Sake tartar","Με σολομό, wakame, avocado, ikura, τηγανητό κρεμμύδι, αυγά χελιδονόψαρου, ponzu & μαγιονέζα τρούφας",10.5,8),
  ("Sea bass temaki","1 Τεμάχιο. Με λαβράκι, αγγούρι, φρέσκο κρεμμύδι, ikura & yuzu soy",6.5,8),
  ("Salmon teriyaki","8 Τεμάχια. Με σολομό, avocado, αγγούρι & teriyaki sauce",11.5,8),
  ("Dragon","8 Τεμάχια. Με χέλι, avocado, αγγούρι, τηγανητό κρεμμύδι & unagi sauce",11.4,8),
  ("Volcano","8 Τεμάχια. Με γαρίδα tempura, surimi, avocado, τηγανητά κρεμμύδια, spicy mayo & wasabi mayo",12.3,8),
  ("New style salmon nigiri","4 Τεμάχια. Με καπνιστό σολομό, αυγά σολομού & sushi `O sauce",9.5,8),
  ("Νερό 500ml","",0.5,8),
  ("Coca-Cola 330ml","",1.2,8),
  ("Ζαμπόν","Με σάλτσα ντομάτας, gouda & ζαμπόν",7.5,9),
  ("Χωριάτικη","Με σάλτσα ντομάτας, gouda, φέτα, ελιές, κρεμμύδι, πιπεριά & φρέσκια ντομάτα",8.5,9),
  ("Castello","Με σάλτσα ντομάτας, gouda, ζαμπόν, μπέικον, σαλάμι αέρος, σουτζούκι, πεπερόνι, μανιτάρια & πιπεριά",8.7,9),
  ("Special κομπλέ","Με σάλτσα ντομάτας, gouda, ζαμπόν, μπέικον, σαλάμι αέρος, πεπερόνι, μανιτάρια & πιπεριά",8.4,9),
  ("Πεπερόνι","Με σάλτσα ντομάτας, gouda & πεπερόνι",7.5,9),
  ("Του σεφ","Σαλάτα με μαρούλι, ντομάτα, ζαμπόν, gouda & sauce",3.3,9),
  ("Caesar`s","Σαλάτα με μαρούλι, φρέσκο φιλέτο κοτόπουλο, μπέικον, παρμεζάνα, κρουτόν, καλαμπόκι & sauce vinaigrette",3.6,9),
  ("Νερό 500ml","",0.5,9),
  ("Coca-Cola 330ml","",1.2,9),
  ("Τυρόπιτα κουρού","Χειροποίητη",2.0,10),
  ("Μπαγκέτα κοτόπουλο","Με κοτόπουλο, λάχανο, καρότο & σως",3.6,10),
  ("Freddo espresso","Dimello",2.0,10),
  ("Cappuccino","Dimello",2.0,10),
  ("Κρουασάν βουτύρ","",1.7,10),
  ("Νερό 500ml","",0.5,10),
  ("Coca-Cola 330ml","",1.2,10);
 
 -- ΠΑΡΑΓΓΕΛΙΕΣ --
insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (1,1,12.20,"2023-01-19 14:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (1,'CREDIT-CARD','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (1,1,1);
insert into order_Items (order_id,item_id,item_quantity)  values (1,2,1);
insert into order_Items (order_id,item_id,item_quantity)  values (1,3,1);
insert into order_Items (order_id,item_id,item_quantity)  values (1,4,1);
insert into order_Items (order_id,item_id,item_quantity)  values (1,5,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (2,2,29.90,"2023-01-19 14:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (2,'CASH','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (2,7,1);
insert into order_Items (order_id,item_id,item_quantity)  values (2,8,1);
insert into order_Items (order_id,item_id,item_quantity)  values (2,9,1);
insert into order_Items (order_id,item_id,item_quantity)  values (2,10,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (3,3,7.10,"2023-01-19 14:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (3,'CREDIT-CARD','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (3,13,1);
insert into order_Items (order_id,item_id,item_quantity)  values (3,14,1);
insert into order_Items (order_id,item_id,item_quantity)  values (3,15,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (4,4,4.60,"2023-01-19 14:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (4,'CASH','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (4,20,1);
insert into order_Items (order_id,item_id,item_quantity)  values (4,21,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (5,5,1.50,"2023-01-19 14:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (5,'CREDIT-CARD','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (5,27,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (6,6,28.70,"2023-01-19 14:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (6,'CASH','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (6,34,1);
insert into order_Items (order_id,item_id,item_quantity)  values (6,35,1);
insert into order_Items (order_id,item_id,item_quantity)  values (6,36,1);
insert into order_Items (order_id,item_id,item_quantity)  values (6,37,1);
insert into order_Items (order_id,item_id,item_quantity)  values (6,38,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (7,7,61.50,"2023-01-19 14:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (7,'CREDIT-CARD','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (7,42,1);
insert into order_Items (order_id,item_id,item_quantity)  values (7,43,1);
insert into order_Items (order_id,item_id,item_quantity)  values (7,44,1);
insert into order_Items (order_id,item_id,item_quantity)  values (7,45,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (8,8,28.50,"2023-01-19 14:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (8,'CREDIT-CARD','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (8,49,1);
insert into order_Items (order_id,item_id,item_quantity)  values (8,50,1);
insert into order_Items (order_id,item_id,item_quantity)  values (8,51,1);


insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (9,9,16.00,"2023-01-19 14:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (9,'CASH','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (9,57,1);
insert into order_Items (order_id,item_id,item_quantity)  values (9,58,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (10,10,2.00,"2023-01-19 14:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (10,'CREDIT-CARD','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (10,66,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (11,1,10.90,"2023-01-20 16:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (11,'CREDIT-CARD','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (11,2,1);
insert into order_Items (order_id,item_id,item_quantity)  values (11,3,1);
insert into order_Items (order_id,item_id,item_quantity)  values (11,4,1);
insert into order_Items (order_id,item_id,item_quantity)  values (11,5,1);
insert into order_Items (order_id,item_id,item_quantity)  values (11,6,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (12,2,16.20,"2023-01-20 16:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (12,'CREDIT-CARD','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (12,9,1);
insert into order_Items (order_id,item_id,item_quantity)  values (12,10,1);
insert into order_Items (order_id,item_id,item_quantity)  values (12,11,1);
insert into order_Items (order_id,item_id,item_quantity)  values (12,12,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (13,3,3.70,"2023-01-20 16:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (13,'CASH','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (13,17,1);
insert into order_Items (order_id,item_id,item_quantity)  values (13,18,1);
insert into order_Items (order_id,item_id,item_quantity)  values (13,19,1);


insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (14,4,3.70,"2023-01-20 16:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (14,'CREDIT-CARD','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (14,22,1);
insert into order_Items (order_id,item_id,item_quantity)  values (14,23,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (15,5,1.90,"2023-01-20 16:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (15,'CASH','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (15,29,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (1,6,24.80,"2023-01-20 16:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (16,'CASH','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (16,36,1);
insert into order_Items (order_id,item_id,item_quantity)  values (16,37,1);
insert into order_Items (order_id,item_id,item_quantity)  values (16,38,1);
insert into order_Items (order_id,item_id,item_quantity)  values (16,39,1);
insert into order_Items (order_id,item_id,item_quantity)  values (16,40,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (2,8,34.40,"2023-01-20 16:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (17,'CREDIT-CARD','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (17,52,1);
insert into order_Items (order_id,item_id,item_quantity)  values (17,53,1);
insert into order_Items (order_id,item_id,item_quantity)  values (17,54,1);
insert into order_Items (order_id,item_id,item_quantity)  values (17,55,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (3,9,14.40,"2023-01-20 16:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (18,'CREDIT-CARD','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (18,61,1);
insert into order_Items (order_id,item_id,item_quantity)  values (18,62,1);
insert into order_Items (order_id,item_id,item_quantity)  values (18,63,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (4,7,29.00,"2023-01-20 16:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (19,'CASH','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (19,44,1);
insert into order_Items (order_id,item_id,item_quantity)  values (19,45,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (5,10,3.60,"2023-01-20 16:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (20,'CREDIT-CARD','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (20,67,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (6,9,11.30,"2023-01-21 16:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (21,'CREDIT-CARD','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (21,66,1);
insert into order_Items (order_id,item_id,item_quantity)  values (21,67,1);
insert into order_Items (order_id,item_id,item_quantity)  values (21,68,1);
insert into order_Items (order_id,item_id,item_quantity)  values (21,69,1);
insert into order_Items (order_id,item_id,item_quantity)  values (21,70,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (7,9,22.80,"2023-01-21 18:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (22,'CREDIT-CARD','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (22,60,1);
insert into order_Items (order_id,item_id,item_quantity)  values (22,61,1);
insert into order_Items (order_id,item_id,item_quantity)  values (22,62,1);
insert into order_Items (order_id,item_id,item_quantity)  values (22,63,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (8,6,15.60,"2023-01-21 18:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (23,'CREDIT-CARD','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity)  values (23,38,1);
insert into order_Items (order_id,item_id,item_quantity)  values (23,39,1);
insert into order_Items (order_id,item_id,item_quantity)  values (23,40,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (9,4,2.30,"2023-01-21 18:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (24,'CREDIT-CARD','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity) values (24,23,1);
insert into order_Items (order_id,item_id,item_quantity) values (24,26,1);

insert into orders (customer_id,restaurant_id,order_total,order_time,order_status) values (10,2,6.90,"2023-01-21 18:00:00","FINISHED");
insert into payment_info (order_id,payment_method,payment_status) values (25,'CASH','SUCCESS');
insert into order_Items (order_id,item_id,item_quantity) values (25,8,1);

-- Select the average cost of an order
SELECT AVG(order_total) as avg_cost
FROM orders
JOIN restaurants ON orders.restaurant_id = restaurants.id;

-- Select the total revenue for each restaurant
SELECT restaurant_name, SUM(menu_items.price * order_items.item_quantity) as total_revenue
FROM order_items
JOIN menu_items ON order_items.item_id = menu_items.id
JOIN restaurants ON menu_items.restaurant_id = restaurants.id
GROUP BY restaurant_name
ORDER BY total_revenue;

-- Select the most popular menu item
SELECT menu_items.item_name, SUM(order_items.item_quantity) as popularity
FROM order_items
JOIN menu_items ON order_items.item_id = menu_items.id
JOIN restaurants ON menu_items.restaurant_id = restaurants.id
GROUP BY menu_items.item_name
ORDER BY popularity DESC
LIMIT 1;

-- Query to get the most popular menu item by revenue
SELECT item_name, SUM(item_quantity * menu_items.price) as total_revenue
FROM order_items
JOIN menu_items ON order_items.item_id = menu_items.id
GROUP BY item_name
ORDER BY total_revenue DESC
LIMIT 1;

-- Query to find the total spending  for each user
SELECT first_name, SUM(order_total) as 'Total Spent' FROM users
JOIN orders ON users.id = orders.customer_id
GROUP BY first_name, last_name ORDER BY SUM(order_total);

-- Query to find the number of orders from every user
SELECT first_name, COUNT(orders.id) as 'Number of Orders' 
FROM users
JOIN orders ON users.id = orders.customer_id
GROUP BY first_name 
ORDER BY COUNT(orders.id);

-- Average total cost per order for each user
SELECT users.first_name, ROUND(AVG(orders.order_total), 2) AS average_total_per_order
FROM orders
JOIN users ON orders.customer_id = users.id
GROUP BY users.first_name
ORDER BY average_total_per_order;

-- This query will join the orders table with the users table on the customer_id and the payment_info table on the order_id to give you the full details for each order including the user's first name, order id, order total, order time, order status, payment method and payment status.
SELECT 
    users.first_name,
    orders.order_total as order_total,
    orders.order_time as order_time,
    orders.order_status as order_status,
    payment_info.payment_method as payment_method,
    payment_info.payment_status as payment_status
FROM 
    orders 
    JOIN users ON orders.customer_id = users.id
    JOIN payment_info ON payment_info.order_id = orders.id;

-- This query will join the order_items table with the menu_items and restaurants table on the item_id and restaurant_id respectively, group the results by the restaurant_name and item_name, and sum the item_quantity to get the popularity of each item. The result will be ordered by item_popularity in descending order and restaurant_name in ascending order, so the most popular item for each restaurant will be at the top.
SELECT 
    restaurants.restaurant_name,
    menu_items.item_name,
    SUM(order_items.item_quantity) as item_popularity
FROM 
    order_items
    JOIN menu_items ON order_items.item_id = menu_items.id
    JOIN restaurants ON menu_items.restaurant_id = restaurants.id
GROUP BY 
    restaurants.restaurant_name,
    menu_items.item_name
ORDER BY 
    item_popularity DESC,
    restaurants.restaurant_name;
