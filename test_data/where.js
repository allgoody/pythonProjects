myData = [
[50.06688579999999,19.9136192, 'aleja Adama Mickiewicza 30, 30-059 Kraków, Poland', 'AGH University of Science and Technology'],
[52.2394019,21.0150792, 'Krakowskie Przedmieście 5, 00-068 Warszawa, Poland', 'Academy of Fine Arts Warsaw Poland'],
[30.0186205,31.5014854, 'AUC Avenue، Road، New Cairo 1, Cairo Governorate 11835, Egypt', 'American University in Cairo'],
[34.0489281,-111.0937311, 'Arizona, USA', 'Arizona State University'],
[38.0399391,23.8030901, 'Monumental Plaza, Building C, 1st Floor, Leof. Kifisias 44, Marousi 151 25, Greece', 'Athens Information Technology'],
[28.3588163,75.58802039999999, 'Vidya Vihar, Pilani, Rajasthan 333031, India', 'BITS Pilani'],
[6.891986300000001,3.7181286, '121103, Ilishan-Remo, Nigeria', 'Babcock University'],
[25.2677203,82.99125819999999, 'Ajagara, Varanasi, Uttar Pradesh 221005, India', 'Banaras Hindu University'],
[12.9504048,77.5020617, 'Mysore Rd, Jnana Bharathi, Bengaluru, Karnataka 560056, India', 'Bangalore University'],
[31.5488923,-97.1130573, '1311 S 5th St, Waco, TX 76706, USA', 'Baylor University'],
[39.9619537,116.3662615, '19 Xin Wai Da Jie, Beitaipingzhuang, Hai Dian Qu, Bei Jing Shi, China, 100875', 'Beijing normal university'],
[53.8930049,27.545623, 'prasp. Niezaliežnasci 4, Minsk, Belarus', 'Belarusian State University'],
[44.8184518,20.4575913, 'Studentski trg 1, Beograd, Serbia', 'Belgrade University'],
[42.5030333,-89.0309048, '700 College St, Beloit, WI 53511, USA', 'Beloit College'],
[53.8930049,27.545623, 'prasp. Niezaliežnasci 4, Minsk, Belarus', 'Belorussian State University'],
[31.261426,34.7995546, 'David Ben Gurion Blvd 1, Beer Sheva, Israel', 'Ben Gurion University'],
[10.6779085,78.74454879999999, 'Palkalaiperur, Tiruchirappalli, Tamil Nadu 620024, India', 'Bharthidasan University'],
[42.3504997,-71.1053991, 'Boston, MA 02215, USA', 'Boston University'],
[35.3050053,-120.6624942, 'San Luis Obispo, CA 93407, USA', 'California Polytechnic State University of San Luis Obispo'],
[34.1813584,-117.3231875, '5500 University Pkwy, San Bernardino, CA 92407, USA', 'California State University San Bernardino'],
[51.5210416,-0.1746649, '25 Paddington Grn, London W2 1NB, UK', 'City of Westminster College'],
[40.8075355,-73.9625727, 'New York, NY 10027, USA', 'Columbia University'],
[52.0740377,-0.6282057, 'College Rd, Cranfield, Wharley End, Bedford MK43 0AL, UK', 'Cranfield University'],
[50.1030364,14.3912841, '166 36 Prague 6, Czechia', 'Czech Technical University in Prague'],
[43.7044406,-72.2886934, 'Hanover, NH 03755, USA', 'Dartmouth'],
[37.3192827,-122.0447913, '21250 Stevens Creek Blvd, Cupertino, CA 95014, USA', 'De Anza College'],
[51.3769424,7.4946354, 'Universitätsstraße 11, 58097 Hagen, Germany', 'Distant University of Hagen'],
[48.4331922,35.0427966, 'Haharina Ave, 72, Dnipropetrovsk, Dnipropetrovska oblast, Ukraine, 49000', 'Dnipropetrovsk National University'],
[38.430691,27.13692, 'No: 144 35210, Alsancak, Cumhuriyet Blv, 35220 Konak/İzmir, Turkey', 'Dokuz Eylul University'],
[39.9566127,-75.18994409999999, '3141 Chestnut St, Philadelphia, PA 19104, USA', 'Drexel'],
[30.267153,-97.7430608, 'Austin, TX, USA', 'Drexel University and University of Texas at Austin'],
[36.0014258,-78.9382286, 'Durham, NC 27708, USA', 'Duke University'],
[45.7864448,4.7641329, '23 Av. Guy de Collongue, 69130 Écully, France', 'EM Lyon'],
[48.709445,2.1661629, 'CentraleSupélec, 3 Rue Joliot Curie, 91190 Gif-sur-Yvette, France', 'Ecole centrale de PARIS'],
[36.1056923,-79.5036508, '100 Campus Dr, Elon, NC 27244, USA', 'Elon University'],
[54.9134537,9.7780196, 'Alsion 4, 6400 Sønderborg, Denmark', 'Erhvervsakademi Sydvest'],
[-2.1480702,-79.9644896, 'Vía Perimetral 5, Guayaquil, Ecuador', 'Escuela Superior Politecnica del Litoral'],
[51.24683899999999,6.7916647, 'Münsterstraße 156, 40476 Düsseldorf, Germany', 'Fachhochschule Dusseldorf'],
[47.7233835,13.0871253, 'Urstein S 1, 5412 Salzburg, Austria', 'Fachhochschule FH Salzburg'],
[-23.6956191,-46.5469041, 'Av. Pereira Barreto, 400 - Vila Baeta Neves - Centro, São Bernardo do Campo - SP, 09751-000, Brazil', 'Faculdade de Tecnologia do Estado de Sao Paulo'],
[45.2461012,19.8516968, 'Trg Dositeja Obradovića 6, Novi Sad 106314, Serbia', 'Faculty of Technical Sciences Novi Sad Serbia'],
[40.7529167,-73.4266988, '2350 NY-110, Farmingdale, NY 11735, USA', 'Farmingdale State University'],
[-19.870682,-43.9677359, 'Av. Pres. Antônio Carlos, 6627 - Pampulha, Belo Horizonte - MG, 31270-901, Brazil', 'Federal University of Minas Gerais'],
[26.3749876,-80.10106329999999, '777 Glades Rd, Boca Raton, FL 33431, USA', 'Florida Atlantic University'],
[42.7789743,-72.05553929999999, '40 University Dr, Rindge, NH 03461, USA', 'Franklin Pierce College'],
[26.1540389,91.66296679999999, 'Gopinath Bordoloi Nagar, Jalukbari, Guwahati, Assam 781014, India', 'Gauhati University'],
[38.8298118,-77.3073606, '4400 University Dr, Fairfax, VA 22030, USA', 'George Mason University'],
[38.8977953,-77.0129087, '600 New Jersey Ave NW, Washington, DC 20001, USA', 'Georgetown University Law Center'],
[33.753068,-84.38528190000001, 'Atlanta, GA 30302, USA', 'Georgia State University'],
[42.9097484,-85.7630885, 'Grandville, MI, USA', 'Grandville'],
[50.87485419999999,4.7077677, 'Andreas Vesaliusstraat 13, 3000 Leuven, Belgium', 'Groep T University'],
[21.0070253,105.843136, '1 Đại Cồ Việt, Bách Khoa, Hai Bà Trưng, Hà Nội, Vietnam', 'Hanoi University of Science and Technology'],
[31.7945578,35.2414009, 'Jerusalem', 'Hebrew University'],
[17.4448649,78.34981379999999, 'Professor CR Rao Rd, Gachibowli, Hyderabad, Telangana 500032, India', 'IIIT Hyderabad'],
[26.5123388,80.2329, 'Kalyanpur, Kanpur, Uttar Pradesh 208016, India', 'IIT KANPUR'],
[58.595272,25.013607, 'Estonia', 'IT College of Estonia'],
[39.1784384,-86.5133166, '107 S Indiana Ave, Bloomington, IN 47405, USA', 'IU'],
[45.4377574,12.3223297, 'Santa Croce, 191, 30135 Venezia VE, Italy', 'IUAV Venezia'],
[41.8348731,-87.6270059, '10 W 35th St, Chicago, IL 60616, USA', 'Illinois Institute of Technology'],
[40.5116781,-88.9926996, '100 N University St, Normal, IL 61761, USA', 'Illinois State University Joliet Junior College'],
[12.9915639,80.2336857, 'Indian Institute Of Technology, Chennai, Tamil Nadu, India', 'Indian Institute of Technology'],
[22.3149274,87.31053109999999, 'Kharagpur, West Bengal 721302, India', 'Indian Institute of Technology Kharagpur India'],
[23.8142953,86.44118069999999, 'Police Line Road, Main Campus IIT (ISM, near Rani Bandh, IIT (ISM, Hirapur, Sardar Patel Nagar, Dhanbad, Jharkhand 826004, India', 'Indian School of Mines Dhanbad'],
[39.1784384,-86.5133166, '107 S Indiana Ave, Bloomington, IN 47405, USA', 'Indiana University'],
[39.1784384,-86.5133166, '107 S Indiana Ave, Bloomington, IN 47405, USA', 'Indiana University at Bloomington']
];
