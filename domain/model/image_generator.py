from venv import logger
import tensorflow as tf
import tensorflow_hub as hub
import tarfile
import os

class ImageGenerator:
    def __init__(self):
        model_tar_path = 'infra/repository/biggan-deep-256_1.tar.gz'
        extract_path = 'infra/repository/biggan-deep-256'

        model_dir = self.extract_model(model_tar_path, extract_path)
        self.model = hub.load(model_dir)
        self.truncation = 0.5  # você pode querer tornar isso configurável

    def train(self, dataloader, epochs=10):
        pass  # O BigGAN é um modelo pré-treinado, então não precisamos treiná-lo novamente

    def generate(self, text):
        logger.info(f"Generating image for text: {text}")
        # Primeiro, você precisa converter o texto em uma representação numérica.
        # Isso depende de como você quer representar o texto. Aqui, estou apenas
        # mostrando um exemplo onde cada caractere é convertido em seu valor ASCII.
        input_vector = [ord(c) for c in text]

        # Em seguida, você precisa converter a entrada em um tensor.
        # O tensor de entrada para o BigGAN deve ser um tensor 1D de tamanho 128.
        # Portanto, você pode precisar truncar ou preencher com zeros o seu vetor de entrada.
        input_vector = input_vector[:128]  # Trunca a entrada para 128 elementos
        input_vector += [0] * (128 - len(input_vector))  # Preenche com zeros se a entrada for curta

        # Converte a entrada em um tensor e adiciona uma dimensão extra no início
        input_tensor = tf.convert_to_tensor([input_vector], dtype=tf.float32)

        # Agora você pode passar o tensor de entrada para o modelo.
        # O modelo retorna um tensor 4D com a forma [batch_size, height, width, channels].
        # Como o nosso batch_size é 1, nós apenas pegamos o primeiro item do batch.
        output_tensor = self.model(input_tensor, truncation=self.truncation)[0]

        # A saída do modelo está no intervalo [-1, 1]. 
        # Nós escalamos isso para o intervalo [0, 255] e convertemos para inteiros para criar uma imagem.
        image = tf.cast((output_tensor + 1) / 2 * 255, tf.uint8)

        # Finalmente, convertemos o tensor de imagem em uma imagem PIL para visualização ou salvamento.
        image = image.fromarray(image.numpy())

        return image
    

    def extract_model(self, model_tar_path, extract_path):
        # Verifica se o diretório de extração existe, se não, cria.
        os.makedirs(extract_path, exist_ok=True)
        
        with tarfile.open(model_tar_path, 'r:gz') as tar:
            tar.extractall(path=extract_path)
        
        # Retorna o caminho do diretório onde o modelo foi extraído
        return extract_path


