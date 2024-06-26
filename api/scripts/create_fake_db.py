import random

from api.app import db, app
from api.models.models import Quote, Teacher
from faker import Faker
import os

os.chdir("../")


fake = Faker()


with app.app_context():
    db.drop_all()

    teacher_entries = [
        ('Aulepp', 'Simon', 'simon.aulepp@schule.hessen.de', '1'),
        ('Bachmann', 'Meike', 'meike.bachmann@schule.hessen.de', '1'),
        ('Backhaus', 'Benjamin', 'benjamin.backhaus@schule.hessen.de', '1'),
        ('Dettmer', 'Annika', 'annika.dettmer@schule.hessen.de', '1'),
        ('Di Fuccia', 'Violetta', 'violetta.difuccia@schule.hessen.de', '1'),
        ('Donskoi', 'Kathrin', 'kathrin.donskoi@schule.hessen.de', '1'),
        ('Eckhardt', 'Guido', 'guido.eckhardt@schule.hessen.de', '1'),
        ('Eichner', 'Maria', 'maria.eichner@schule.hessen.de', '1'),
        ('Emde', 'Christian', 'christian.emde@schule.hessen.de', '1'),
        ('Emde', 'Sonja', 'sonja.emde@schule.hessen.de', '1'),
        ('Fooken', 'Dierk', 'dierk.fooken@schule.hessen.de', '1'),
        ('Franz', 'Silke', 'silke.franz@schule.hessen.de', '1'),
        ('Fuhr', 'Gunther', 'manfred.fuhr@schule.hessen.de', '1'),
        ('Gerhards', 'Björn', 'bjoern.gerhards@schule.hessen.de', '1'),
        ('Gerland', 'Simone', 'simone.gerland@schule.hessen.de', '1'),
        ('Geßner', 'Jörg', 'joerg.gessner@schule.hessen.de', '1'),
        ('Görth', 'Meike', 'meike.goerth@schule.hessen.de', '1'),
        ('Groß', 'René', 'rene.gross@schule.hessen.de', '1'),
        ('Grüninger', 'Ursula', 'ursula.grueninger@schule.hessen.de', '1'),
        ('Haas', 'Domenica', 'domenica.haas@schule.hessen.de', '1'),
        ('Haferburg', 'Sven', 'sven.haferburg@schule.hessen.de', '1'),
        ('Haschen', 'Heike', 'heike.haschen@schule.hessen.de', '1'),
        ('Hofmann', 'Thomas', 'thomas.hofmann2@schule.hessen.de', '1'),
        ('Hülsmann', 'Andreas', 'andreas.huelsmann@schule.hessen.de', '1'),
        ('Huscher', 'Christopher', 'christopher.huscher@schule.hessen.de', '1'),
        ('Kallmeyer', 'Alexander', 'alexander.kallmeyer@schule.hessen.de', '1'),
        ('Kastmann', 'Katharina', 'ira.kastmann@schule.hessen.de', '1'),
        ('Kunsch', 'Christiane', 'christiane.kunsch@schule.hessen.de', '1'),
        ('Likci', 'Lara', 'lara.likci@schule.hessen.de', '1'),
        ('Lindner', 'Annika', 'annika.lindner@schule.hessen.de', '1'),
        ('Lingelbach', 'Constanze', 'constanze.lingelbach@schule.hessen.de', '1'),
        ('Meyfarth', 'Thorsten', 'thorsten.meyfarth@schule.hessen.de', '1'),
        ('Müller', 'Nora', 'nora.mueller2@schule.hessen.de', '1'),
        ('Neumann-Westhof', 'Britta', 'britta.neumann-westhof@schule.hessen.de', '1'),
        ('Neuner', 'Jeanette', 'jeanette.neuner@schule.hessen.de', '1'),
        ('Nitsch', 'Anne', 'anne-kristin.nitsch@schule.hessen.de', '1'),
        ('Nordmeier', 'Beatrice', 'beatrice.nordmeier@schule.hessen.de', '1'),
        ('Otto', 'Kerstin', 'kerstin.otto@schule.hessen.de', '1'),
        ('Pfeifer', 'Max', 'max.pfeifer@schule.hessen.de', '1'),
        ('Philipp', 'Jasmina', 'jasmina.philipp@schule.hessen.de', '1'),
        ('Reiß-Jäger', 'Philipp', 'philipp.reiss-jaeger@schule.hessen.de', '1'),
        ('Ritter', 'Alexandra', 'alexandra.ritter@schule.hessen.de', '1'),
        ('Rosenkranz', 'Susanne', 'susanne.rosenkranz@schule.hessen.de', '1'),
        ('Schmoll', 'Anna-Lena', 'anna-lena.schmoll@schule.hessen.de', '1'),
        ('Schulze', 'Sabine', 'sabine.schulze2@schule.hessen.de', '1'),
        ('Schulze', 'Stephanie', 'stephanie.schulze@schule.hessen.de', '1'),
        ('Sivrić-Peša', 'Sanela', 'sanela.sivric-pesa@schule.hessen.de', '1'),
        ('Sommerfeld', 'Lisa', 'lisa.sommerfeld@schule.hessen.de', '1'),
        ('Söther', 'Kai', 'kai.soether@schule.hessen.de', '1'),
        ('Trusheim', 'Bernd', 'bernd.trusheim@schule.hessen.de', '1'),
        ('Ventura', 'Maria João', 'maria.venturacorceiromendes@schule.hessen.de', '1'),
        ('Weyer', 'Annabelle', 'annabelle.weyer@schule.hessen.de', '1'),
        ('Witte', 'Jan-Patrick', 'jan-patrick.witte@schule.hessen.de', '1'),
        ('Wittwer', 'Thomas', 'thomas.wittwer@schule.hessen.de', '1'),
        ('Brandstäter', 'Saskia', 'saskia.brandstäter@schule.hessen.de', '1'),
        ('Fischer', 'Marie-Charlott', 'marie-charlott.fischer@schule-hessen.de', '1'),
        ('Giller', 'Jana', 'jana.giller@schule.hessen.de', '1'),
        ('Göbel', 'Tim', 'tim.goebel@schule.hessen.de', '1'),
        ('Keßler', 'Jana', 'jana.kessler@schule.hessen.de', '1'),
        ('Knauf', 'Theresa', 'theresa.knauf@schule.hessen.de', '1'),
        ('Kumerics', 'Andreas', 'andreas.kumerics@schule.hessen.de', '1'),
        ('Linß', 'Caroline', 'caroline.linss@schule.hessen.de', '1'),
        ('Pavel', 'Katja', 'katja.pavel@schule.hessen.de', '1'),
        ('Richter', 'Sascha', 'sascha.richter2@schule.hessen.de', '1'),
        ('Tunalioglu', 'Damla', 'damla.tunalioglu@schule.hessen.de', '1'),
        ('Rainer', 'Beckert', 'rainer.beckert@schule.hessen.de', '1'),
        ('Bock', 'Norbert', 'norbert.bock@schule.hessen.de', '1'),
        ('Brauer', 'Florian', 'flobrauer@web.de', '1'),
        ('Detka', 'Lena', 'lena.detka@schule.hessen.de', '1'),
        ('Hoeppe', 'Christine', 'christine.hoeppe@schule.hessen.de', '1'),
        ('Lutz', 'Burkhard', 'b.lutz@osw-kassel.de', '1'),
        ('Müller', 'Tanja', 'tanja.mueller@schule.hessen.de', '1'),
        ('Noske', 'Silke', 'silke.noske@schule.hessen.de', '1'),
        ('Pengel', 'Tobias', 'tobias.pengel@schule.hessen.de', '1'),
        ('Perl', 'Annika', 'annika.perl@schule.hessen.de', '1'),
        ('Starke', 'Petra', 'petra.starke@schule.hessen.de', '1'),
        ('Zitouni', 'Khaira-Salima', 'khaira-salima.zitouni@schule.hessen.de', '1'),
        ('Niklas', 'Brede', 'niklas.brede@schule.hessen.de', '1'),
        ('Förster', 'Julia', 'julia.foerster2@schule.hessen.de', '1'),
        ('Hilberg', 'Tatiana', 'tatiana.hilberg@schule.hessen.de', '1'),
        ('Müller', 'Edmund', 'edekassel@t-online.de', '1'),
    ]
    db.create_all()

    for teacher in teacher_entries:
        db.session.add(Teacher(name=f"{teacher[1]} {teacher[0]}"))

    db.session.commit()

    for i in range(200):
        db.session.add(Quote(
            teacher_id=random.randint(1, 20),
            quote="".join(fake.sentences(3)),
            votes=random.randint(-200, 200)
        ))

    db.session.commit()
