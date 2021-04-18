from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left emtpy")
    parser.add_argument('passwd',
                        type=str,
                        required=True,
                        help="This field cannot be left empty")
    
    def post(self):
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_name(data['username']):
            return {'message': 'User already registered'}, 400
        
        user = UserModel(**data)
        user.save_to_db()
        
        return {'message': 'User created'}, 201