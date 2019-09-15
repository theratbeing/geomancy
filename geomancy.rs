#![allow(dead_code)]

/* TODO:
	make display for via puncti
	print house chart
	implement rng
	get user input
	get local time
	write log to file
	main event loop
	error handling
 */

pub mod color {
	// module containing ANSI color codes in 16-bit notation
	// makes names easier to look with color:: prefix
	pub const RESET		:&str = "\x1b[0m";
	pub const BLACK		:&str = "\x1b[38;5;0m";
	pub const RED		:&str = "\x1b[38;5;1m";
	pub const GREEN		:&str = "\x1b[38;5;2m";
	pub const YELLOW	:&str = "\x1b[38;5;3m";
	pub const BLUE		:&str = "\x1b[38;5;4m";
	pub const MAGENTA	:&str = "\x1b[38;5;5m";
	pub const CYAN		:&str = "\x1b[38;5;6m";
	pub const WHITE		:&str = "\x1b[38;5;7m";
	pub const B_BLACK	:&str = "\x1b[38;5;8m";
	pub const B_RED		:&str = "\x1b[38;5;9m";
	pub const B_GREEN	:&str = "\x1b[38;5;10m";
	pub const B_YELLOW	:&str = "\x1b[38;5;11m";
	pub const B_BLUE	:&str = "\x1b[38;5;12m";
	pub const B_MAGENTA	:&str = "\x1b[38;5;13m";
	pub const B_CYAN	:&str = "\x1b[38;5;14m";
	pub const B_WHITE	:&str = "\x1b[38;5;15m";
	pub const ORANGE	:&str = "\x1b[38;5;208m";
	pub const PURPLE	:&str = "\x1b[38;5;200m";
}

struct Virtue <'a> {
	// a struct containing information of an occult Virtue
	name	: &'a str,
	short	: &'a str,
	//symbol	: &'a str,		//too small, barely readable
	color	: &'a str,
}
impl <'a> Virtue <'_> {
	/* not usable for constants
	fn new(name: &'a str, short: &'a str, color: &'a str) -> Virtue<'a> {
		Virtue { name, short, color }
	}
	*/
	fn info( &self ) {
		println!( "name  : {}", self.name );
		println!( "short : {}", self.short );
		println!( "color : {}COLOR{}", self.color, color::RESET );
	}
	fn color_name( &self ) -> String {
		//full name with in color
		format!( "{}{}{}", 
			self.color, self.name, color::RESET )
	}
	fn color_short( &self ) -> String {
		//shortened name in color
		format!( "{}{}{}", 
			self.color, self.short, color::RESET )
	}
}

// Direct instantiation because can't use the function for constants

const X_ERROR	:Virtue = Virtue {
	name: "ERROR",	short: "!", color: color::B_RED };

// Element data
const E_FIRE	:Virtue = Virtue {
	name: "Fire",	short: "F", color: color::RED };
const E_AIR		:Virtue = Virtue {
	name: "Air",	short: "A", color: color::YELLOW };
const E_WATER	:Virtue = Virtue {
	name: "Water",	short: "W", color: color::BLUE };
const E_EARTH	:Virtue = Virtue {
	name: "Earth",	short: "E", color: color::GREEN };

// Planet data
const P_SATURN	:Virtue = Virtue {
	name: "Saturn",		short: "Sat", color: color::B_BLACK };
const P_JUPITER	:Virtue = Virtue {
	name: "Jupiter", 	short: "Jup", color: color::B_BLUE };
const P_MARS	:Virtue = Virtue {
	name: "Mars", 		short: "Mar", color: color::B_RED };
const P_SUN		:Virtue = Virtue {
	name: "Sun", 		short: "Sun", color: color::B_YELLOW };
const P_VENUS	:Virtue = Virtue {
	name: "Venus", 		short: "Ven", color: color::B_GREEN };
