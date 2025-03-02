# QR Code Scanner com Webcam

Este é um script simples em Python que usa a webcam do seu computador para escanear códigos QR ou de barras. Quando um código é detectado, ele exibe as informações na tela e copia o conteúdo do código para a área de transferência.

---

## Como funciona?

1. **Captura de Vídeo**: O script usa a webcam para capturar frames em tempo real.
2. **Detecção de Códigos**: Ele converte cada frame para tons de cinza e tenta detectar códigos QR ou de barras usando a biblioteca `pyzbar`.
3. **Exibição e Cópia**: Se um código for detectado, ele é destacado na tela com um retângulo vermelho, e o texto do código é exibido e copiado para a área de transferência.
4. **Sair**: Pressione a tecla `ESC` para fechar o programa.

---

## Dependências

As bibliotecas necessárias estão listadas no arquivo `requirements.txt`:

```plaintext
numpy==2.2.3
opencv-python==4.11.0.86
pyperclip==1.9.0
pyzbar==0.1.9
```

---

## Tutorial: Como configurar e rodar o projeto

### Passo 1: Criar um ambiente virtual (venv)

1. Abra o terminal (ou prompt de comando) no diretório do seu projeto.
2. Crie um ambiente virtual com o comando:
   ```bash
   python -m venv venv
   ```
   Isso criará uma pasta chamada `venv` no seu diretório.

3. Ative o ambiente virtual:
   - **No Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **No macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

   Após ativar, você verá o nome do ambiente virtual (`venv`) no início do prompt do terminal.

---

### Passo 2: Instalar as dependências

1. Com o ambiente virtual ativado, instale as dependências usando o arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

2. Isso instalará todas as bibliotecas necessárias com as versões corretas.

---

### Passo 3: Executar o script

1. Salve o código do scanner em um arquivo Python, por exemplo, `qr_scanner.py`.
2. Execute o script:
   ```bash
   python qr_scanner.py
   ```
3. Aponte a webcam para um código QR ou de barras e veja o resultado na tela. O texto do código será copiado automaticamente para a área de transferência.

4. Para sair do programa, pressione a tecla `ESC`.

---

## Exemplo de Uso

- **Leitura de Códigos QR**: Aponte a câmera para um QR Code e o texto será copiado automaticamente.
- **Leitura de Códigos de Barras**: Funciona da mesma forma que os QR Codes.

---

