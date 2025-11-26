
from src.db.de_connection import execute_query
from src.db.ticket_field import TICKET_METADATA_FIELDS

class Ticket:
     def __init__(self, metadata, description, embedding=None):
        self.metadata = metadata
        self.description = description
        self.embedding = embedding

class TicketRepository:
        def __init__(self, db_config):
                self.db_config = db_config

        def _fetch_tickets(self, fields=None, filters=None):
                fields = fields or TICKET_METADATA_FIELDS + ["description"]
                valid_fields = set(TICKET_METADATA_FIELDS + ["description"])
                for field in fields:
                        if field not in valid_fields:
                                raise ValueError(f"Invalid field: {field}")
                select_clause = ", ".join(fields)
                query = f"SELECT {select_clause} FROM customer_support_ticket"
                params = []
                if filters:
                        where_clauses = " AND ".join([f"{k} = %s" for k in filters])
                        query += f" WHERE {where_clauses}"
                        params = list(filters.values())
                rows = execute_query(query, params)
                tickets = []
                for row in rows:
                        metadata = {field: val for field, val in zip(fields, row) if field != "description"}
                        description = row[fields.index("description")] if description in fields else ""
                        tickets.append(Ticket(metadata, description))
                return tickets
    
        def get_all_(self):
                return self._fetch_tickets()

        def get_by_filter(self, **filters):
               return self._fetch_tickets(filters=filters)
        
        def fetch_custom(self, fields, filters=None):
               return self._fetch_tickets(fields=fields, filters=filters)