const P_MERCURY	:Virtue = Virtue {
	name: "Mercury",	short: "Mer", color: color::ORANGE };
const P_MOON	:Virtue = Virtue {
	name: "Moon", 		short: "Mon", color: color::PURPLE };
const P_NODE_N	:Virtue = Virtue {
	name: "North Node", short: "Nor", color: color::B_WHITE };
const P_NODE_S	:Virtue = Virtue {
	name: "South Node", short: "Sou", color: color::WHITE };

// Zodiac data. Name is 6 letters
const Z_ARIES	:Virtue = Virtue {
	name: "Aries",		short: "Ari", color: color::RED };
const Z_LEO		:Virtue = Virtue {
	name: "Leo",		short: "Leo", color: color::RED };
const Z_SAGITT	:Virtue = Virtue {
	name: "Sagittarius",short: "Sag", color: color::RED };
const Z_CAPRIC	:Virtue = Virtue {
	name: "Capricorn",	short: "Cap", color: color::GREEN };
const Z_TAURUS	:Virtue = Virtue {
	name: "Taurus",		short: "Tau", color: color::GREEN };
const Z_VIRGO	:Virtue = Virtue {
	name: "Virgo",		short: "Vir", color: color::GREEN };
const Z_LIBRA	:Virtue = Virtue {
	name: "Libra",		short: "Lib", color: color::YELLOW };
const Z_AQUARI	:Virtue = Virtue {
	name: "Aquarius",	short: "Aqu", color: color::YELLOW };
const Z_GEMINI	:Virtue = Virtue {
	name: "Gemini",		short: "Gem", color: color::YELLOW };
const Z_CANCER	:Virtue = Virtue {
	name: "Cancer",		short: "Can", color: color::BLUE };
const Z_SCORPI	:Virtue = Virtue {
	name: "Scorpio",	short: "Sco", color: color::BLUE };
const Z_PISCES	:Virtue = Virtue {
	name: "Pisces",		short: "Pis", color: color::BLUE };

struct Figure<'a> {
	/* this contains all relevant info of a geomantic figure
	 * element1 : traditional elements
	 * element2 : modern elements
	 * zodiac1	: Gerardus of Cremona
	 * zodiac2	: H.C. Agrippa
	 * */
	name    : &'a str,
	points  : [i32; 4],
	lines   : [&'a str; 4],
	element1: Virtue <'a>,
	element2: Virtue <'a>,
	planet  : Virtue <'a>,
	zodiac1 : Virtue <'a>,
	zodiac2 : Virtue <'a>,
	meaning : &'a str,
	manzil  : &'a str,
}

impl Figure <'_> {
	fn info( &self ) {
		println!( "\tName\t: {}", self.name );
		println!( "  {}\tElement\t: {}{}{x} (Traditional) {}{}{x} (Modern)",
			self.lines[0],
			self.element1.color, self.element1.name,
			self.element2.color, self.element2.name, x = color::RESET );
		println!( "  {}\tPlanet\t: {}{}{}",
			self.lines[1],
			self.planet.color, self.planet.name, color::RESET );
		println!( "  {}\tZodiac\t: {}{}{x} (Gerardus) {}{}{x} (Agrippa)",
			self.lines[2],
			self.zodiac1.color, self.zodiac1.name,
			self.zodiac2.color, self.zodiac2.name, x = color::RESET );
		println!( "  {}\tMansion\t: {}", self.lines[3], self.manzil );
		println!( "\tMeaning\t: {}", self.meaning );
	}
}

