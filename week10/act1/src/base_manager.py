class BaseManager:
    """Base class for managers with common database filter utilities."""

    def _generate_null_filter(self, query_parts, column, value):
        # NULL filters cannot use the usual parameter placeholder syntax.
        if value == "NOT NULL":
            query_parts.append(f"{column} IS NOT NULL")
        else:
            query_parts.append(f"{column} IS NULL")

    def _generate_numeric_filter(self, query_parts, values, column, value, raw_value):
        # Numeric filters support simple comparison prefixes such as >=10 or !=0.
        op = None
        if value.startswith(">="):
            op = ">="
            value = value[2:].strip()
        elif value.startswith("<="):
            op = "<="
            value = value[2:].strip()
        elif value.startswith(">"):
            op = ">"
            value = value[1:].strip()
        elif value.startswith("<"):
            op = "<"
            value = value[1:].strip()
        elif value.startswith("!="):
            op = "!="
            value = value[2:].strip()
        elif value.startswith("="):
            op = "="
            value = value[1:].strip()
        if op is None:
            # default numeric filter is equality when no operator is provided
            op = "="
        try:
            numeric_value = int(value)
            query_parts.append(f"{column} {op} ?")
            values.append(numeric_value)
        except ValueError:
            # fallback to LIKE for invalid numeric values
            query_parts.append(f"{column} LIKE ?")
            values.append(f"%{raw_value}%")

    def _generate_where_clause(self, filters, numeric_columns):
        # Convert keyword filters into a parameterized WHERE clause shared by managers.
        query_parts = []
        values = []
        for column, raw_value in filters.items():
            value = "NULL" if raw_value is None else str(raw_value).strip()
            normalized_value = value.upper()
            if normalized_value in {"NULL", "NONE", "IS NULL"}:
                self._generate_null_filter(query_parts, column, "NULL")
                continue
            if normalized_value in {"NOT NULL", "IS NOT NULL"}:
                self._generate_null_filter(query_parts, column, "NOT NULL")
                continue
            if column in numeric_columns:
                self._generate_numeric_filter(query_parts, values, column, value, str(raw_value))
            else:
                query_parts.append(f"{column} LIKE ?")
                values.append(f"%{raw_value}%")
        where_clause = "WHERE " + " AND ".join(query_parts) if query_parts else ""
        return where_clause, values
