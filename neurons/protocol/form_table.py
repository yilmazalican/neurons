# encoding: utf8
#
# This file is part of the Neurons project.
# Copyright (c), Burak Arslan <burak.arslan@arskom.com.tr>,
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the {organization} nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#


from spyne import ModelBase
from spyne.protocol.html import HtmlColumnTable
from spyne.util.cdict import cdict

from neurons.protocol.form import HtmlForm


class HtmlFormTable(HtmlColumnTable):
    def __init__(self, app=None, ignore_uncap=False, ignore_wrappers=False,
                       cloth=None, attr_name='spyne_id', root_attr_name='spyne',
                                                             cloth_parser=None):

        super(HtmlFormTable, self).__init__(app=app,
                     ignore_uncap=ignore_uncap, ignore_wrappers=ignore_wrappers,
                cloth=cloth, attr_name=attr_name, root_attr_name=root_attr_name,
                                                      cloth_parser=cloth_parser)

        self.serialization_handlers = cdict({
            ModelBase: self.model_base_to_parent,
        })

        self.prot_form = HtmlForm()

    def model_base_to_parent(self, ctx, cls, inst, parent, name, array_index=None,
                                                      from_arr=False, **kwargs):
        if from_arr:
            with parent.element('tr'):
                with parent.element('td'):
                    self.prot_form.to_parent(ctx, cls, inst, parent, name, **kwargs)

        else:
            self.prot_form.to_parent(ctx, cls, inst, parent, name, **kwargs)