// I and O for visibility
const I_I :&str = " ● ";
const O_O :&str = "● ●";
const X_X :&str = "???";
// text representation for all figures because
// I don't know how to use vectors
const L_VIA :[&str; 4] = [I_I, I_I, I_I, I_I];
const L_CAU :[&str; 4] = [I_I, I_I, I_I, O_O];
const L_PUR :[&str; 4] = [I_I, I_I, O_O, I_I];
const L_MIN :[&str; 4] = [I_I, I_I, O_O, O_O];
const L_PUL :[&str; 4] = [I_I, O_O, I_I, I_I];
const L_AMI :[&str; 4] = [I_I, O_O, I_I, O_O];
const L_CAR :[&str; 4] = [I_I, O_O, O_O, I_I];
const L_LAE :[&str; 4] = [I_I, O_O, O_O, O_O];
const L_CAP :[&str; 4] = [O_O, I_I, I_I, I_I];
const L_CON :[&str; 4] = [O_O, I_I, I_I, O_O];
const L_ACQ :[&str; 4] = [O_O, I_I, O_O, I_I];
const L_RUB :[&str; 4] = [O_O, I_I, O_O, O_O];
const L_MAJ :[&str; 4] = [O_O, O_O, I_I, I_I];
const L_ALB :[&str; 4] = [O_O, O_O, I_I, O_O];
const L_TRI :[&str; 4] = [O_O, O_O, O_O, I_I];
const L_POP :[&str; 4] = [O_O, O_O, O_O, O_O];
const L_ERR :[&str; 4] = [X_X, X_X, X_X, X_X];

const F_ERR : Figure = Figure {
	// error dummy for use until I get error handling right
	name	: "ERROR",		points	: [0, 0, 0, 0], lines	: L_ERR,
	element1: X_ERROR,		element2: X_ERROR,		planet	: X_ERROR,
	zodiac1	: X_ERROR,		zodiac2 : X_ERROR,
	meaning : "Array mismatch",
	manzil	: "ERROR",
};

