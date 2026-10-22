TAM = 64 * 1024   # 64 KB por fragmento
 
def fragmentos(ruta):
    nombre = os.path.basename(ruta)
    with open(ruta, "rb") as f:
        while True:
            datos = f.read(TAM)
            if not datos:
                break
            yield imagenes_pb2.Fragmento(
                nombre=nombre, datos=datos)
 
def main(ruta):
    stub = imagenes_pb2_grpc.ImagenesStub(
        grpc.insecure_channel(SERVIDOR))
    r = stub.Subir(fragmentos(ruta),
                   wait_for_ready=True)
