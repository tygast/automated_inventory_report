# -*- coding: utf-8 -*-
import urllib

import cx_Oracle
from sqlalchemy import create_engine


class db_connect:
    @classmethod
    def Engine_A(cls):
        """
        returns an sqlalchemy engine to Database_A
        """
        db_dsn = cx_Oracle.makedsn(
            host="database_a.company.com",
            port=1521,
            service_name="DATABASE_A_NAME.COMPANY.COM",
        )
        return create_engine("oracle+cx_oracle://user_name:password@%s" % db_dsn)

    @classmethod
    def Engine_B(cls):
        """
        returns an sqlalchemy engine to Database_B
        """
        db_params = urllib.parse.quote(
            "DRIVER={SQL Server};SERVER=DATABASE_B_NAME;DATABASE=Database_B;UID=user_name;PWD=password"
        )

        return create_engine("mssql+pyodbc:///?odbc_connect=%s" % db_params)

    @classmethod
    def Engine_C(cls):
        """
        This creates an engine that connects to Database_C
        """
        db_dsn = cx_Oracle.makedsn(
            host="database_c.company.com",
            port=1521,
            service_name="DATABASE_C_NAME.COMPANY.COM",
        )
        return create_engine("oracle+cx_oracle://user_name:password@%s" % db_dsn)

    @classmethod
    def Engine_D(cls):
        """
        Makes a connection to Database_D
        """
        db_dsn = cx_Oracle.makedsn(
            host="database_d.company.com",
            port=1521,
            service_name="DATABASE_D_NAME.COMPANY.COM",
        )
        return create_engine("oracle+cx_oracle://user_name:password@%s" % db_dsn)

    @classmethod
    def Engine_E(cls):
        """
        returns an sqlalchemy engine to Database_E
        Example:

        >>> engine = db_connect.Engine_E()
        """
        _params = urllib.parse.quote(
            "DRIVER={SQL Server};SERVER=DATABASE_E_NAME;DATABASE=Database_E;UID=user_name;PWD=password"
        )

        return create_engine("mssql+pyodbc:///?odbc_connect=%s" % _params)

    @classmethod
    def Engine_F(cls):
        """
        returns an sqlalchemy engine to Database_F
        Example:

        >>> engine = db_connect.Engine_F()
        """
        _params = urllib.parse.quote(
            "DRIVER={SQL Server};SERVER=DATABASE_F_NAME;DATABASE=Database_E;UID=user_name;PWD=password"
        )

        return create_engine("mssql+pyodbc:///?odbc_connect=%s" % _params)

    @classmethod
    def Engine_G(cls):
        """
        returns an sqlalchemy engine to Database_G
        Example:

        >>> engine = db_connect.Engine_G()
        """
        _params = urllib.parse.quote(
            "DRIVER={SQL Server};SERVER=DATABASE_G_NAME;DATABASE=Database_E;UID=user_name;PWD=password"
        )

        return create_engine("mssql+pyodbc:///?odbc_connect=%s" % _params)

    @classmethod
    def Engine_H(cls):
        """
        returns an sqlalchemy engine to Database_H
        Example:

        >>> engine = db_connect.Engine_H()
        """
        _params = urllib.parse.quote(
            "DRIVER={SQL Server};SERVER=DATABASE_H_NAME;DATABASE=Database_E;UID=user_name;PWD=password"
        )

        return create_engine("mssql+pyodbc:///?odbc_connect=%s" % _params)

    @classmethod
    def Engine_I(cls):
        """
        returns an sqlalchemy engine to Database_I
        Example:

        >>> engine = db_connect.Engine_I()
        """
        _params = urllib.parse.quote(
            "DRIVER={SQL Server};SERVER=DATABASE_I_NAME;DATABASE=Database_E;UID=user_name;PWD=password"
        )

        return create_engine("mssql+pyodbc:///?odbc_connect=%s" % _params)

    @classmethod
    def Engine_J(cls):
        """
        returns an sqlalchemy engine to Database_J
        Example:

        >>> engine = db_connect.Engine_J()
        """
        _params = urllib.parse.quote(
            "DRIVER={SQL Server};SERVER=DATABASE_J_NAME;DATABASE=Database_E;UID=user_name;PWD=password"
        )

        return create_engine("mssql+pyodbc:///?odbc_connect=%s" % _params)