const F_VIA : Figure = Figure {
	name	: "Via",		points	: [1, 1, 1, 1], lines	: L_VIA,
	element1: E_WATER,		element2: E_WATER,		planet	: P_MOON,
	zodiac1	: Z_LEO,		zodiac2 : Z_CANCER,
	meaning : "Road, journey, change of fortune.",
	manzil	: "10. Al-Jab'hah",
};
const F_POP : Figure = Figure {
	name	: "Populus",	points	: [2, 2, 2, 2], lines	: L_POP,
	element1: E_WATER,		element2: E_WATER,		planet	: P_MOON,
	zodiac1	: Z_CAPRIC,		zodiac2 : Z_CANCER,
	meaning : "Crowd, multitude, assembly. Neutral figure.",
	manzil	: "20. An-Na‘āʾam",
};
const F_LAE : Figure = Figure {
	name	: "Laetitia",	points	: [1, 2, 2, 2], lines	: L_LAE,
	element1: E_AIR,		element2: E_FIRE,		planet	: P_JUPITER,
	zodiac1	: Z_TAURUS,		zodiac2 : Z_PISCES,
	meaning : "Happiness and good health.",
	manzil	: "4. Ad-Dabarān",
};
const F_TRI : Figure = Figure {
	name	: "Tristitia",	points	: [2, 2, 2, 1], lines	: L_TRI,
	element1: E_EARTH,		element2: E_EARTH,		planet	: P_SATURN,
	zodiac1	: Z_SCORPI,		zodiac2 : Z_AQUARI,
	meaning : "Sorrow, illness. Bad except for land and agriculture.",
	manzil	: "19. Ash-Shawlah",
};
const F_RUB : Figure = Figure {
	name	: "Rubeus",		points	: [2, 1, 2, 2], lines	: L_RUB,
	element1: E_FIRE,		element2: E_AIR,		planet	: P_MARS,
	zodiac1	: Z_GEMINI,		zodiac2 : Z_SCORPI,
	meaning : "Passion, vice, hot temper. Unfavorable. \
	In 1st position it means the querent is dishonest.",
	manzil	: "6. Al-Han‘ah",
};
const F_ALB : Figure = Figure {
	name	: "Albus",		points	: [2, 2, 1, 2], lines	: L_ALB,
	element1: E_WATER,		element2: E_WATER,		planet	: P_MERCURY,
	zodiac1	: Z_CANCER,		zodiac2 : Z_GEMINI,
	meaning : "Peace, wisdom, patience. Favorable but weak.",
	manzil	: "8. An-Nathrah, 9. Aṭ-Ṭarf",
};
const F_PUL : Figure = Figure {
	name	: "Puella",		points	: [1, 2, 1, 1], lines	: L_PUL,
	element1: E_WATER,		element2: E_WATER,		planet	: P_VENUS,
	zodiac1	: Z_LIBRA,		zodiac2 : Z_LIBRA,
	meaning : "Female, beauty. Good figure but fickle.",
	manzil	: "5. Al-Haq‘ah",
};
const F_PUR : Figure = Figure {
	name	: "Puer",		points	: [1, 1, 2, 1], lines	: L_PUR,
	element1: E_AIR,		element2: E_AIR,		planet	: P_MARS,
	zodiac1	: Z_GEMINI,		zodiac2 : Z_ARIES,
	meaning : "Male, power, reckless action. Bad except for love and war.",
	manzil	: "15. Al-Ghafr, 16. Az-Zubānā",
};
const F_ACQ : Figure = Figure {
	name	: "Acquisitio",	points	: [2, 1, 2, 1], lines	: L_AMI,
	element1: E_AIR,		element2: E_AIR,		planet	: P_JUPITER,
	zodiac1	: Z_ARIES,		zodiac2 : Z_SAGITT,
	meaning : "Gain.",
	manzil	: "1. An-Naṭḥ, 2. Al-Buṭayn",
};
const F_AMI : Figure = Figure {
	name	: "Amissio",	points	: [1, 2, 1, 2], lines	: L_AMI,
	element1: E_FIRE,		element2: E_FIRE,		planet	: P_VENUS,
	zodiac1	: Z_SCORPI,		zodiac2 : Z_TAURUS,
	meaning : "Loss. Bad for wealth but good for love.",
	manzil	: "17. Al-Iklīl",
};
const F_CON : Figure = Figure {
	name	: "Conjunctio",	points	: [2, 1, 1, 2], lines	: L_CON,
	element1: E_AIR,		element2: E_AIR,		planet	: P_MERCURY,
	zodiac1	: Z_VIRGO,		zodiac2 : Z_VIRGO,
	meaning : "Combination, mixed results.",
	manzil	: "14. As-Simāk",
};
const F_CAR : Figure = Figure {
	name	: "Carcer",		points	: [1, 2, 2, 1], lines	: L_CAR,
	element1: E_FIRE,		element2: E_FIRE,		planet	: P_SATURN,
	zodiac1	: Z_PISCES,		zodiac2 : Z_CAPRIC,
	meaning : "Restriction, obstacle.",
	manzil	: "28. Ar-Rashāʾ",
};
const F_CAP : Figure = Figure {
	name	: "Caput Draconis", points	: [2, 1, 1, 1], lines	: L_CAP,
	element1: E_EARTH,		element2: E_EARTH,		planet	: P_NODE_N,
	zodiac1	: Z_VIRGO,		zodiac2 : Z_VIRGO,
	meaning : "Beginnings, ascending movement. Favorable.",
	manzil	: "13. Al-‘Awwāʾ",
};
const F_CAU : Figure = Figure {
	name	: "Cauda Draconis",	points	: [1, 1, 1, 2], lines	: L_CAU,
	element1: E_FIRE,		element2: E_FIRE,		planet	: P_NODE_S,
	zodiac1	: Z_SAGITT,		zodiac2 : Z_VIRGO,
	meaning : "Endings, descending movement. Unfavorable. \
	In 1st position it means the querent won't change his/her view.",
	manzil	: "21. Al-Baldah",
};
const F_MAJ : Figure = Figure {
	name	: "Fortuna Major",	points	: [2, 2, 1, 1], lines	: L_MAJ,
	element1: E_EARTH,		element2: E_EARTH,		planet	: P_SUN,
	zodiac1	: Z_AQUARI,		zodiac2 : Z_LEO,
	meaning : "Success through one's own effort. Good for beginnings.",
	manzil	: "3. Ath-Thurayyā",
};
const F_MIN : Figure = Figure {
	name	: "Fortuna Minor",	points	: [1, 1, 2, 2], lines	: L_MIN,
	element1: E_FIRE,		element2: E_FIRE,		planet	: P_SUN,
	zodiac1	: Z_TAURUS,		zodiac2 : Z_LEO,
	meaning : "Outside help, outer honor, quick result. Good for endings.",
	manzil	: "25. Al-ʾAkhbiyyah, 26. Al-Muqdim, 27. Al-Muʾkhar",
};

