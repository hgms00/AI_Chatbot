questions = {
    'A': 'Como você pretende viajar?' + '\n'
         + '\t' + '\t' + '1: Sozinho' + '\n'
         + '\t' + '\t' + '2: Casal' + '\n'
         + '\t' + '\t' + '3: Família' + '\n',

    'B': 'Qual seu principal objetivo na sua viagem?' + '\n'
         + '\t' + '\t' +'1: Visitar um lugar com abundância de pontos turísticos' + '\n'
         + '\t' + '\t' +'2: Aprender um novo idioma e conhecer novas pessoas' + '\n'
         + '\t' + '\t' +'3: Visitar pontos de entretiremento e compra' + '\n',

    'C': 'O que você busca fazer com seu parceiro?' + '\n'
         + '\t' + '\t' +'1: Ir para lugares românticos' + '\n'
         + '\t' + '\t' +'2: Se divertir juntos' + '\n'
         + '\t' + '\t' +'3: Experimentar das variedades da gastronomia' + '\n',

    'D': 'O que você quer fazer em família na sua viagem?' + '\n'
         + '\t' + '\t' +'1: Diversão em família' + '\n'
         + '\t' + '\t' +'2: Descanso em família' + '\n'
         + '\t' + '\t' +'3: Unir os laços familiares' + '\n',

    'E': 'Qual o tipo de ponto turístico que você prefere visitar?' + '\n'
         + '\t' + '\t' +'1: Pontos turísticos naturais' + '\n'
         + '\t' + '\t' +'2: Construções históricas' + '\n',

    'F': 'Dentre as línguas listadas, qual você mais gostaria de praticar?' + '\n'
         + '\t' + '\t' +'1: Inglês' + '\n'
         + '\t' + '\t' +'2: Francês' + '\n'
         + '\t' + '\t' +'3: Espanhol' + '\n',

    'G': 'Você prefere visitar playgrounds ou se divertir tentando a sorte em jogos de azar?' + '\n'
         + '\t' + '\t' +'1: Playgrounds' + '\n'
         + '\t' + '\t' +'2: Jogos de Azar' + '\n',

    'H': 'Vocês preferem um lugar com um clima frio?' + '\n'
         + '\t' + '\t' +'1: Sim' + '\n'
         + '\t' + '\t' +'2: Não' + '\n',

    'I': 'Vocês buscam aventuras inesquecíveis ou a diversão de um parque temático com um ar romântico?' + '\n'
         + '\t' + '\t' +'1: Aventuras' + '\n'
         + '\t' + '\t' +'2: Parques temáticos' + '\n',

    'J': 'Você prefere lugares onde você possa comer bastante massa?' + '\n'
         + '\t' + '\t' +'1: Sim' + '\n'
         + '\t' + '\t' +'2: Não' + '\n',

    'K': 'Você quer fazer esportes radicais com sua família?' + '\n'
         + '\t' + '\t' +'1: Sim' + '\n'
         + '\t' + '\t' +'2: Não' + '\n',

    'L': 'Vocês preferem ficar em contato com a natureza ou em um SPA?' + '\n'
         + '\t' + '\t' +'1: Natureza' + '\n'
         + '\t' + '\t' +'2: SPA' + '\n',
    'M': 'Você prefere acampar ou participar de exposições como um zoológico?' + '\n'
         + '\t' + '\t' +'1: Acampar' + '\n'
         + '\t' + '\t' +'2: Exposições' + '\n',
                          ''
    'N': 'Vocês buscam um lugar de clima quente ou frio?' + '\n'
         + '\t' + '\t' +'1: Frio' + '\n'
         + '\t' + '\t' +'2: Calor' + '\n',

    'O': 'Se refrescar em um parque aquático ou aproveitar das maravilhas de um parque temático?' + '\n'
         + '\t' + '\t' +'1: Temático' + '\n'
         + '\t' + '\t' +'2: Aquático' + '\n'
}

