import logging

from neutronclient.neutron import v2_0 as neutronV20


class ListQoS(neutronV20.ListCommand):
    resource = 'qos'
    log = logging.getLogger(__name__ + '.ListQoS')

    list_columns = [
        'id', 'description', 'type', 'policy'
    ]


class ShowQoS(neutronV20.ShowCommand):
    resource = 'qos'
    log = logging.getLogger(__name__ + '.ShowQoS')


class DeleteQoS(neutronV20.DeleteCommand):
    resource = 'qos'
    log = logging.getLogger(__name__ + '.DeleteQoS')


class UpdateQoS(neutronV20.UpdateCommand):
    resource = 'qos'
    log = logging.getLogger(__name__ + '.UpdateQoS')

    def args2body(self, parsed_args):
        body = {self.resource: {}}
        body[self.resource]['policies'] = {}
        if parsed_args.policies:
            for parg in parsed_args.policies:
                args = parg.split('=')
                body[self.resource]['policies'][args[0]] = args[1]
        return body


class CreateQoS(neutronV20.CreateCommand):
    resource = 'qos'
    log = logging.getLogger(__name__ + '.CreateQoS')

    def add_known_arguments(self, parser):
        parser.add_argument('--type',
                            help="QoS Type", choices=['dscp', 'ratelimit'])
        parser.add_argument('--policies',
                            help='Set of policies for a QoS', nargs='*')
        parser.add_argument('--description', help="description for the QoS")

    def args2body(self, parsed_args):
        body = {self.resource: {}}

        body[self.resource]['policies'] = {}
        if parsed_args.policies:
            for parg in parsed_args.policies:
                args = parg.split('=')
                body[self.resource]['policies'][args[0]] = args[1]
        if parsed_args.type:
            body[self.resource]['type'] = parsed_args.type
        if parsed_args.description:
            body[self.resource]['description'] = parsed_args.description
        if parsed_args.tenant_id:
            body[self.resource].update({'tenant_id': parsed_args.tenant_id})
        return body
