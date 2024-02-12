import pandas as pd
from datetime import datetime


class FlightData:
    # This class is responsible for managing flight data

    def populate_flights_df(self, data):
        # Initialize DataFrame with necessary columns
        self.flights_df = pd.DataFrame(
            columns=[
                "airline",
                "price",
                "departure_city",
                "departure_airport",
                "arrival_city",
                "arrival_airport",
                "outbound_date",
                "inbound_date",
            ]
        )

        # Prepare a list to store flight data
        rows = []

        # Loop through the data and populate the rows list
        for row in data["data"]:
            rows.append(
                {
                    "airline": row["airlines"][0],
                    "price": row["price"],
                    "departure_city": row["route"][0]["cityFrom"],
                    "departure_airport": row["route"][0]["flyFrom"],
                    "arrival_city": row["route"][0]["cityTo"],
                    "arrival_airport": row["route"][0]["flyTo"],
                    "outbound_date": datetime.strptime(
                        row["route"][0]["local_departure"], "%Y-%m-%dT%H:%M:%S.%fZ"
                    ),
                    "inbound_date": (
                        datetime.strptime(
                            row["route"][1]["local_departure"], "%Y-%m-%dT%H:%M:%S.%fZ"
                        )
                        if len(row["route"]) > 1
                        else None
                    ),
                }
            )

        # Add the rows to the DataFrame
        self.flights_df = pd.concat(
            [self.flights_df, pd.DataFrame(rows)], ignore_index=True
        )

        # Return the populated DataFrame
        return self.flights_df