// Indices for shield chart
const MOTHER	: usize	=  0; // + 1..3
const DAUGHTER	: usize	=  4;
const NIECE		: usize	=  8;
const WITNESS	: usize	= 12; // + 1
const JUDGE		: usize	= 14; // + 1 = Reconciler
const CHART_SIZE: usize = 16;

struct Chart <'a> {
	array	: Vec <[i32;4]>,
	figures	: Vec <Figure <'a>>,
}

impl Chart <'_> {
	fn add_figures(a :[i32; 4], b :[i32; 4]) -> [i32; 4] {
		let mut output = [1, 1, 1, 1];
		for lin in 0..4 {
			if a[lin] == b[lin] { output[lin] = 2; }
		}
		output
	}
	
	fn array2figure <'a> ( array :[i32; 4] ) -> Figure <'a> {
		match array {
			[1, 1, 1, 1] => F_VIA,
			[1, 1, 1, 2] => F_CAU,
			[1, 1, 2, 1] => F_PUR,
			[1, 1, 2, 2] => F_MIN,
			[1, 2, 1, 1] => F_PUL,
			[1, 2, 1, 2] => F_AMI,
			[1, 2, 2, 1] => F_CAR,
			[1, 2, 2, 2] => F_LAE,
			[2, 1, 1, 1] => F_CAP,
			[2, 1, 1, 2] => F_CON,
			[2, 1, 2, 1] => F_ACQ,
			[2, 1, 2, 2] => F_RUB,
			[2, 2, 1, 1] => F_MAJ,
			[2, 2, 1, 2] => F_ALB,
			[2, 2, 2, 1] => F_TRI,
			[2, 2, 2, 2] => F_POP,
			_			 => F_ERR,
		}
	}
	
	fn array2chart(
		a :[i32;4], b :[i32;4], c :[i32;4],
		d :[i32;4] ) -> Vec<[i32;4]> {
		
		// takes 4 [i32;4] arrays and return a vecor with 16 arrays
		let mut output :Vec<[i32;4]> = vec![];
		output.push(a);
		output.push(b);
		output.push(c);
		output.push(d);
	
		//transposition; array length is 4
		for i in 0..4 {
			output.push([a[i], b[i], c[i], d[i]]);
		}
	
		/* add the array figures together
		* MOTHER		DAUGHTER
		* 0- 1;  2- 3;  4- 5;  6-7;
		* NIECE			WITNESS 	JUDGE
		* 8- 9; 10-11; 12-13; 		14-0;
		*/
		for i in 0..7 {
			let x = i * 2;
			let y = x + 1;
			output.push(Chart::add_figures(output[x], output[y]));
		}
		output.push(Chart::add_figures(output[JUDGE], output[MOTHER]));
		output
	}
	
	fn new <'a> (
		a :[i32;4], b :[i32;4],
		c :[i32;4], d :[i32;4])  -> Chart <'a> {
		
		let array :Vec<[i32;4]> = Chart::array2chart(a, b, c, d);
		let mut figures :Vec<Figure> = vec![];
		for ar in array.iter() {
			figures.push(Chart::array2figure(*ar));
		}
		Chart { array, figures }
	}
	
	fn same_in_row( source :&[&i32; 4] ) -> i32 {
		// needed for Via Puncti
		let head = source[0];
		let mut score :i32 = 0;
		for n in source.iter() {
			if *n != head { break; }
			score += 1;
		}
		score
	}

	fn max_in_list( source :&Vec<i32> ) -> i32 {
		// Via Puncti
		let mut score :i32 = 0;
		for n in source.iter() {
			if *n > score {
				score = *n;
			}
		}
		score
	}
	
	fn calculate_vp( &self ) -> Vec<i32> {
		/* Take first line of every figure, see if they are same with judge's.
		 * Outputs a vector containing only branches of Via Puncti with maximum
		 * score. Lots of `let` statement for maximum READIBILITY
		 * I could use arrays directly but every line would be too long~
		 */
		let p_judge = &self.array[JUDGE][0];
		let p_right = &self.array[WITNESS][0];
		let p_left  = &self.array[WITNESS+1][0];
		let p_niec1 = &self.array[NIECE][0];
		let p_niec2 = &self.array[NIECE+1][0];
		let p_niec3 = &self.array[NIECE+2][0];
		let p_niec4 = &self.array[NIECE+3][0];
		let p_daug1 = &self.array[DAUGHTER][0];
		let p_daug2 = &self.array[DAUGHTER+1][0];
		let p_daug3 = &self.array[DAUGHTER+2][0];
		let p_daug4 = &self.array[DAUGHTER+3][0];
		let p_moth1 = &self.array[MOTHER][0];
		let p_moth2 = &self.array[MOTHER+1][0];
		let p_moth3 = &self.array[MOTHER+2][0];
		let p_moth4 = &self.array[MOTHER+3][0];
		
		/* Branches goes like this:
		 *									Mother 1	branch1
		 *						Niece 1		Mother 2	branch2
		 *			R. Witness <
				   /			Niece 2		Mother 3	branch3
				   |						Mother 4	branch4
		 * Judge <
		 *			L. Witness, etc.
		 */
		 
		let branch1 = [p_judge, p_right, p_niec1, p_moth1];
		let branch2 = [p_judge, p_right, p_niec1, p_moth2];
		let branch3 = [p_judge, p_right, p_niec2, p_moth3];
		let branch4 = [p_judge, p_right, p_niec2, p_moth4];
		let branch5 = [p_judge, p_left, p_niec3, p_daug1];
		let branch6 = [p_judge, p_left, p_niec3, p_daug2];
		let branch7 = [p_judge, p_left, p_niec4, p_daug3];
		let branch8 = [p_judge, p_left, p_niec4, p_daug4];
		
		let tree = [branch1, branch2, branch3, branch4,
					branch5, branch6, branch7, branch8];
		
		// see how many same number in a row
		let mut tree_map :Vec<i32> = vec![];
		for branch in tree.iter() {
			tree_map.push(Chart::same_in_row(branch));
		}
		
		// we only need to know the longest chain
		// 8 branches -> vector length 8
		let maximum = Chart::max_in_list(&tree_map);
		for i in 0..8 {
			if tree_map[i] < maximum {
				tree_map[i] = 0;
			}
		}
		
		// remove duplicates but keep first occurence intact
		if maximum == 1 { tree_map = [1, 0, 0, 0, 0, 0, 0, 0].to_vec(); }
		
		// exception: number 2 may appear twice in specific places
		for n in 0..4 {
			if tree_map[n] == 2 {
				tree_map[0] = 2;
				tree_map[1] = 0;
				tree_map[2] = 0;
				tree_map[3] = 0;
			}
		}
		for n in 4..8 {
			if tree_map[n] == 2 {
				tree_map[4] = 2;
				tree_map[5] = 0;
				tree_map[6] = 0;
				tree_map[7] = 0;
			}
		}
		
		// no exception here
		if maximum == 3 {
			for i in 0..4 {
				let a = i*2;
				let b = a+1;
				if tree_map[a] == tree_map[b] { tree_map[b] = 0; } 
			}
		}
		
		tree_map
	}
	
	fn draw_shield( &self ) {
		// store our strings in a vector before printing them
		let mut chart_panel :Vec<String> = vec![];
		chart_panel.push( format!("┏{}━━━━━┓", "━━━━━┯".repeat(7)) );
		
		// 1-4 : mothers; 5-8 : daughters;
		chart_panel.push(
		format!("┃  8  │  7  │  6  │  5  │  4  │  3  │  2  │  1  ┃"));
		
		let m1 :&Figure = &self.figures[MOTHER];
		let m2 :&Figure = &self.figures[MOTHER+1];
		let m3 :&Figure = &self.figures[MOTHER+2];
		let m4 :&Figure = &self.figures[MOTHER+3];
		let d1 :&Figure = &self.figures[DAUGHTER];
		let d2 :&Figure = &self.figures[DAUGHTER+1];
		let d3 :&Figure = &self.figures[DAUGHTER+2];
		let d4 :&Figure = &self.figures[DAUGHTER+3];
		
		for i in 0..4 {
			chart_panel.push(
				format!("┃{}{:^5}{x}│{}{:^5}{x}│{}{:^5}{x}│{}{:^5}{x}\
						│{}{:^5}{x}│{}{:^5}{x}│{}{:^5}{x}│{}{:^5}{x}┃",
				// order is right to left (reversed)
				d4.element1.color, d4.lines[i], d3.element1.color, d3.lines[i],
				d2.element1.color, d2.lines[i], d1.element1.color, d1.lines[i],
				m4.element1.color, m4.lines[i], m3.element1.color, m3.lines[i],
				m2.element1.color, m2.lines[i], m1.element1.color, m1.lines[i],
				x=color::RESET) );
		}
		
		chart_panel.push(format!("┠{}─────┴─────┨", "─────┴─────┼".repeat(3)));
		chart_panel.push(format!("┃{:^11}│{:^11}│{:^11}│{:^11}┃",
			"12", "11", "10", "9"));
		
		let n1 :&Figure = &self.figures[NIECE];
		let n2 :&Figure = &self.figures[NIECE+1];
		let n3 :&Figure = &self.figures[NIECE+2];
		let n4 :&Figure = &self.figures[NIECE+3];
		for i in 0..4 {
			chart_panel.push(
				format!("┃{}{:^11}{x}│{}{:^11}{x}│{}{:^11}{x}│{}{:^11}{x}┃",
				n4.element1.color, n4.lines[i], n3.element1.color, n3.lines[i],
				n2.element1.color, n2.lines[i], n1.element1.color, n1.lines[i],
				x=color::RESET));
		}
		chart_panel.push(format!("┠{x}┴{x}┼{x}┴{x}┨", x="─".repeat(11)));
		chart_panel.push(format!("┃{:^23}│{:^23}┃", "Left", "Right"));
		
		let c1 :&Figure = &self.figures[WITNESS];
		let c2 :&Figure = &self.figures[WITNESS+1];
		for i in 0..4 {
			chart_panel.push(format!("┃{}{:^23}{x}│{}{:^23}{x}┃",
				c2.element1.color, c2.lines[i], c1.element1.color, c1.lines[i],
				x=color::RESET));
		}
		chart_panel.push(
			format!("┠{}┴{}┬─────┨", "─".repeat(23), "─".repeat(17)));
		
		chart_panel.push(format!("┃{:>26}{}│{:^5}┃",
			"Judge", " ".repeat(15), "Rc"));
		
		let c3 :&Figure = &self.figures[JUDGE];
		let c4 :&Figure = &self.figures[JUDGE+1];
		for i in 0..4 {
			chart_panel.push(format!("┃{}{:>25}{x}{}│{}{:^5}{x}┃",
				c3.element1.color, c3.lines[i], " ".repeat(16),
				c4.element1.color, c4.lines[i], x=color::RESET));
		}
		chart_panel.push(format!("┗{}┷━━━━━┛", "━".repeat(41)));
		
		// construct the right-side panel
		let mut name_panel :Vec<String> = vec![];
		// panel width is 31 chars
		name_panel.push(format!("╭{}╮", "─".repeat(29)));
		for line in 0..CHART_SIZE {
			if line == MOTHER {
				name_panel.push(format!("│{:^29}│", "Mothers"));
			} else if line == DAUGHTER {
				name_panel.push(format!("│{}│", " ".repeat(29)));
				name_panel.push(format!("│{:^29}│", "Daughters"));
			} else if line == NIECE {
				name_panel.push(format!("│{}│", " ".repeat(29)));
				name_panel.push(format!("│{:^29}│", "Nieces"));
			} else if line == WITNESS {
				name_panel.push(format!("│{}│", " ".repeat(29)));
				name_panel.push(format!("│{:^29}│", "Court"));
			}
			
			// shorthand for properties makes formatting easier
			let name	:&str = &self.figures[line].name;
			let f_color :&str = &self.figures[line].element1.color;
			let element :&Virtue = &self.figures[line].element1;
			let planet	:&Virtue = &self.figures[line].planet;
			let zodiac	:&Virtue = &self.figures[line].zodiac1;
			// labels for named figures
			let mut label :Vec<String> = vec![];
			for i in 0..WITNESS { label.push(format!("{}", i+1)); }
			label.push("Ri".to_string());
			label.push("Le".to_string());
			label.push("Ju".to_string());
			label.push("Rc".to_string());
			
			name_panel.push(
			format!("│ {d:>2} {cl}{n:<14} {ec}{en} {pc}{pn} {zc}{zn}{x} │",
					cl=f_color, n=name, ec=element.color, en=element.short,
					pc=planet.color, pn=planet.short, zc=zodiac.color,
					zn=zodiac.short, d=label[line], x=color::RESET));
		}
		// close the panel
		name_panel.push(format!("╰{}╯", "─".repeat(29)));
		// print them side-by-side
		for line in 0..chart_panel.len() {
			println!("{}{}", chart_panel[line], name_panel[line]);
		}
	}
}

