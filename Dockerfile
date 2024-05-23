###############################################################################
#   Copyright (C) 2024 Shane aka, ShaYmez <support@gb7nr.co.uk>  
#   Version 2.0.1
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software Foundation,
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
###############################################################################

FROM python:alpine3.16

COPY entrypoint /entrypoint

RUN adduser -D -u 54000 radio && \
        apk update && \
        apk add git gcc musl-dev curl && \
        curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf -y | sh && \
        pip install --upgrade pip && \
        pip cache purge && \
        cd /opt && \
        git clone https://github.com/shaymez/HBMonv2.git /hbmon && \
        cd /hbmon && \
        pip install --no-cache-dir -r requirements.txt && \
        apk del git gcc musl-dev curl && \
        chown -R radio: /hbmon

USER radio

ENTRYPOINT [ "/entrypoint" ]
