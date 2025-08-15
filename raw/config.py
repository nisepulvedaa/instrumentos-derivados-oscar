nombre_evaluador="oscar" #solo primer nombre, sin espacios
nombre_proceso="instrumentos-derivados-slim-oscar" #nombre-proceso
version_arquetipo_raw="slim" #slim|full
periodicidad="diario"# diario|mensual|esporadico
##ORIGIN
buckets_detino="gs://dev-deinsoluciones-ingestas/files/"
path_destino="instrumentos-derivados-oscar"
nombre_archivo="instrumentos-derivados-oscar.parquet"
##RAW
proyecto="deinsoluciones-serverless"
dataset_raw_zone="dev_raw_zone"
nombre_tabla_raw="tbl_instrumento_derivado_dia_oscar"
campo_fecha_tabla_raw="fec_periodo"
fecha_ejecucion="2025-04-24"
ddl_raw="CREATE TABLE IF NOT EXISTS`deinsoluciones-serverless.dev_raw_zone.tbl_instrumento_derivado_dia_oscar` (fec_periodo DATE,cod_filial STRING,rut_deudor STRING,cod_operacion STRING,tip_derivado STRING,monto STRING,ind_netting STRING,sistema_origen STRING,fecha_carga TIMESTAMP ) PARTITION BY fec_periodo;"
##
correos_destinatarios="oscarmendozach@gmail.com"
