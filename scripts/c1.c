#include <stdio.h>
#include "mongo.h"

int main() {
  mongo conn[1];
  status = mongo_connect( conn, "127.0.0.1", 27017 );

  if( status != MONGO_OK ) {
      switch ( conn->err ) {
        case MONGO_CONN_SUCCESS:    printf( "connection succeeded\n" ); break;
        case MONGO_CONN_BAD_ARG:    printf( "bad arguments\n" ); return 1;
        case MONGO_CONN_NO_SOCKET:  printf( "no socket\n" ); return 1;
        case MONGO_CONN_FAIL:       printf( "connection failed\n" ); return 1;
        case MONGO_CONN_NOT_MASTER: printf( "not master\n" ); return 1;
      }
  }

  mongo_destroy( conn );

  return 0;
}