fn main() {

	println!( "Testing!" );
	
	println!("\nLet's make a new chart!");
	
	let test:Chart = Chart::new(
		[1, 2, 1, 1], [2, 2, 2, 2], [1, 1, 2, 2], [2, 2, 1, 1]);
	
	let judge = &test.figures[JUDGE];
	judge.info();
	test.draw_shield();
	
	println!("\nWay of Points simulation");
	let wop = test.calculate_vp();
	println!("{:?}", wop);
	/*
	//4 mothers are from user input
	println!("\nCreating the first mother.");
	let m1: [i32; 4] = figure_from_text();
	
	println!("\nCreating the second mother.");
	let m2: [i32; 4] = figure_from_text();
	
	println!("\nCreating the third mother.");
	let m3: [i32; 4] = figure_from_text();
	
	println!("\nCreating the fourth mother.");
	let m4: [i32; 4] = figure_from_text();

	println!("\nThe mothers are:\n{:?} {:?} {:?} {:?}",
		m1, m2, m3, m4);
	
	*/
}

fn user_input() -> String {
	use std::io;
	let mut answer = String::new();
	io::stdin().read_line(&mut answer)
		.expect("Failed to read line");
	answer
}

fn figure_from_text() -> [i32; 4] {
	println!("Please enter 4 lines of text.");
	let mut output :[i32; 4] = [1, 1, 1, 1];
	//Ask input and calculate the parity
	for lin in 0..4 {
		let input = user_input();
		if input.len() % 2 == 0 { output[lin] = 2; }
	}
	output
}
