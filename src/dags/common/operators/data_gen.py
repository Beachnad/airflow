from typing import Callable
import pandas as pd

from airflow.operators import BaseOperator
from airflow.hooks.postgres_hook import PostgresHook


class PandasToPostgresOperator(BaseOperator):
    template_fields = ('destination_table', 'preoperator', 'fun_args')
    template_ext = ('.sql', '.hql',)
    ui_color = '#42cef5'

    def __init__(
            self,
            destination_conn_id: str,
            destination_table: str,
            fun: Callable[..., pd.DataFrame],
            fun_args=None,
            preoperator: str = None,
            *args, **kwargs
    ):
        super(PandasToPostgresOperator, self).__init__(*args, **kwargs)
        self.destination_conn_id = destination_conn_id
        self.destination_table = destination_table
        self.preoperator = preoperator
        self.fun = fun
        self.fun_args = fun_args

    def get_data_frame(self):
        df = self.fun(*self.fun_args)
        return df

    def execute(self, context):
        df = self.get_data_frame()
        if df is not None:
            destination_hook = PostgresHook.get_hook(self.destination_conn_id)
            if self.preoperator:
                self.log.info("Running preoperator")
                self.log.info(self.preoperator)
                destination_hook.run(self.preoperator)

            self.log.info(f"Inserting data frame into {self.destination_conn_id}")
            destination_hook.insert_rows(table=self.destination_table, rows=df.itertuples())

