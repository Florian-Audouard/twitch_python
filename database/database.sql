DROP TABLE IF EXISTS data_twitch CASCADE;


CREATE TABLE data_twitch(
    id_data int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    un_text text
);