answer = {
    'A': ['a','b','c'],
    'B': ['d','e','f'],
    'C': ['g','h','i'],
    'D': ['j','k','l'],
    'E': ['m'],
    'F': ['n','o','p'],
    'G': ['q'],
    'H': ['r'],
    'I': ['s'],
    'J': ['t'],
    'K': ['u'],
    'L': ['v'],
    'M': ['w'],
    'N': ['x'],
    'O': ['y']
}
possible_answers = {
    'A': [['1', 'Sozinho', 'Individualmente', 'Individual', 'apenas eu' ], 
         ['2','Casal', 'Com o parceiro', 'Dupla'], 
         ['3','Em família', 'família', 'familia']],

    'B': [['1', 'Visitar um lugar com abundância de pontos turísticos', 'pontos turísticos', 'abundância de pontos turísticos'], 
         ['2', 'Aprender um idioma', 'conhecer pessoas novas', 'Aprender um novo idioma e conhecer pessoas novas','Aprender um novo idioma'], 
         ['3', 'Visitar pontos de entreterimento e compras', 'pontos de entreterimento', 'compras']],

    'C': [['1', 'Ir para lugares românticos', 'lugares românticos', 'lugares romanticos'], 
         ['2', 'Se divertir juntos', 'Se divertir', 'Diversão'], 
         ['3', 'Experimentar das variedades da gastronomia', 'experimentar', 'variedades da gastronomia', 'experimentar a gastronomia']],

    'D': [['1', 'Diversão em família', 'Diversão', 'Diversao em familia'], 
         ['2', 'Descanso em familia', 'Descanso', 'Descanso em familia'], 
         ['3', 'Unir os laços', 'União', 'Unir laços']],

    'E': [['1', 'Pontos turísticos naturais', 'Pontos turisticos naturais', 'naturais'], 
         ['2', 'Construções históricas', 'Construções']],

    'F': [['1', 'Inglês', 'Ingles'], 
         ['2', 'Francês', 'Frances'], 
         ['3', 'Espanhol']],

    'G': [['1', 'Playgrounds', 'Playground'], 
         ['2', 'Jogos de azar', 'Cassinos', 'Jogo de azar']],

    'H': [['1', 'Sim', 'Claro', 'Prefiro', 'Preferemos', 'Frio'], 
         ['2', 'Não', 'Nao', 'negativo', 'jamais', 'quente']],

    'I': [['1', 'Aventuras', 'Aventuras inesquecíveis', 'Aventuras inesqueciveis'], 
         ['2', 'Parques', 'Parques temáticos', 'Parque temático com um ar romântico', 'parque tematico com um ar romantico', 'parque temático romântico']],

    'J': [['1', 'Sim', 'Claro', 'Prefiro', 'Preferemos', 'massa'], 
         ['2', 'Não', 'Nao', 'negativo', 'não gosto de massa', 'odeio massa', 'nao gosto de massa']], 

    'K': [['1', 'Sim', 'Claro', 'Prefiro', 'Preferemos', 'adorariamos'], 
         ['2', 'Não', 'Nao', 'negativo', 'nunca', 'não gostamos de praticar esportes radicais']],  

    'L': [['1', 'Natureza', 'Contato com a natureza', 'Com a natureza'], 
         ['2', 'SPA', 'Em um SPA', 'Em SPA']], 

    'M': [['1', 'Acampar'], 
         ['2', 'Exposições', 'Zoológico', 'Exposições como um zoológico', 'Exposiçoes']],   

    'N': [['1', 'Frio', 'Clima frio'], 
         ['2', 'Calor', 'Quente', 'Clima quente']], 

    'O': [['1', 'Parque temático', 'temático', 'tematico', 'maravilhas de um parque temático'], 
         ['2', 'Parque aquático', 'aquatico', 'aquático', 'se refrescar em um parque aquático']], 
}
final_answers = {
    'P': 'Pacote Individual Austrália',
    'Q': 'Pacote Individual Peru',
    'R': 'Pacote Individual Inglaterra',
    'S': 'Pacote Individual França',
    'T': 'Pacote Individual Espanha',
    'U': 'Pacote Individual Áustria - Swarovski Kristallwelten',
    'V': 'Pacote Individual EUA - Las Vegas',
    'W': 'Pacote Casal Argentina - Bariloche',
    'X': 'Pacote Casal Ilhas Maldivas',
    'Y': 'Pacote Casal Turquia - Capadócia',
    'Z': 'Pacote Casal Dinamarca - Copenhague',
    '0': 'Pacote Casal Itália - Veneza',
    '1': 'Pacote Casal França - Paris',
    '2': 'Pacote Família Canadá',
    '3': 'Pacote Família Inglaterra',
    '4': 'Pacote Família EUA - Disney',
    '5': 'Pacote Família Dubai - Emirados Árabes - Aquaventure Waterpark',
    '6': 'Pacote Família Filipinas',
    '7': 'Pacote Família Estados Unidos',
    '8': 'Pacote Família Chile - Torres del Paine',
    '9': 'Pacote Família Alemanha - Jardim Zoológico de Berlim',
}

travelBotSpeechs = {
    'initial': ['Olá!!', 'Bem-vindo!', 'Oi!!!', 'Oi!!, tudo bom?', 'Saudações!!!'],
    'objective': ['TravelBot é um chat bot para te ajudar a planejar sua viagem dos sonhos',
                 'Eu, TravelBot, irei te ajudar a providenciar uma viagem perfeita!',
                 'Não sabe para onde quer ir? Deixe que eu cuide disso !',
                 'Parece que alguém quer viajar não é mesmo? Vamos escolher um lugar incrível para você ir']
}